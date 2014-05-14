#! /opt/local/bin//python

######
## What do I want to do here,
# 1. Find a filefor the list of files
# 2. Evaluate his size
# 3 Look for keywords in the file

import sys
import os
import time

def FindFiles(string,location):
    list_of_files_path= False
    for dirname, dirnames, filenames in os.walk(location):
        for filename in filenames:
#            print filename
            file_path=os.path.join(dirname, filename)
            if string in filename:
                list_of_files_path = file_path
            
    return list_of_files_path

def evaluateSizeFile(filepath):
    statinfo = os.stat(filepath)
    return(statinfo.st_size)

def KeywordsSearch(file_path,keywords):
    fh = open( file_path, 'r' )
    checked = False
    for line in fh:
        for keyword in keywords:
            if keyword in line:
                checked = True
        
    return checked

list_of_errors_containing_files = { 'errIndelRealigner': 0,
                                    'errRealignerTargetCreator': 0,
                                    'errMarkDup': 1000,
                                    'errAnalyzeCovariates': 0,
                                    'errBaseRecalibratorPost': 0,
                                    'errBaseRecalibratorPre': 0,
                                    'errPrintReads': 0,
                                    'errCollectAlignmentSummaryMetrics': 1000,
                                    'errCollectInsertSizeMetrics': 1000,
                                    'errCalculateHsMetrics': 1000,
                                    'errSelectVariantsIndel': 0,
                                    'errSelectVariantsSNP': 0,
                                    'errSnpFingerPrintingTestUnifiedGenotyper': 0,
                                    'errUnifiedGenotyper': 0,
                                    'errCombineVariants': 0,
                                    'errVariantFiltrationIndel': 0,
                                    'errVariantRecalibratorSNP': 0,
                                    'errConvert2annovarAll': 1000,
                                    'errConvert2annovarInCand': 1000,
                                    'errTableAnnovarAll': 1000,
                                    'errTableAnnovarInCand': 1000
                                    }



location = os.getcwd()
keywords = ["NOTICE","Runtime.totalMemory"]
for error_file in list_of_errors_containing_files:
    #print "\nSearch this file ", error_file

    target=FindFiles(error_file,location)
    if target:
        #print "evalute this  ",target
        size = evaluateSizeFile(target)
        #print size, " of ", target
        if size == list_of_errors_containing_files[error_file]:
            pass
#            print "GOOD"
        else:
#            print "Need to check if content if OK"
            test = KeywordsSearch(target,keywords)
            if test:
                pass
#                print "NOWORRIES"
            else:
                print"really bad"
                print "one need to check "
                sys.exit(target)
    else:
        print error_file, "\t Not Found.\nIs the analysis finished or incomplete"
        print "\t\t PLEASE CHECK\n"
