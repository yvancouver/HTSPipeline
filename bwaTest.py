#import shlex
import subprocess
from subprocess import Popen, PIPE, STDOUT
#import os
import ConfigParser
import doctest
import configReader


def bwaVersion():
    r"""Return the bwa version Need to comment better NOW
    >>> p=Popen(['bwa'], stdout=PIPE, stdin=PIPE, stderr=STDOUT); output = p.communicate(); bwaVer = configReader.Config(file,section)[0]; bwaVer == output[0].split('\n')[2]
    True
    """

def bwaLocation():
    r"""Test the location of bwa
    >>> bwaloc = configReader.Config(file,section)[1]; bwaloc == subprocess.check_output(["which", "bwa"]).strip()
    True
    """

section = 'Bwa'
file = '/Users/yvans/Home/workspace/HTSPipeline/config.cfg'

if __name__ == "__main__":
    doctest.testmod()