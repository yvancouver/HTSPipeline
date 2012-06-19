#Yvan Strahm  2012 yvan.strahm@gmail.com
# take a fastq file and chop it according to a certain nuber of line
# usage split.py Diag-HaloBRCA1A-test-6_GCCAAT_L004_R1_001.pf.fastq 4000000 
# Will split a illumina file into 1000000 reads

#import os
#import sys
from sys import argv

#index lines in ori
i = 1
#index subdirectory
j = 1

#open file
ori = open(argv[1], "r" )
#open output file
d = open( str(j),"w+")

for line in ori:
    d.write(line)
    i +=1
    if i > int(argv[2]):
        d.close()
        j += 1
        d = open( str(j),"w+")
        i = 1
