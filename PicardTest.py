import doctest
import subprocess
import os
import configReader

def PicardVersion():
    r'''Test Picard Version
    >>> os.path.exists(configReader.Config(file,section)[1]+configReader.Config(file,section)[0]);
    True
    '''
def GATKLocation():
    r'''Test GATK location
    >>> os.path.exists(configReader.Config(file,section)[1])
    True
    '''

section = 'Picard'
file = '/Users/yvans/Home/workspace/HTSPipeline/config.cfg'

if __name__ == '__main__':
    doctest.testmod()