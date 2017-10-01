from tqdm import tqdm
import csv

areas = []

with open('hae_pats.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print row[2]

