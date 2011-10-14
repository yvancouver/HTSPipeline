import shlex
import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import ConfigParser

def samtoolsConfig(file):
    config = ConfigParser.ConfigParser()
    try:
        config.readfp(open(file))
    except:
        message = "could not find the config file " + file
        exit(message)

    Version = config.get('Bwa','Version')
    Location = config.get('Bwa','Location')
    return(Version,Location)

def samtoolsVersion():
        p=Popen(['samtools'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        output = p.communicate()
        version = output[0].split("\n")[2]
        return version

def samtoolsLocation():
    return(subprocess.check_output(["which", "samtools"]).strip())

def samtoolsTest():
    """Return the location of samtools
    >>> samtoolsLocation()
    '/Users/yvans/Home/bin/samtools//samtools'
    
    Return the samtools version
    >>> samtoolsVersion()
    'Version: 0.1.18 (r982:295)'
    """
samtools_config=samtoolsConfig('/Users/yvans/Home/workspace/HTSPipeline/config.cfg')
print samtools_config
if __name__ == "__main__":
    import doctest
    doctest.testmod()