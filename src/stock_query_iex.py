#https://iextrading.com/developer/docs/#quote
from stock_query_engine import StockQueryEngine
import json
import urllib2
import os
import util

prefix = 'https://api.iextrading.com/1.0'

class StockQueryIEX(StockQueryEngine):
    def __init__(self):
        pass
    
    def quote(self, symbol):
        url = "%s/stock/%s/chart/5y"%(prefix, symbol)
        return json.load(urllib2.urlopen(url))

if __name__ == '__main__':
    stock_query_iex = StockQueryIEX()
    datadir = '../data/stock/'
    
    import fio
    fio.NewPath(datadir)
    
    symbols = util.GetSymbolList()
    
    for symbol in symbols:
        print symbol
        outfile = os.path.join(datadir, '%s.json'%symbol)
        if fio.IsExist(outfile): continue
        
        raw = stock_query_iex.quote(symbol)
        
        try:
            with open(outfile, "w") as fout:
                json.dump(raw, fout, indent=2, encoding="utf-8")
        except Exception as e:
            print e

    print "Done"