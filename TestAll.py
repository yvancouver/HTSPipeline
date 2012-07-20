# October 2011 Yvan strahm OUS
# This should be the place where all test are called
# as well where the config file is located/called?
#
#
import doctest
import samtoolsTest
import bwaTest
import GATKTest
import PicardTest
import cutadaptTest

print "Bwa:\n", doctest.testmod(bwaTest)
print "Samtools:\n", doctest.testmod(samtoolsTest)
print "GATK:\n", doctest.testmod(GATKTest)
print "Picard:\n" , doctest.testmod(PicardTest)
