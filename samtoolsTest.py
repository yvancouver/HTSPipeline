#import shlex
import subprocess
from subprocess import Popen, PIPE, STDOUT
#import os
import ConfigParser
import doctest
import configReader


def samtoolsVersion():
    r"""Return the samtools version
    >>> p=Popen(['samtools'], stdout=PIPE, stdin=PIPE, stderr=STDOUT); output = p.communicate(); samtoolsVer = configReader.Config(file,section)[0]; samtoolsVer == output[0].split('\n')[2]
    True
    """
def samtoolsLocation():
    r"""Return the location of samtools
    >>> samtoolsLoc = configReader.Config(file,section)[1]; samtoolsLoc == subprocess.check_output(["which", "samtools"]).strip()
    True
    """

section = 'Samtools'
file = '/Users/yvans/Home/workspace/HTSPipeline/config.cfg'
if __name__ == "__main__":
    doctest.testmod()
