import csv

def readCSV(arquivo):
	csvfile = open(arquivo)
	return csv.reader(csvfile, delimiter=',')

def main():
	arquivo_1 = list(readCSV('Arquivo_1.csv'))
	arquivo_2 = list(readCSV('Arquivo_2.csv'))
	print(arquivo_1)
	print(arquivo_2)
	arquivo_1 = [int(x) for x in arquivo_1[0]]
	arquivo_2 = [int(x) for x in arquivo_2[0]]
	print(arquivo_1)
	print(arquivo_2)

main()