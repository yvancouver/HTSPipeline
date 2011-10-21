import doctest
import subprocess
import os
import configReader

def GATKVersion():
    r'''Test GATK Version
    >>> version = subprocess.check_output(["java", "-jar" , "/Users/yvans/Home/bin/GenomeAnalysisTK-latest/GenomeAnalysisTK.jar", " --help"]); configReader.Config(file,section)[0] == version.split("\n")[1].split(",")[0]
    True
    '''
def GATKLocation():
    r'''Test GATK location
    >>> os.path.exists(configReader.Config(file,section)[1])
    True
    '''
    pass

def GATKalias():
    r'''Test if GATK as been aliased. NOT SURE IF WE SHOULD USE ALIAS
    '''

section = 'GATK'
file = '/Users/yvans/Home/workspace/HTSPipeline/config.cfg'

if __name__ == '__main__':
    doctest.testmod()