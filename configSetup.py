import ConfigParser

config = ConfigParser.RawConfigParser()

# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.

config.add_section('Samtools')
config.set('Samtools', 'Location', '/Users/yvans/Home/bin/samtools//samtools')
config.set('Samtools', 'Version', 'Version: 0.1.18 (r982:295)')

config.add_section('Bwa')
config.set('Bwa', 'Location', '/Users/yvans/Home/bin/bwa//bwa')
config.set('Bwa', 'Version', 'Version: 0.5.9-r16')

config.add_section('GATK')
config.set('GATK' , 'location' , '/Users/yvans/Home/bin/GenomeAnalysisTK-latest/GenomeAnalysisTK.jar')
config.set('GATK' , 'Version' , '')

# Writing our configuration file to 'example.cfg'
with open('config.cfg', 'wb') as configfile:
    config.write(configfile)