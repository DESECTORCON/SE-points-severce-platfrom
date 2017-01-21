import time, datetime, csv, os, json

ITEMSFORTXT = open('items.txt', 'r')
ITEMSFORPRO = open('itemsForPro.json', 'r')
#os.chdir('/SE_point_severce/')

for file in os.listdir('./'):

    if file.endswith('.csv'):
        fileA = str(file)
        fileA = open(str(file), 'r')