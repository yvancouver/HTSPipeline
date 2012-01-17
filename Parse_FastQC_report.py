# Yvan Strahm 2011
#

"""Parsing the FastQC report to extract info
Not sure if the report will be read directly form its file system location
or if it will be passed as an argument.
"""
__author__ = "Yvan Strahm (yvan.strahm@gmail.com)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date:  $"
__copyright__ = "Copyright (c) 2011 Yvan Strahm"
__license__ = "Python"

import doctest
import subprocess
import os
import configReader

class Report:
    def __init__(self):
          self.exist = "yes"
      
    def read_header():
        pass
    
    def read_Per_base_sequence_quality_pass():
        pass
    
    def read_Per_sequence_quality_scores():  
        pass
    
    def read_Per_base_sequence_content():
        pass
    
    def read_Per_base_GC_content():
        pass
    
    def read_Per_sequence_GC_content():
        pass
    
    def read_Per_base_N_content():
        pass
    
    def read_Sequence_Length_Distribution():
        pass
    
    def read_Overrepresented_sequences():
        pass
    
    def read_Kmer_Content():
        pass
    

if __name__ == "__main__":
    doctest.testmod()

 