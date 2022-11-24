import csv

file = open("TitanicSurvival.csv","r")
data = list(csv.reader(file,delimiter=","))
file.close()

name_input=str(input('Name: '))
for element in data:
	tmp = element
	if tmp[0] == name_input:
		print (tmp)
		break
	


#temp = data[-1]
#temp[4] = '1st'
#data[-1] = temp


for element in data:
	tmp = element
	tmp[4] = '1st'
	element = tmp
		
#print(data)

