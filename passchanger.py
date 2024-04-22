import csv

header = ['name','url','username','password','note','totp','vault']

data = []

file = open("kaspersky.txt", "r")

currentData = {}
for line in file:
  if line.startswith('---'):
    data.append(currentData)
    currentData = {}
  if line.startswith('Website name: '):
    currentData["name"] = line[len('Website name: '):].replace("\n", "")
  if line.startswith('Application: '):
    currentData["name"] = line[len('Application: '):].replace("\n", "")
  if (line.startswith('Website URL: ')):
    currentData["url"] = line[len('Website URL: '):].replace("\n", "")
  if (line.startswith('Login: ')):
    currentData["username"] = line[len('Login: '):].replace("\n", "")
  if (line.startswith('Password: ')):
    currentData["password"] = line[len('Password: '):].replace("\n", "")
  if (line.startswith('Comment: ')):
    currentData["note"] = line[len('Comment: '):].replace("\n", "")

data.append(currentData)

with open('generic-proton.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
