from glob import iglob
import logging
import pandas as pd
from pathlib import Path, PureWindowsPath

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#MAPPING FILE between Pason code and well name
mapping_file = r'C:\Users\Davie\Documents\CRC\1551924558_sample\crc_mapping_file.csv'

data = pd.read_csv(mapping_file)

logging.debug("Sample mapping  '{0}'".format(data.head()))
logging.debug("data column  '{0}'".format(data.loc[data['Well Number'] == 23353520]))

directory = r'C:\Users\Davie\Documents\CRC\1551924558_sample\csv_modification'
new_directory = r'C:\Users\Davie\Documents\CRC\1551924558_sample\csv_modification\new_files/'
file_ending = '**\\*.csv'

files = []

files.extend(iglob(directory + file_ending, recursive=False))

logging.debug('number of files: %s' % len(files))

for i in files:
    name = i.split('\\')[-1]
    name = name.split(".")[0]
    pasonid = name.split("_")[0]
    logging.debug('filename: %s' % pasonid)
    well = data.loc[data['Well Number'] == int(pasonid)]
    logging.debug("well  '{0}'".format(well['Well Name'].item()))

    #open pason data
    e = i

    logging.debug("file  '{0}'".format(e))
    df = pd.read_csv(e)

    df.insert(0, 'api', well['API'].item())
    df.insert(0, 'well_name', well['Well Name'].item())
    df = df.replace(-999.25, '')
    logging.debug("verify insert column  '{0}'".format(df.head()))

    df.to_csv(new_directory + name + '_amended.csv', index=False)