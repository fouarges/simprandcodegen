#!/bin/python3

import random

print('''
Random Code Generator
=====================
''')

# Characters to use
chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ123456789'

length = input('Code length?')
length = int(length)

nb = input('How many Codes?')
nb = int(nb)

csvData = []

for pwd in range(nb):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  csvData.append(password)
  # Print the passwords
  # print(password)

import csv

with open('codes.csv', 'w') as csvFile:
    writer = csv.writer(csvFile, delimiter=",")
    writer.writerows([c.strip() for c in r.strip(', ').split(',')]
                     for r in csvData)

csvFile.close()
