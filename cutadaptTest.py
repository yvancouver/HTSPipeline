import subprocess
import ConfigParser
import doctest
import configReader


def cutadaptVersion():
    r"""Return the cutadapt version Need to comment better NOW
    >>> configReader.Config(file,section)[0] == subprocess.check_output(["cutadapt", "--version"]).strip()
    True
    """

def cutadaptLocation():
    r"""Test the location of cutadapt
    >>> cutadaptloc = configReader.Config(file,section)[1]; cutadaptloc == subprocess.check_output(["which", "cutadapt"]).strip()
    True
    """

section = 'cutadapt'
file = '/Users/yvans/Home/workspace/HTSPipeline/config.cfg'

if __name__ == "__main__":
    doctest.testmod()