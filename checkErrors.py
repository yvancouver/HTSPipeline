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
    print string
    list_of_files_path= False
    for dirname, dirnames, filenames in os.walk(location):
        for filename in filenames:
#            print filename
            file_path=os.path.join(dirname, filename)
            if string in filename:
                list_of_files_path = file_path
            
    return list_of_files_path

'''
            if ".txt" in file_path:
                f = open( file_path, 'r' )
                for line in f:
                    if string in line:
                        if f.name not in list_of_files: list_of_files.append(f.name )
    files = sorted(set(list_of_files))

    
    if len(files) == 0 :
        msg = "Could not find the TaqMan results for "+ SampleID +" plus precisement "+ string + " in here "+ location
        sys.exit(msg)
    elif len(files) > 1:
        print "This Sample ID ",SampleID," having  this ID <",string,"> is present in different files\nWhich one is it?"
        index =1
        for i in files:
            print index, i
            index += 1
        reponse = raw_input()
        taq_file = files[int(reponse)-1]
        return(taq_file)
    else:
        return(files)
'''
def evaluateSizeFile(filepath):
    statinfo = os.stat(filepath)
    return(statinfo.st_size)

def KeywordsSearch(file_path,keyword):
    fh = open( file_path, 'r' )
    checked = False
    for line in fh:
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
                                    'errVariantRecalibratorSNP': 1000,
                                    'errConvert2annovarAll': 1000,
                                    'errConvert2annovarInCand': 1000,
                                    'errTableAnnovarAll': 1000,
                                    'errTableAnnovarInCand': 1000,
                                    'bwaTest': 721}

list_of_errors_containing_files = { 'errTableAnnovarInCand': 1000,
                                    'bwaTest': 721
                                  }

location = os.getcwd()

for error_file in list_of_errors_containing_files:
    print "\nSearch this file ", error_file

    target=FindFiles(error_file,location)
    if target:
        print "evalute this  ",target
        size = evaluateSizeFile(target)
        #print size, " of ", target
        if size == list_of_errors_containing_files[error_file]:
            print "GOOD"
        else:
            print "Need to check if content if OK"
            print "Runtime.total , "
            test = KeywordsSearch(target,"Runtime")
            if test:
                print "NOWORRIES"
            else:
                print"really bad"
                print "one need to check ", target
    else:
        print "Nothingfound"