import pandas as p
import datetime as dt
import pandas_datareader as dReader
import plotly.graph_objects as gObjects
from tkinter import *
import os
import plotly.io as pio
import PIL.Image
import PIL.ImageTk
import StockLookup as sl
import tkinter.font as tkFont

global label
global photo

def getGraph(stock, year, month, day):

    start = dt.datetime((int)(year), (int)(month), (int)(day))
    end = dt.datetime.now()

    stocks = dReader.DataReader([stock], 'yahoo', start, end)
    stocks_close = p.DataFrame(dReader.DataReader([stock], 'yahoo', start, end)['Close'])

    c_candlestick = gObjects.Figure(data = [gObjects.Candlestick(x = stocks.index,
                                                open = stocks[('Open',    stock)],
                                                high = stocks[('High',    stock)],
                                                low = stocks[('Low',    stock)],
                                                close = stocks[('Close',    stock)])])

    c_candlestick.update_xaxes(
        title_text = 'Date')

    c_candlestick.update_layout(
        title = {
            'text': stock.upper() + ' SHARE PRICE (' + str(year) + '-' + str(dt.datetime.now().year) + ')',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    c_candlestick.update_yaxes(title_text = stock + ' Close Price', tickprefix = '$')

    if not os.path.exists("images"):
        os.mkdir("images")
    pio.write_image(c_candlestick, file="images/stock.png")

def updateImage():
    photo = PIL.ImageTk.PhotoImage(PIL.Image.open("images/stock.png"))
    label.config(image=photo)
    label.image=photo

def takeInput():
    getGraph(EntryTicker.get(), EntryYear.get(), EntryMonth.get(), EntryDay.get())
    addLabels()
    updateImage()

def takeInputT5(val):
    getGraph(val, 2020, 1, 1)
    addLabelsT5(val)
    updateImage()

global labelArr

def addLabelsT5(val):
    sto = sl.lookUpStockInfo(val.upper())

    labelSymbol.text = "Ticker: " + sto.symbol
    labelLast.text = "Last: " + sto.last
    labelNet.text = "Net: " + str(sto.net)
    temp = sto.net
    if float(temp) < 0:
        labelNet.configure(foreground='red')
    elif float(temp) > 0:
        labelNet.configure(foreground='green')
    temp = sto.change
    temp = temp[:-1]
    labelChange.text = "Change: " + str(sto.change)
    if float(temp) < 0:
        labelChange.configure(foreground='red')
    elif float(temp) > 0:
        labelChange.configure(foreground='green')
    labelMarket.text = "Market: " + sto.market
    labelIPO.text = "IPO: " + sto.ipo
    labelVolume.text = "Volume: " + str(sto.volume)
    labelSector.text = "Sector: " + sto.sector
    labelIndustry.text = "Industry: " + sto.industry

    labelSymbol.config(text="Ticker: " + sto.symbol)
    labelLast.config(text="Last: " + sto.last)
    labelNet.config(text="Net: " + str(sto.net))
    labelChange.config(text="Change: " + str(sto.change))
    labelMarket.config(text="Market: " + "{:,}".format(int(str(sto.market)[:-3])))
    labelIPO.config(text="IPO: " + sto.ipo)
    labelVolume.config(text="Volume: " + "{:,}".format(int(str(sto.volume)[:-2])))
    labelSector.config(text="Sector: " + sto.sector)
    labelIndustry.config(text="Industry: " + sto.industry)

    labelIndustry.pack(side=BOTTOM, fill=X)
    labelSector.pack(side=BOTTOM, fill=X)
    labelVolume.pack(side=BOTTOM, fill=X)
    labelIPO.pack(side=BOTTOM, fill=X)
    labelMarket.pack(side=BOTTOM, fill=X)
    labelChange.pack(side=BOTTOM, fill=X)
    labelNet.pack(side=BOTTOM, fill=X)
    labelLast.pack(side=BOTTOM, fill=X)
    labelSymbol.pack(side=BOTTOM, fill=X)

def addLabels():
    sto = sl.lookUpStockInfo(EntryTicker.get().upper())

    labelSymbol.text="Ticker: "+sto.symbol
    labelLast.text="Last: "+sto.last
    labelNet.text="Net: "+str(sto.net)
    temp = sto.net
    if float(temp) < 0:
        labelNet.configure(foreground='red')
    elif float(temp) > 0:
        labelNet.configure(foreground='green')
    temp = sto.change
    temp = temp[:-1]
    labelChange.text="Change: "+str(sto.change)
    if float(temp) < 0:
        labelChange.configure(foreground='red')
    elif float(temp) > 0:
        labelChange.configure(foreground='green')
    labelMarket.text="Market: "+sto.market
    labelIPO.text="IPO: "+sto.ipo
    labelVolume.text="Volume: "+str(sto.volume)
    labelSector.text="Sector: "+sto.sector
    labelIndustry.text="Industry: "+sto.industry

    labelSymbol.config(text="Ticker: "+sto.symbol)
    labelLast.config(text="Last: "+sto.last)
    labelNet.config(text="Net: "+str(sto.net))
    labelChange.config(text="Change: "+str(sto.change))
    labelMarket.config(text="Market: "+"{:,}".format(int(str(sto.market)[:-3])))
    labelIPO.config(text="IPO: "+sto.ipo)
    labelVolume.config(text="Volume: "+"{:,}".format(int(str(sto.volume)[:-2])))
    labelSector.config(text="Sector: "+sto.sector)
    labelIndustry.config(text="Industry: "+sto.industry)

    labelIndustry.pack(side=BOTTOM, fill=X)
    labelSector.pack(side=BOTTOM, fill=X)
    labelVolume.pack(side=BOTTOM, fill=X)
    labelIPO.pack(side=BOTTOM, fill=X)
    labelMarket.pack(side=BOTTOM, fill=X)
    labelChange.pack(side=BOTTOM, fill=X)
    labelNet.pack(side=BOTTOM, fill=X)
    labelLast.pack(side=BOTTOM, fill=X)
    labelSymbol.pack(side=BOTTOM, fill=X)

root = Tk()
root.geometry("1300x800")
root.title("Stock Program")
frame = Frame(root)
frame.pack()

fontStyle = tkFont.Font(family="Lucida Grande", size=15)

LabelStockName = Label(frame, text="Enter stock name:", relief='groove', width=15, font = fontStyle)
LabelStockName.grid(column=1, row=1)
EntryTicker = Entry(frame, width=20, font = fontStyle)
EntryTicker.grid(column=2, row=1)

LabelMDYEAR = Label(frame, text="Enter MM/DD/YEAR:", relief='groove', width=18, font = fontStyle)
LabelMDYEAR.grid(column=4, row=1)

EntryMonth = Entry(frame, width=2, font = fontStyle)
EntryMonth.grid(column=5, row=1)

EntryDay = Entry(frame, width=2, font = fontStyle)
EntryDay.grid(column=6, row=1)

EntryYear = Entry(frame, width=5, font = fontStyle)
EntryYear.grid(column=7, row=1)

button1 = Button(frame, text="Submit", command=takeInput, font = fontStyle)
button1.grid(column=8, row=1)

labelSymbol = Label(root, text='Ticker: ', relief='groove', font = fontStyle)
labelLast = Label(root, text='Last: ', relief='groove', font = fontStyle)
labelNet = Label(root, text='Net: ', relief='groove', font = fontStyle)
labelChange = Label(root, text='Change: ', relief='groove', font = fontStyle)
labelMarket = Label(root, text='Market: ', relief='groove', font = fontStyle)
labelIPO = Label(root, text='IPO: ', relief='groove', font = fontStyle)
labelVolume = Label(root, text='Volume: ', relief='groove', font = fontStyle)
labelSector = Label(root, text='Sector: ', relief='groove', font = fontStyle)
labelIndustry = Label(root, text='Industry: ', relief='groove', font = fontStyle)

labelArr = []
labelArr.append(labelSymbol)
labelArr.append(labelLast)
labelArr.append(labelNet)
labelArr.append(labelChange)
labelArr.append(labelMarket)
labelArr.append(labelIPO)
labelArr.append(labelVolume)
labelArr.append(labelSector)
labelArr.append(labelIndustry)

labelSymbol.pack(side=BOTTOM)
labelLast.pack(side=BOTTOM)
labelNet.pack(side=BOTTOM)
labelChange.pack(side=BOTTOM)
labelMarket.pack(side=BOTTOM)
labelIPO.pack(side=BOTTOM)
labelVolume.pack(side=BOTTOM)
labelSector.pack(side=BOTTOM)
labelIndustry.pack(side=BOTTOM)

labelSymbol.pack_forget()
labelLast.pack_forget()
labelNet.pack_forget()
labelChange.pack_forget()
labelMarket.pack_forget()
labelIPO.pack_forget()
labelVolume.pack_forget()
labelSector.pack_forget()
labelIndustry.pack_forget()


manyStocks = sl.getTopFive()

top5Title = Label(root, text="Top 5 Climbers", font=fontStyle, relief='groove')
top5Title.pack(side=LEFT)
butNum1 = Button(top5Title, text=manyStocks.s5.symbol.upper() + " change: " + manyStocks.s5.change, command= lambda: takeInputT5(manyStocks.s5.symbol.upper() ), font=fontStyle, width=25)
butNum1.pack(side=BOTTOM)
butNum2 = Button(top5Title, text=manyStocks.s4.symbol.upper() + " change: " + manyStocks.s4.change, command= lambda: takeInputT5(manyStocks.s4.symbol.upper() ), font=fontStyle, width=25)
butNum2.pack(side=BOTTOM)
butNum3 = Button(top5Title, text=manyStocks.s3.symbol.upper() + " change: " + manyStocks.s3.change, command= lambda: takeInputT5(manyStocks.s3.symbol.upper() ), font=fontStyle, width=25)
butNum3.pack(side=BOTTOM)
butNum4 = Button(top5Title, text=manyStocks.s2.symbol.upper() + " change: " + manyStocks.s2.change, command= lambda: takeInputT5(manyStocks.s2.symbol.upper() ), font=fontStyle, width=25)
butNum4.pack(side=BOTTOM)
butNum5 = Button(top5Title, text=manyStocks.s1.symbol.upper() + " change: " + manyStocks.s1.change, command= lambda: takeInputT5(manyStocks.s1.symbol.upper() ), font=fontStyle, width=25)
butNum5.pack(side=BOTTOM)
title = Label(top5Title, text="Top 5 Climbers", font=fontStyle, relief='groove', width=20)
title.pack(side=BOTTOM)








photo = PIL.ImageTk.PhotoImage(PIL.Image.open("images/nostock.png"))
label = Label(root, image=photo, relief='groove')
label.pack()

root.mainloop()
