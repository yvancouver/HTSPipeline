import ConfigParser

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
