#!python

import os
import re
import sys
import gzip
import time
import urllib
import requests
import argparse
import subprocess
import numpy as np
import pandas as pd
from Bio import Entrez
from datetime import datetime
from mycotools.lib.kontools import intro, outro, formatPath, prep_output, eprint, vprint, findExecs
from mycotools.lib.dbtools import log_editor, loginCheck, db2df


def prepareFolders( output_path, gff, prot, assem, transcript ):

    file_types = []
    if assem:
        if not os.path.exists(output_path + 'assembly'):
            os.mkdir(output_path + 'assembly')
        file_types.append( 'assembly' )
    if gff:
        if not os.path.exists(output_path + 'gff3'):
            os.mkdir(output_path + 'gff3')
        file_types.append( 'gff3' )
    if prot:
        if not os.path.exists(output_path + 'proteome'):
            os.mkdir(output_path + 'proteome')
        file_types.append( 'proteome' ) 
    if transcript:
        if not os.path.exists(output_path + 'transcript'):
            os.mkdir(output_path + 'transcript')
        file_types.append( 'transcript' )

    return file_types  


def compileLog( output_path, remove = False ):

    ass_prots = {}
    if not os.path.isfile( output_path + 'ncbiDwnld.log' ):
        with open( output_path + 'ncbiDwnld.log', 'w' ) as out:
            out.write('#ome\tassembly_acc\tassembly\tproteome\tgff3\ttranscript\t' + \
            'assemMD5\tprotMD5\tgff3MD5\ttransMD5\tgenome_id(s)')

        # too risky, too many things can go wrong and then users would be in a
        # loop, but necessary for huge downloads
    else:
        with open( output_path + 'ncbiDwnld.log', 'r' ) as raw:
            for line in raw:
                if not line.startswith('#'):
                    data = [x.rstrip() for x in line.split('\t')]
                    while len(data) < 10:
                        data.append('')
                    ass_prots[data[0]] = { 
                        'assembly_acc': str(data[1]), 'assembly': str(data[2]), 
                        'proteome': str(data[3]), 'gff3': str(data[4]), 
                        'transcript': str(data[5]), 'assembly_md5': str(data[6]),
                        'proteome_md5': str(data[7]), 'gff3_md5': str(data[8]),
                        'transcript_md5': str(data[9]), 'genome_id': data[10].split(',')
                        }

    return ass_prots

def acquire_genome_ids(accession, column, database = 'assembly'):
    search_term, esc_count = accession + '[' + column + ']', 0
    while esc_count < 10:
        try:
            handle = Entrez.esearch(db=database, term=search_term)
            genome_ids = Entrez.read(handle)['IdList']
            break
        except (RuntimeError, urllib.error.HTTPError) as e:
            time.sleep(1)
            esc_count += 1
    else:
        print('\tERROR:', accession, 'failed to search NCBI')
    return genome_ids

def acquire_ftp_path(ID, database):

    esc_count = 0
    while esc_count < 10:
        esc_count += 1
        try:
            handle = Entrez.esummary(db=database, id=ID, report="full")
            record = Entrez.read(handle, validate = False)
        except urllib.error.HTTPError:
            time.sleep(0.1)
            continue
        try:
            ftp_path = str(record['DocumentSummarySet']['DocumentSummary'][0]['FtpPath_GenBank'])
        except IndexError:
            time.sleep(0.1)
            continue
        assemblyID = record['DocumentSummarySet']['DocumentSummary'][0]['AssemblyAccession']
        esc_count = 0
        break
    else:
        if esc_count >= 10:
            raise urllib.error.HTTPError('\tERROR: FTP request failed')

    return ftp_path, assemblyID

# collects paths to download proteomes and assemblies
def collect_ftps(
    ncbi_df, ass_prots, api_key=0, column = 'assembly_acc',
    ncbi_column='Assembly Accession', database="assembly", output_path = '',
    verbose=True, remove = False
    ):

    eprint('\nAssembling NCBI ftp directories', flush = True)
    count, failed = 0, []

# for each row in the assembly, grab the accession number, form the search term for Entrez, use Entrez,
    out_df = pd.DataFrame()
    for accession, row in ncbi_df.iterrows():
        if pd.isnull(row[column]):
            ass_prots[str(accession)] = {
                'accession': accession, 'assembly': '',
                'proteome': '', 'gff3': '', 'transcript': '',
                'assembly_md5': '', 'proteome_md5': '',
                'gff3_md5': '', 'transcript_md5': '', 'genome_id': ''
                }
            failed.append([accession, datetime.strftime(row['version'], '%Y%m%d')])
            continue

        if accession in ass_prots: # add all rows that have indices associated with this
            out_df = out_df.append(row)
            icount = 1
            test = str(accession) + '_' + str(icount)
            while test in ass_prots:
                count += 1
#                row['assembly_acc'] = ass_prots[test]['genome_id']
                if 'ome' in row.keys():
                    row['ome'] = None # haven't assigned a mycotools ID yet
                out_df = out_df.append(row)
                test = str(accession) + '_' + str(icount)
            continue

        if ncbi_column not in {'assembly'}:
            genome_id = acquire_genome_ids(accession, ncbi_column, database = 'assembly')
        else:
            genome_id = [accession]

        if ncbi_column in {'assembly', 'genome'}: # be confident it is the most
        # recent assembly UID
            genome_id = [str(max([int(i) for i in genome_id]))]

        if not genome_id: # No IDs retrieved
            if 'ome' in row.keys():
                accession = row['ome']
            eprint('\t' + accession + ' failed to find genome ID', flush = True)
            try:
                failed.append([accession, datetime.strftime(row['version'], '%Y%m%d')])
            except TypeError: # if the row can't be formatted as a date
                failed.append([accession, row['version']])
            continue

        icount = 0
        for ID in genome_id:
            if count:
                new_acc = str(accession) + '$' + str(icount)
            else:
                new_acc = accession
# obtain the path from a summary of the ftp directory and create the standard paths for proteomes and assemblies
            ass_prots[str(new_acc)] = {
                'accession': accession, 'assembly': '', 'proteome': '', 
                'gff3': '', 'transcript': '', 'assembly_md5': '',
                'proteome_md5': '', 'gff3_md5': '', 
                'transcript_md5': '', 'genome_id': ID
                }

            ftp_path, genbank_id = acquire_ftp_path(ID, database)
            if not ftp_path:
                eprint('\t' + accession + ' failed to return any FTP path', flush = True)
                failed.append([accession, datetime.strftime(row['version'], '%Y%m%d')])
                continue

            esc_count = 0
            ass_md5, gff_md5, trans_md5, prot_md5, md5s = '', '', '', '', {}
            basename = os.path.basename(ftp_path)
            while True:
                try:
                    esc_count += 1
                    request = requests.get( 
                        (ftp_path + '/md5checksums.txt').replace('ftp://','https://'), timeout = 120
                        )
                    break
                except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as e:
                    if esc_count == 20:
                        eprint('\n\tERROR: Failed to fulfill ftp request!', flush = True)
                        sys.exit(70)
                    count = 0
                    time.sleep(1)
            count += 1
            if request.status_code != 200:
                eprint('\t' + ome + '\tno ' + md5, flush = True)
                dwnld = 69
            else:
                dwnld = subprocess.call(
                    ['curl', ftp_path + '/md5checksums.txt', '-o', output_path + '.tmpmd5'], 
                    stdout = subprocess.PIPE, stderr = subprocess.PIPE
                    )
                count += 1
                with open( output_path + '.tmpmd5', 'r' ) as raw:
                    for line in raw:
                        data = line.rstrip().split('  ')
                        if data:
                            md5s[ftp_path + '/' + os.path.basename(data[1])] = data[0]
            tranname = os.path.basename(ftp_path.replace('/GCA','/GCF'))
            assembly = ftp_path + '/' + basename + '_genomic.fna.gz'
            if assembly in md5s:
                ass_md5 = md5s[assembly]
            else:
                assembly = ''
            proteome = ftp_path + '/' + basename + '_protein.faa.gz'
            if proteome in md5s:
                prot_md5 = md5s[proteome]
            else:
                proteome = ''
            gff3 = ftp_path + '/' + basename + '_genomic.gff3.gz'
            test_gff3 = re.sub( r'\.gff3\.gz$', '.gff.gz', gff3 )
            if gff3 in md5s:
                gff_md5 = md5s[gff3]
            elif test_gff3 in md5s:
                gff3 = test_gff3
                gff_md5 = md5s[gff3]
            else:
                gff3 = ''
    
            transcript = ftp_path.replace('/GCA', '/GCF') + '/' + tranname + '_rna.fna.gz'
            if transcript in md5s:
                trans_md5 = md5s[transcript]
    
            if (not assembly or not gff3) and remove:
                failed.append([accession, datetime.strftime(row['version'], '%Y%m%d')])
    
            log_editor( 
                output_path + 'ncbiDwnld.log', str(new_acc), 
                str(accession) + '\t' + accession + '\t' +  assembly + '\t' + \
                proteome + '\t' + gff3 + '\t' + transcript + '\t' + \
                ass_md5 + '\t' + prot_md5 + '\t' + gff_md5 + '\t' + trans_md5 + \
                '\t' + ID
                )
            ass_prots[str(new_acc)] = {
                'accession': accession, 'assembly': assembly, 'assembly_md5': ass_md5,
                'proteome': proteome, 'proteome_md5': prot_md5,
                'gff3': gff3, 'gff3_md5': gff_md5,
                'transcript': transcript, 'transcript_md5': trans_md5,
                'genome_id': ID
                }
            row['dwnld_id'] = ID
            if icount:
                if 'ome' in row:
                    row['ome'] = None
            out_df = out_df.append(row)
            icount += 1
    
    # if no API key is used, we can only generate 3 queries per second, otherwise we can use 10
            count += 1
            if not api_key:
                if count >= 2:
                    time.sleep( 1 )
                    count = 0
            else:
                if count >= 7:
                    time.sleep( 1 )
                    count = 0
    
    return ass_prots, failed, out_df

# download the file depending on the type inputted
def download_files(acc_prots, acc, file_types, output_dir, count,
                   remove = False, checkMD5 = False):

    esc_count, dwnlds = 0, {}
    for file_type in file_types:
        ftp_link = acc_prots[file_type]
        dwnlds[file_type] = -1
        if file_type == 'assembly':
            file_path = output_dir + 'assembly/' + \
                os.path.basename(acc_prots[file_type])
        elif file_type == 'gff3':
            file_path = output_dir + 'gff3/' + \
                os.path.basename(acc_prots[file_type])
        elif file_type == 'proteome':
            file_path = output_dir + 'proteome/' + \
                os.path.basename(acc_prots[file_type])
        elif file_type == 'transcript':
            file_path = output_dir + 'transcript/' + \
                os.path.basename(acc_prots[file_type])

        if os.path.isfile( file_path ):
            if checkMD5:
                count += 1
                md5_cmd = subprocess.run( [
                    'md5sum', file_path],
                    stdout = subprocess.PIPE )
                md5_res = md5_cmd.stdout.decode( 'utf-8' )
                md5_find = re.search(r'\w+', md5_res)
                md5 = md5_find[0]
                if md5 == acc_prots[file_type + '_md5']:
                    eprint('\t\t' + file_type + ': ' + os.path.basename(file_path), flush = True)
                    dwnlds[file_type] = 0
                    continue
            else:
                eprint('\t\t' + file_type + ': ' + os.path.basename(file_path), flush = True)
                dwnlds[file_type] = 0
                continue
        elif os.path.isfile( file_path[:-3] ):
            eprint('\t\t' + file_type + ': ' + os.path.basename(file_path), flush = True)
            dwnlds[file_type] = 0
            continue

        if ftp_link == '':
            dwnlds[file_type] = 15
            continue
        while True:
            try:
                esc_count += 1
                request = requests.get( ftp_link.replace('ftp://','https://' ))
                break
            except requests.exceptions.ConnectionError:
                if esc_count == 20:
                    eprint('\n\tERROR: Failed to fulfill ftp request!', flush = True)
                    sys.exit(71)
                time.sleep(1)
                count = 0
        count += 1
        if request.status_code != 200:
            eprint('\t\t' + file_type + ': ERROR, no file exists', flush = True)
            dwnlds[file_type] = 69
            acc_prots[file_type] = ''
            log_editor( output_dir + 'ncbiDwnld.log', str(acc), str(acc) + \
                '\t' + str(acc_prots['accession']) + '\t' + str(acc_prots['assembly']) + \
                '\t' + str(acc_prots['proteome']) + '\t' + str(acc_prots['gff3']) + \
                '\t' + str(acc_prots['transcript']) + '\t' + \
                str(acc_prots['assembly_md5']) + '\t' + \
                str(acc_prots['proteome_md5']) + '\t' + \
                str(acc_prots['gff3_md5']) + '\t' + \
                str(acc_prots['transcript_md5']) + '\t' + \
                str(','.join([str(x) for x in acc_prots['genacc_id']])))
            if remove and file_type in {'assembly', 'gff3'}:
                break
            continue

        count += 1
        dwnlds[file_type] = subprocess.call(
            ['curl', ftp_link, '-o', file_path], 
            stdout = subprocess.PIPE, stderr = subprocess.PIPE
            )

        if dwnlds[file_type] != 0:
            eprint('\t\t' + file_type + ': ERROR, download failed', flush = True)
            if remove and file_type in {'assembly', 'gff3'}:
                break
        else:
            if os.stat(file_path).st_size < 150:
                eprint('\t\t' + file_type + ': ERROR, file too small', flush = True)
#                       print('\t' + acc + '\t' + file_type + ' empty', flush = True)
                dwnlds[file_type] = 420
                if remove and file_type in {'assembly', 'gff3'}:
                    break
        eprint('\t\t' + file_type + ': ' + os.path.basename(file_path), flush = True)

    return dwnlds, count


def main( 
    api = None, 
    assembly = True, proteome = False, gff3 = True, transcript = False,
    ncbi_df = False, remove = False, output_path = os.getcwd(), verbose = False,
    column = 'assembly_acc', ncbi_column = 'Assembly', checkMD5 = True
    ):

    # initialize run directory and information
    output_path = formatPath(output_path)
    file_types = prepareFolders( 
        output_path, gff3, proteome, assembly, transcript
        )
    ass_prots = compileLog(output_path, remove )

    # check if ncbi_df is a dataframe, and import if not
    if not isinstance(ncbi_df, pd.DataFrame) and os.path.isfile(ncbi_df):
        ncbi_df = db2df(ncbi_df)
    if len(ncbi_df.index) == 0:
        ncbi_df = pd.DataFrame(
            {i: [v] for i, v in enumerate(list(ncbi_df.keys()))}
            )

    # make the modify date from a standard NCBI table the version if it does
    # not otherwise exist, else there isn't a version to reference
    if 'Modify Date' in ncbi_df.keys() and not 'version' in ncbi_df.keys():
        ncbi_df['version'] = pd.to_datetime(ncbi_df['Modify Date'])
    elif 'version' not in ncbi_df.keys():
        ncbi_df['version'] = ''

    ncbi_df = ncbi_df.set_index(pd.Index(list(ncbi_df[column])))
    ass_prots, failed, ncbi_df = collect_ftps( 
            ncbi_df, ass_prots, remove = remove,
            ncbi_column = ncbi_column, column = column, api_key=api,
            output_path = output_path, verbose = verbose
            )

    if remove:
        ass_prots = { 
            o: ass_prots[o] for o in ass_prots \
            if all(ass_prots[o][p] for p in ['assembly', 'gff3'])
            }
    new_df = pd.DataFrame()

    eprint('\nDownloading NCBI files', flush = True)
    count = 0
    for acc, data in ass_prots.items():
        if count >= 2:
            if not api:
                time.sleep(1)
                count = 0
            elif count >= 7:
                time.sleep(1)
                count = 0
        if acc not in set(ncbi_df[column]):
            continue
        eprint('\t' + str(acc), flush = True)
        if data:
            exits, count = download_files( 
                data, acc, file_types, output_path, 
                count, remove = remove, checkMD5 = checkMD5
                )
        else:
            check = ncbi_df[ncbi_df[column] == acc[:acc.find('$')]]
            # check for entries in the inputted table that match the accession
            # provided without version modification
            db_vers = datetime.strftime(row['version'], '%Y%m%d')
            failed.append([acc, db_vers])
            continue
        if 'assembly' in exits:
            if exits['assembly'] != 0:
                if '$' in acc:
                    t_acc = acc[:acc.find('$')]
                else:
                    t_acc = acc
                failed.append([t_acc, ncbi_df['version'][t_acc]])
                continue
        if 'gff3' in exits:
            if exits['gff3'] != 0:
                 failed.append([t_acc, ncbi_df['version'][t_acc]])
                 continue
        ncbi_df.at[acc, 'assemblyPath'] = output_path + 'assembly/' + \
            os.path.basename(ass_prots[acc]['assembly'])
        ncbi_df.at[acc, 'faa'] = output_path + 'proteome/' + \
            os.path.basename(ass_prots[acc]['proteome'])
        ncbi_df.at[acc, 'gffPath'] = output_path + 'gff3/' + \
            os.path.basename(ass_prots[acc]['gff3'])
        new_df = new_df.append( ncbi_df.loc[acc] )
 
    new_df = new_df.reset_index()
    return new_df, failed


def getSRA(assembly_acc, fastqdump = 'fastq-dump', pe = True):

    handle = Entrez.esearch(db='SRA', term=assembly_acc)
    ids = Entrez.read(handle)['IdList']
    for id in ids:
        handle = Entrez.esummary(db='SRA', id = id, report='full')
        records = Entrez.read(handle, validate = False)
        for record in records:
            srr = re.search(r'Run acc="(S\w+\d+)"', record['Runs'])[1]
            print('\t\t' + srr, flush = True)
            if pe:
                subprocess.call([
                    fastqdump, '--gzip', '--split-3', srr], 
                    stdout = subprocess.PIPE)
                if os.path.isfile(srr + '_1.fastq.gz'):
                    os.rename(srr + '_1.fastq.gz', assembly_acc + '_' + srr + '_1.fq.gz')
                    os.rename(srr + '_2.fastq.gz', assembly_acc + '_' + srr + '_2.fq.gz')
                else:
                    print('\t\t\tERROR: file failed', flush = True)
            else:
                subprocess.call([
                    fastqdump, '--gzip', srr],
                    stdout = subprocess.PIPE)
                if os.path.isfile(srr + '.fastq.gz'):
                    os.rename(srr + '.fastq.gz', assembly_acc + '_' + srr + '.fq.gz')
                else:
                    print('\t\t\tERROR: file failed', flush = True)


def goSRA(df, output = os.getcwd() + '/', pe = True):

    print()
    sra_dir = output + 'sra/'
    if not os.path.isdir(sra_dir):
        os.mkdir(sra_dir)
    os.chdir(sra_dir)
    fastqdump = findExecs('fastq-dump', exit = set('fastq-dump'))
    count = 0

    if 'sra' in df.keys():
        row_key = 'sra'
    else:
        row_key = 'assembly_acc'

    for i, row in df.iterrows():
        print('\t' + row[row_key], flush = True)
        getSRA(row[row_key], fastqdump[0])
        count +=1
        if count >= 10:
            time.sleep(1)
            count = 0


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required = True, \
    help = 'Space delimited accession; tab delimited file with -c')
    parser.add_argument('-a', '--assembly', action = 'store_true')
    parser.add_argument('-p', '--proteome', action = 'store_true')
    parser.add_argument('-g', '--gff3', action = 'store_true')
    parser.add_argument('-t', '--transcript', action = 'store_true')
    parser.add_argument('-s', '--sra', action = 'store_true', \
        help = 'Download SRAs only' )
    parser.add_argument('-pe', '--paired', action = 'store_true', \
        help = 'Download paired-end SRAs. (REQUIRES -s)')
    parser.add_argument('-c', '--column', \
        help = 'Accession column num/name; DEFAULT ["assembly_acc" | 0]')
    parser.add_argument('-n', '--ncbi_column', \
        help = 'NCBI database associated with column. ' \
            + '{"assembly", "biosample", "bioproject", "genome" ...}; ' \
            + 'DEFAULT: attempt to decipher')
    parser.add_argument( '-o', '--output', help = 'Output directory' )
    args = parser.parse_args()

    ncbi_email, ncbi_api, jgi_email, jgi_pwd = loginCheck(jgi = False) 

    Entrez.email = ncbi_email
    if ncbi_api:
        Entrez.api_key = ncbi_api

    if not args.output:
        output = os.getcwd() + '/'
    else:
        output = formatPath(args.output)

    args_dict = {
        'NCBI Table': args.input,
        'email': ncbi_email,
        'Assemblies': args.assembly,
        'Proteomes': args.proteome,
        ".gff3's": args.gff3,
        'Transcripts': args.transcript,
        'SRA': args.sra
    }

    start_time = intro('Download NCBI files',args_dict)
    if not args.assembly and not args.proteome and not args.gff3 and not args.sra and not args.transcript:
        eprint('\nERROR: You must choose at least one download option\nExit code 37', flush = True)
        sys.exit( 37 )

    if args.sra:
        if os.path.isfile(formatPath(args.input)):
            goSRA(pd.read_csv(formatPath(args.input), sep = '\t'), output, pe = args.paired)
        else:
            goSRA(pd.DataFrame({'sra': [args.input.rstrip()]}), output, pe = args.paired)
    else:
        if os.path.isfile(formatPath(args.input)):
            df = db2df(args.input) # db2df is deprecated, so this needs to change. move out of pandas in general
            if not column:
                if 'assembly_acc' in ncbi_df.keys():
                    column = 'assembly_acc'
                    ncbi_column = 'Assembly Accession'
                elif 'Assembly Accession' in ncbi_df.keys():
                    column = 'assembly_acc'
                    ncbi_column = 'Assembly Accession'
                else:
                    column = 0
            try:
                column = ncbi_df.columns[int(column)]
                ncbi_column = column
            except TypeError: # not an integer
                pass
            if not args.ncbi_column:
                if column.lower() in {'assembly'}:
                    ncbi_column = 'assembly'
                elif column.lower() in \
                    {'genome', 'assembly accession', 'assembly_acc'}:
                    ncbi_column = 'genome'
                elif column.lower() in {'biosample', 'biosample accession'}:
                    ncbi_column = 'biosample'
                else:
                    ncbi_column = column.lower()
            else:
                ncbi_column = args.ncbi_column.lower()
        else:
            df = pd.DataFrame({'assembly_acc': args.input.replace('"','').replace("'",'').split()})
    
        new_df, failed = main( 
            assembly = args.assembly, column = column, ncbi_column = ncbi_column,
            proteome = args.proteome, gff3 = args.gff3, transcript = args.transcript,
            ncbi_df = df, output_path = output, verbose = True
            )
        new_df.to_csv( args.input + '_dwnld', sep = '\t' )

    outro(start_time)
