import shlex
import subprocess
from subprocess import Popen, PIPE, STDOUT
import os

def samtoolsVersion():
        p=Popen(['samtools'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        output = p.communicate()
        version = output[0].split("\n")[2]
        return version

def samtoolsTest():
    """Return the location of samtools
    >>> subprocess.check_output(["which", "samtools"]).strip()
    '/Users/yvans/Home/bin/samtools//samtools'
    
    Return the samtools version
    >>> samtoolsVersion()
    'Version: 0.1.18 (r982:295)'
    """
if __name__ == "__main__":
    import doctest
    doctest.testmod()