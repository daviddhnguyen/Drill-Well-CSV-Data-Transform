from glob import iglob
import logging
import csv
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


directory = r'\\calnet.ads\data\BDA\Data_Engineering\Pason\unzipped'
file_ending = '**\\*.csv'

files = []

files.extend(iglob(directory + file_ending, recursive=False))

logging.debug('number of files: %s' % len(files))

with open(r'\\calnet.ads\data\BDA\Data_Engineering\Pason\unzipped\csv_headers.csv', 'w', newline = '') as g:
    for i in files:
        with open(i, 'rt') as f:
            reader = csv.reader(f)
            n = next(reader)
            logging.debug('header: %s' % n)

            writer = csv.writer(g)
            writer.writerow(n)

# unique_headers = set()
#
#
# with open(r"\\calnet.ads\data\BDA\Data_Engineering\Pason\unzipped\2093_1sec.csv", 'rt') as f:
#     reader = csv.reader(f)
#     i = next(reader)
#
#     print(i)