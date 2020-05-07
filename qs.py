__author__ = "Florian Thiery"
__copyright__ = "MIT Licence 2019, Reseqrch Squirrel Engineers, Florian Thiery"
__credits__ = ["Florian Thiery"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Florian Thiery"
__email__ = "rse@fthiery.de"
__status__ = "draft"

# import dependencies
import uuid
import pandas as pd
import os
import codecs
import datetime

# set paths
dir_path = os.path.dirname(os.path.realpath(__file__))
file_in = dir_path + "\\" + "lkpop.csv"
file_out = dir_path + "\\" + "lkpop.txt"

# read csv file
data = pd.read_csv(
    file_in, # relative python path to subdirectory
    encoding='utf-8',
    sep='\t', # deliminiter
    quotechar="'",  # single quote allowed as quote character
    usecols=['insgesamt','m','w','RS','item','label','wd'], # only load the  columns specified
    skiprows=0, # skip X rows of the file
    na_values=['.', '??'] # take any '.' or '??' values as NA
)

# create triples from dataframe
outStr = ""
lines = []
for index, row in data.iterrows():
    lines.append(str(row['wd']).replace("http://www.wikidata.org/entity/","")+"	P1082	"+str(row['insgesamt'])+"	P585	+2019-10-31T00:00:00Z/11	P459	Q52679562	S854	\"https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.html\"")
    lines.append(str(row['wd']).replace("http://www.wikidata.org/entity/","")+"	P1540	"+str(row['m'])+"	P585	+2019-10-31T00:00:00Z/11	P459	Q52679562	S854	\"https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.html\"")
    lines.append(str(row['wd']).replace("http://www.wikidata.org/entity/","")+"	P1539	"+str(row['w'])+"	P585	+2019-10-31T00:00:00Z/11	P459	Q52679562	S854	\"https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.html\"")

# write output file
file = codecs.open(file_out, "w", "utf-8")
for line in lines:
    file.write(line)
    file.write("\r\n")
file.close()
