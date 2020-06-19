import configparser
def readConfigData(section,key):
    cfg = configparser.ConfigParser()
    cfg.read("..//Configfiles//Config.cfg")
    return cfg.get(section,key)

#print(readConfigData("Details","Application_URL"))

#def fetchElementLocators(section,key):
 #   cfg = configparser.ConfigParser
  #  cfg.read("../Configfiles/Element.cfg")
   # return cfg.get(section, key)


#def readConfigData(param, param1):
 #   cfg = configparser.ConfigParser
  #  cfg.read("../Configfiles/Element.cfg")

   # pass


#print(readConfigData("Registration","email_name"))