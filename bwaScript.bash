#!/bin/bash

# BWA alignment for SR and PE sequences
# BWA does gapped global alignment w.r.t queries, supports paired-end reads and is one of the fastest short read alignment algorithms (achieves this by using the Burrows-Wheeler transform).

# INPUTS
# See below

# SUMMARY OF PROCEDURE AND MAIN OUTPUT
# Indexing: the database in fasta format needs to be indexed (takes a few hours). This is not done in the script as it only needs to be done once.
# Alignment: finds the suffix array coordinates of good hits of each individual read
# Convert (samse and sampe): convert the SA coords to chromosomal coords and pair reads for PE data (finding pair is not obvious as each member of pair may have ambiguous mapping)
# --> SAM alignment file 

# OTHER OUTPUTS
# --> insSizeStats.txt: insert size statistics (produced as the sam file is produced when calling sampe).
# --> readClassification.txt: number of reads mapped (uniquely and ambiguously) and unmapped (produced by an analysis of the sam file). Treats PE reads as SR reads. Read classification is in fact more complex in the case of PE data. 
# For example a mate in a pair may not be mapped or may be mapped but in an anamalous position. A more complex read classification in the case of PE data is obtained from the flagstat command in samtools (This is called in the samtools script).



#################### KEY INPUTS #############################################


# Use absolute path of the dir as the query reads might be in pre-processing, but can also be in seqData.
declare readsDir="/Users/tim/home/platform/seqData/100916_PCUS-319-EAS487_0008/Data/Intensities/BaseCalls/GERALD_27-09-2010_SBSUser";

# Reads (specify full name with all extensions whether compressed or not))
declare read1Files=( \
${readsDir}/"s_1_1_sequence.txt" \
);

declare read2Files=( \
${readsDir}/"s_1_2_sequence.txt" \
);

# Need by sampe when forming pairs
declare maxInsSize=600;

# Set this to reasonable value so that computes at optimal speed.
declare nbThreads=4;

## ref db which reference indexed using bwa
# Contains:
# allChr.fa.amb
# allChr.fa.ann
# allChr.fa.bwt
# allChr.fa.pac
# allChr.fa.rbwt
# allChr.fa.rpac
# allChr.fa.rsa
# allChr.fa.sa
declare refDb="/Users/tim/home/platform/ref/hg18/bwa/allChr.fa";


################## PROGRAM VERSIONS USED ##########################################


#Define which version of bwa to use
declare bwaDir="/Users/tim/home/bin/bwa-0.5.5";

#Define which version of maq to use (need this for conversion from Illumina to Sanger)
declare maqDir="${h}/bin/maq-0.7.1/scripts";



################## ANALYSIS #############################################


# Only gunzip the files if need to and convert from illumina to Sanger.
# This way of doing it avoids having to gunzip and then gzip again when finished.

# Determine whether the read files are zipped up
declare ext=`echo ${read1Files[0]} | sed 's/.*\.\(.*\)/\1/'`;
echo "Converting Illumina format to Sanger format";


# Convert first read
if [ $ext == "gz" ]; then
	gunzip -c ${read1Files[@]} | ${maqDir}/fq_all2std.pl ill2std > reads1.fq;
else
	cat ${read1Files[@]} | ${maqDir}/fq_all2std.pl ill2std > reads1.fq
fi

# Convert PE if it exists
if [ ${read2Files} ]; then
	if [ $ext == "gz" ]; then
		gunzip -c ${read2Files[@]} | ${maqDir}/fq_all2std.pl ill2std > reads2.fq;
	else
		cat ${read2Files[@]} | ${maqDir}/fq_all2std.pl ill2std > reads2.fq
	fi
fi




# bwa aln [-n maxDiff] [-o maxGapO] [-e maxGapE] [-d nDelTail] [-i nIndelEnd] [-k maxSeedDiff] [-l seedLen] [-t nThrds] [-cRN] [-M misMsc] [-O gapOsc] [-E gapEsc] [-q trimQual] <in.db.fasta> <in.query.fq> > <out.sai>
# 
# Find the SA coordinates of the input reads. Maximum maxSeedDiff differences are allowed in the first seedLen subsequence and maximum maxDiff differences are allowed in the whole sequence.
# 
# OPTIONS:
# -n NUM	 Maximum edit distance if the value is INT, or the fraction of missing alignments given 
# 		2% uniform base error rate if FLOAT. In the latter case, the maximum edit distance is 
# 		automatically chosen for different read lengths. [0.04]
# -o INT	 Maximum number of gap opens [1]
# -e INT	 Maximum number of gap extensions, -1 for k-difference mode (disallowing long gaps) [-1]
# -d INT	 Disallow a long deletion within INT bp towards the 3’-end [16]
# -i INT	 Disallow an indel within INT bp towards the ends [5]
# -l INT	 Take the first INT subsequence as seed. If INT is larger than the query sequence, 
# 		seeding will be disabled. For long reads, this option is typically ranged from 25 to 35 
# 		for ‘-k 2’. [inf]
# -k INT	 Maximum edit distance in the seed [2]
# -t INT	 Number of threads (multi-threading mode) [1]
# -M INT	 Mismatch penalty. BWA will not search for suboptimal hits with a score lower than (bestScore-misMsc). [3]
# -O INT	 Gap open penalty [11]
# -E INT	 Gap extension penalty [4]
# -R INT	 Proceed with suboptimal alignments if there are no more than INT equally best hits. This 
# 		option only affects paired-end mapping. Increasing this threshold helps to improve the 
# 		pairing accuracy at the cost of speed, especially for short reads (~32bp).
# -c		 Reverse query but not complement it, which is required for alignment in the color space.
# -N	 	Disable iterative search. All hits with no more than maxDiff differences will be found. This 
# 		mode is much slower than the default.
# -q INT	 Parameter for read trimming. BWA trims a read down to argmax_x{\sum_{i=x+1}^l(INT-q_i)} 
# 		if q_l<INT where l is the original read length. [0]

# Align first set of reads
${bwaDir}/bwa aln -t ${nbThreads} ${refDb} reads1.fq > aln1.sai

# Align second set of reads if they are present
if [ -e reads2.fq ]; then
	${bwaDir}/bwa aln -t ${nbThreads} ${refDb} reads2.fq > aln2.sai
fi



# Generate alignments in the SAM format given single-end reads. Repetitive hits will be randomly chosen
# Usage: bwa samse [-n max_occ] <in.db.fasta> <in.sai> <in.fq> > <out.sam>
#
# Options: -n INT   Maximum number of alignments to output in the XA tag for reads paired properly. If a read has more than INT hits, the XA tag will not be written.

# Usage: bwa sampe [-a maxInsSize] [-o maxOcc] [-n maxHitPaired] [-N maxHitDis] [-P] <in.db.fasta> <in1.sai> <in2.sai> <in1.fq> <in2.fq> > <out.sam>
# Generate alignments in the SAM format given paired-end reads. Repetitive read pairs will be placed randomly.
# 
# OPTIONS:
# -a INT	 Maximum insert size for a read pair to be considered being mapped properly. 
# 		Since 0.4.5, this option is only used when there are not enough good alignment to infer the 
# 		distribution of insert sizes. [500]
# -o INT	 Maximum occurrences of a read for pairing. A read with more occurrneces will be treated as 
# 		a single-end read. Reducing this parameter helps faster pairing. [100000]
# -P	 	Load the entire FM-index into memory to reduce disk operations (base-space reads only). With 
# 		this option, at least 1.25N bytes of memory are required, where N is the length of the genome.
# -n INT	 Maximum number of alignments to output in the XA tag for reads paired properly. If a read
# 		has more than INT hits, the XA tag will not be written. [3]
# -N INT	 Maximum number of alignments to output in the XA tag for disconcordant read pairs 
# 		(excluding singletons). If a read has more than INT hits, the XA tag will not be written. [10]

if [ -e reads2.fq ]; then
	echo "Running sampe";
	echo "Output on progress being send to sampeStdError.txt, but will also appear on screen when finished";
	${bwaDir}/bwa sampe -a ${maxInsSize} ${refDb} aln1.sai aln2.sai reads1.fq reads2.fq >aln.sam 2>sampeStdError.txt;
	cat sampeStdError.txt;
	cat sampeStdError.txt | grep "infer_isize" > insSizeStats.txt;
	rm sampeStdError.txt;
else
	${bwaDir}/bwa samse ${refDb} aln1.sai reads1.fq > aln.sam
fi

echo "Deleting the sai files as no longer needed";
rm -f aln1.sai aln2.sai;

echo "Computing the basic read classification";
cat aln.sam | awk 'BEGIN{unmapped=0; unique=0; ambiguous=0};($1 !~ /^@/){if($3!="*"){if($5==0){ambiguous=ambiguous+1}else{unique=unique+1}}else{unmapped=unmapped+1}};END{print "Unmapped: " unmapped "\n";print "Mapping uniquely: " unique "\n"; print "Mapping ambiguously: "  ambiguous  "\n"}' > readClassification.txt;

echo "Gzipping sam file";
gzip aln.sam;


# Compress the Sanger format sequences for record
# This means that we have two copies of the sequences one in Illumina format (input to this script)
# and one in sanger format.
# Could also consider deleting this file (as it just the qualities that have been converted from Illumina to Sanger)
echo "Compressing the Sanger read files";
gzip reads1.fq;
if [ -e reads2.fq ]; then
	gzip reads2.fq;
fi

echo "Script completed";





