
# This script expect to get the reference genome location and version,
# the reads location and the experiment name

import ConfigParser
import sys,io
from time import gmtime, strftime,localtime
from optparse import OptionParser

helpstr = '''ConfigSetup is use to configure the location and
the version of the software needed in the pipeline.
It also defines the location of the reference files and the reads file.
It is also needed/use by the test scripts to check consistency.

Author: Yvan Strahm (yvan.strahm@gmail.com)
Thanks to Tim Hugues and Ying Sheng for help.
Thanks to Sebastian Bassi for his book, Python for Bioinformatics (First Edition).

License: GPL 3.0 (http://www.gnu.org/licenses/gpl-3.0.txt)'''
usage = "\n"+helpstr + '\n\nusage: %prog Project name [options]'
parser = OptionParser(usage=usage)
parser.add_option("-p", "--project", dest="project", default=None,
                  help="name of project")
parser.add_option("-1", "--reads1", dest="reads1", default=None,
                  help="localisation of the read1 file")
parser.add_option("-2", "--reads2", dest="reads2", default=None,
                  help="localisation of the read2 file")

(opts,args) = parser.parse_args()
print "args", args


print "POTS" ,opts
#print "R1", opts.READ1
print "r1", opts.reads1
#print "R2", opts.READS2
print "r2", opts.reads2

if opts.project == None:
    errmsg = "Bad or missing project in input."
    errmsg += " This program requires a project name"
    errmsg += " Please see the help with -h or --help"
    parser.error(errmsg)
elif (opts.reads1 == None) or (opts.reads2 == None):
    errmsg = "Bad or missing read files in input."
    errmsg += " This program requires reads file"
    errmsg += " Please see the help with -h or --help"
    parser.error(errmsg)

# Test if the reads files exists
try:
    io.open(opts.reads1,'r')
except:
    errmsg = "Unreadable or missing read1 files in input."
    errmsg += " This program requires a readable reads file"
    errmsg += " Please see the help with -h or --help"
    parser.error(errmsg)
try:
    io.open(opts.reads2,'r')
except:
    errmsg = "Unreadable or missing read2 files in input."
    errmsg += " This program requires a readable reads file"
    errmsg += " Please see the help with -h or --help"
    parser.error(errmsg)

# Construct the file name from the date and the project name
date = strftime("%d_%B_%Y",localtime())
name = date+"_"+opts.project+"_config.cfg"


# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.

config = ConfigParser.RawConfigParser()

# Software section
config.add_section('Samtools')
config.set('Samtools', 'Location', '/Users/yvans/Home/bin/samtools//samtools')
config.set('Samtools', 'Version', 'Version: 0.1.18 (r982:295)')

config.add_section('Bwa')
config.set('Bwa', 'Location', '/Users/yvans/Home/bin/bwa//bwa')
config.set('Bwa', 'Version', 'Version: 0.5.9-r26-dev')

config.add_section('GATK')
config.set('GATK' , 'location' , '/Users/yvans/Home/GATK/gatk/dist/GenomeAnalysisTK.jar')
config.set('GATK' , 'Version' , 'v1.4-11-g845c0b1')

config.add_section('Picard')
config.set('Picard' , 'Location' , '/Users/yvans/Home/bin/picard/')
config.set('Picard' , 'Version' , 'picard-1.49')

# Files Reference section
config.add_section('DB')
config.set('DB','Location','Where should I put the reference genome?')
config.set('DB','Version','Is a version need? I guess so')

config.add_section('READS1')
config.set('READS1','Location',opts.reads1)
config.set('READS1','Version','')

config.add_section('READS2')
config.set('READS2','Location',opts.reads2)
config.set('READS2','Version','')


# Writing our configuration file to 'experiment_date.cfg'
with open(name, 'wb') as configfile:
    config.write(configfile)