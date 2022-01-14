import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except IOError as e:
        print(e)

    return conn


def select_stock(conn, symbol):
    cur = conn.cursor()
    cur.execute("SELECT * FROM stock_data WHERE Symbol=\""+symbol+"\";")
    row = cur.fetchall()

    for r in row:
        s = Stock(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10])


    return s



def lookUpStockInfo(symbol):
    database = r"Stocks.db"
    conn = create_connection(database)
    return select_stock(conn,symbol)


def getTopFive():
    database = r"Stocks.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * from stock_data ORDER BY change DESC LIMIT 5;")
    row = cur.fetchall()

    index=1
    while index<=5:
     for r in row:
         if index==1:
            s1=Stock(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10])
         if index==2:
             s2 = Stock(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10])
         if index==3:
             s3 = Stock(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10])
         if index==4:
             s4 = Stock(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10])
         if index==5:
             s5 = Stock(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10])

         index=index+1

    return topFiveStocks(s1,s2,s3,s4,s5)


class Stock:
    def __init__(self,symbol,name,last,net,change,market,country,ipo,volume,sector,industry):
      self.symbol=symbol;
      self.name=name;
      self.last=last
      self.net=net
      self.change=change
      self.market=market
      self.country=country
      self.ipo=ipo
      self.volume=volume
      self.sector=sector
      self.industry=industry

class topFiveStocks:
    def __init__(self,s1,s2,s3,s4,s5):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5
