import csv
import os
import fio

datadir = '../data/'

def getSymbolsFromCSV():
    symbols = []
    
    for inputname in ['NASDAQ.csv', 'NYSE.csv', 'AMEX.csv']:
        inputfile = os.path.join(datadir, inputname)
        with open(inputfile, 'rb') as csvfile:
            csv_read = csv.reader(csvfile, delimiter=',', quotechar='"')
            head = True
            for row in csv_read:
                if head:
                    head = False
                    continue
                
                symbols.append(
                    {
                        "Symbol":row[0].strip().rstrip(),
                        "Name":row[1],
                        "LastSale":row[2],
                        "MarketCap":row[3],
                        "IPOyear":row[4],
                        "Sector":row[5],
                        "industry":row[6],
                        "Summary Quote":row[7],
                    }
                )
    
    fio.SaveDict2Json(symbols, os.path.join(datadir, 'symbols.json'))

def GetSymbolList():
    symbolraw = fio.LoadDictJson(os.path.join(datadir, 'symbols.json'))

    return [symbol['Symbol'] for symbol in symbolraw]

if __name__ == '__main__':
    getSymbolsFromCSV()
    print GetSymbolList()