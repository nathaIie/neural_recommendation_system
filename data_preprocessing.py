import csv
data = []
file = open('spotify_data.csv', encoding = 'utf-8')
writeFile = open('prepared_spotify_data.csv', 'a', encoding = 'utf-8')
csvreader = csv.reader(file)
for row in csvreader:
    for element in row:
        if('"' in element):
            row[row.index(element)] = element.replace('"', '')
    if(len(row) > 4):
        replace = ''
        for element in row:
            replace += element + ','
        replace = replace[:-1]
        eachData = replace.split('\n')
        for oneData in eachData:
            data.append(oneData.split(','))
    else:
        data.append(row)
keyDict = {}
userId = 0
rowIndex = 0
for eachRow in data:
    if(rowIndex == 0):
        titleIndex = 0
        for eachElement in eachRow:
            eachElement = eachElement.replace(' ', '')
            if(titleIndex < len(eachRow)-1):
                writeFile.write('\"' + str(eachElement) + '\",')
            else:
                writeFile.write('\"' + str(eachElement) + '\"')
            titleIndex += 1
        rowIndex += 1
        writeFile.write("\n")
    else:
        if(eachRow[0] not in keyDict):
            keyDict[eachRow[0]] = userId
            eachRow[0] = userId
            userId += 1
            index = 0
            for eachElement in eachRow:
                if(index < len(eachRow)-1):
                    writeFile.write('\"' + str(eachElement) + '\",')
                else:
                    writeFile.write('\"' + str(eachElement) + '\"')
                index += 1
            writeFile.write('\n')
        else:
            eachRow[0] = keyDict[eachRow[0]]
            index = 0
            for eachElement in eachRow:
                if(index < len(eachRow)-1):
                    writeFile.write('\"' + str(eachElement) + '\",')
                else:
                    writeFile.write('\"' + str(eachElement) + '\"')
                index += 1
            writeFile.write('\n')
file.close()
writeFile.close()