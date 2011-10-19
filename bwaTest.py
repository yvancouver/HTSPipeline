import shlex
import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import ConfigParser
import doctest

def Config(file,section):
    config = ConfigParser.ConfigParser()
    try:
        config.readfp(open(file))
    except:
        message = "could not find the config file " + file
        exit(message)

    Version = config.get(section,'Version')
    Location = config.get(section,'Location')
    return(Version,Location)

def bwaVersion():
    r"""Return the samtools version
    >>> p=Popen(['bwa'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    >>> output = p.communicate()
    >>> version = output[0].split('\n')[2]
    >>> print version
    Version: 0.5.9-r16
    """

def bwaLocation():
    r"""Test the location of bwa
    >>> subprocess.check_output(["which", "bwa"]).strip()
    '/Users/yvans/Home/bin/bwa//bwa'
    """
config_samtools=Config('/Users/yvans/Home/workspace/HTSPipeline/config.cfg','Bwa')

#output = doctest.testmod()
#print "Bwa:\n",output
