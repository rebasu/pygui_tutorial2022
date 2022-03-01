from tkinter import *
from tkinter import ttk, messagebox

import csv

from datetime import datetime

import wikipedia

import webbrowser

from hyperlink import URL


GUI = Tk()
GUI.title('Crypto price calculator')
GUI.geometry('1200x600')

########Tab setting##########
Tab = ttk.Notebook(GUI)
Tab.pack(fill = BOTH, expand = 1)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
# T4 = Frame(Tab)
T5 = Frame(Tab)

icon_tab1 = PhotoImage(file = 'tab1.png')
icon_tab2 = PhotoImage(file = 'tab2.png')
icon_tab3 = PhotoImage(file = 'tab3.png')
# icon_tab4 = PhotoImage(file = 'tab4.png')
icon_tab5 = PhotoImage(file = 'tab4.png')


Tab.add(T1, text = 'Crypto', image = icon_tab1, compound = 'left')
Tab.add(T2, text = 'Wiki Search', image = icon_tab2, compound = 'left')
Tab.add(T3, text = 'Betting', image = icon_tab3, compound = 'left')
# Tab.add(T4, text = 'Point', image = icon_tab4, compound = 'left')
Tab.add(T5, text = 'Point', image = icon_tab5, compound = 'left')


# SHORTCUT - History New Windows

def HistoryWindow(event = None):
    HIS = Toplevel()
    HIS.title('Table')
    HIS.geometry('800x375')

    L = Label(HIS, text = 'Order history', font = FONT1)
    L.pack()
    

    header = ['TS-ID', 'Datetime', 'Title', 'Price', 'Amount', 'Total']
    hwidth = [100, 150, 200, 100, 100, 100]


    table_history = ttk.Treeview(HIS, columns = header, show = 'headings', height = 15)
    table_history.pack()

    for hd,hw in zip(header, hwidth):
        table_history.heading(hd, text = hd)
        table_history.column(hd, width = hw)

    with open('transaction.csv', newline = '', encoding = 'utf-8') as file:
        fr = csv.reader(file)
        for row in fr:
            table_history.insert('', 0, value = row)

    HIS.mainloop()






########zone1-crypto#########

def writetocsv(data, filename = 'data.csv'):
    with open(filename, 'a', newline = '', encoding = 'utf-8') as file:
        fw = csv.writer(file) # fw = filewriter
        fw.writerow(data)


def Year_change(dt):
    eng_year = dt[:4]
    thai_year = str(int(eng_year) + 543)
    thai_dt = thai_year + dt[4:]
    return thai_dt


def Calc(event = None):
    print('Calculation is in process ...')
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    thai_dt = Year_change(dt)
    currency = v_curency.get()
    amount = float(v_amount.get())
    value = float(v_value.get())
    result = amount * value
    print(result)
    data = [thai_dt, currency, amount, result, value]
    writetocsv(data)
    messagebox.showinfo('Result',f'Your currency is {currency}, total price in THB: {result:,.2f}  ({value:,.0f} THB per {currency})')

v_curency = StringVar()
v_amount = StringVar()
v_value = StringVar()

OFFSET = 5

L0 = Label(T1, text = 'Your currency', font = ('THSarabun', 13))
L0.pack(pady = OFFSET)

E0 = ttk.Entry(T1, textvariable = v_curency, width = 12, font = ('impact', 20), justify = 'center')
E0.pack(pady = OFFSET)

E0.focus()


L1 = Label(T1, text = 'Input number of your currency(s)', font = ('THSarabun', 13))
L1.pack(pady = OFFSET)

E1 = ttk.Entry(T1, textvariable = v_amount, width = 12, font = ('impact', 20), justify = 'center')
E1.pack(pady = OFFSET)

L2 = Label(T1, text = 'Input currency value in THB', font = ('THSarabun', 13))
L2.pack(pady = OFFSET)

E2 = ttk.Entry(T1, textvariable = v_value, width = 12, font = ('impact', 20), justify = 'center')
E2.pack(pady = OFFSET)


B1 = ttk.Button(T1, text = 'Calculate', command = Calc)
B1.pack(ipadx = 15, ipady = 5, pady = OFFSET)

E2.bind('<Return>', Calc)


########zone2-wikipedia#########


FONT1 = ('THSarabun', 15)
FONT2 = ('THSarabun', 13)
LANG = 'en'
wikipedia.set_lang(LANG)

v_search = StringVar()
v_result = StringVar()
v_link = StringVar()

def url_call(url):
    webbrowser.open(url)

def Search(event = None):
    try:
        search = v_search.get()
        page = wikipedia.page(search)
        url = page.url
        text = wikipedia.summary(search, sentences = 5)
        print(url)
        v_link.set(url)
        v_result.set(text)
        L.bind("<Button-1>", lambda e: url_call(url))


    except:
        v_link.set('----Link----')
        v_result.set('Data not found, please search again!')



L3 = Label(T2, text = 'Search data from wikipedia', font = FONT1)
L3.pack(pady = OFFSET)
 
E3 = ttk.Entry(T2, textvariable = v_search, font = FONT1)
E3.pack(pady = OFFSET)

B2 = ttk.Button(T2, text = 'Search', image = icon_tab2, compound = 'left', command = Search)
B2.pack(pady = OFFSET)

L = Label(T2, textvariable = v_link, font = FONT2, fg = "blue")
L.pack(pady = OFFSET)


v_result.set('----Result----')
v_link.set('----Link----')
result = Label(T2, textvariable = v_result, wraplength = 550, font = FONT2)
result.pack(pady = OFFSET)


E3.bind('<Return>', Search)



#######Zone3 - Lottery#######

FONT3 = ('THSarabun', 10)
v_total = StringVar()
Bfont = ttk.Style()
Bfont.configure('TButton', font = FONT3)


CF1 = Frame(T3)
CF1.place(x = 50, y = 100)


allmenu = {}

product = {'Lottery':{'name':'Lottery', 'price':30}, 
            'Poker':{'name': 'Poker', 'price': 40},
            'Blackjack': {'name': 'Blackjack', 'price': 50},
            'Slotmania': {'name': 'Slotmania', 'price': 60},
            'Roulette': {'name': 'Roulette', 'price': 75},
            'Hearts': {'name': 'Hearts', 'price': 100}}

def UpdateTable():
    table.delete(*table.get_children())

    total = 0
    for i,m in enumerate(allmenu.values(), start = 1):
        table.insert('', 'end', value = [i, m[0], m[1], m[2], m[3]])
        total += m[3]
        v_total.set(f'Total: {total}')



def ResetTable():
    allmenu.clear()
    table.delete(*table.get_children())
    v_total.set('Total: 0')
    trstamp = datetime.now().strftime('%y%m%d%H%M%S')
    v_transaction.set(trstamp)


def Addmenu(name):
    # name = 'Lottery'
    if name not in allmenu:
        allmenu[name] = [product[name]['name'], product[name]['price'], 1, product[name]['price']]
        
    else:
        quan = allmenu[name][2] + 1
        total = quan * product[name]['price']
        allmenu[name] = [product[name]['name'], product[name]['price'], quan, total]

    print(allmenu)
    UpdateTable()


B = ttk.Button(CF1, text = 'Lottery', image = icon_tab3, compound = 'top', command = lambda m = 'Lottery': Addmenu(m))
B.grid(row = 0, column = 0, ipadx = 20, ipady = 10)


B = ttk.Button(CF1, text = 'Poker', image = icon_tab3, compound = 'top', command = lambda m = 'Poker': Addmenu(m))
B.grid(row = 0, column = 1, ipadx = 20, ipady = 10)


B = ttk.Button(CF1, text = 'Blackjack', image = icon_tab3, compound = 'top',command = lambda m = 'Blackjack': Addmenu(m))
B.grid(row = 0, column = 2, ipadx = 20, ipady = 10)



B = ttk.Button(CF1, text = 'Slotmania', image = icon_tab3, compound = 'top',command = lambda m = 'Slotmania': Addmenu(m))
B.grid(row = 1, column = 0, ipadx = 20, ipady = 10)


B = ttk.Button(CF1, text = 'Roulette', image = icon_tab3, compound = 'top',command = lambda m = 'Roulette': Addmenu(m))
B.grid(row = 1, column = 1, ipadx = 20, ipady = 10)


B = ttk.Button(CF1, text = 'Hearts', image = icon_tab3, compound = 'top',command = lambda m = 'Hearts': Addmenu(m))
B.grid(row = 1, column = 2, ipadx = 20, ipady = 10)


CF2 = Frame(T3)
CF2.place(x = 500, y = 100)

header = ['No.', 'Title', 'Price', 'Amount', 'Total']
hwidth = [50, 200, 100, 100, 100]


table = ttk.Treeview(CF2, columns = header, show = 'headings', height = 15)
table.pack()


for hd,hw in zip(header, hwidth):
    table.heading(hd, text = hd)
    table.column(hd, width = hw)

CF3 = Frame(T3)
CF3.place(x = 500, y = 450)

v_total.set('Total: 0')

LT = Label(CF3, textvariable = v_total, font = FONT1)
LT.pack(pady = OFFSET)


B1 = ttk.Button(CF3, text = 'Reset', command = ResetTable)
B1.pack(pady = OFFSET)

# Transaction ID #

v_transaction = StringVar()

trstamp = datetime.now().strftime('%y%m%d%H%M%S')
v_transaction.set(trstamp)

LTR = Label(T3, textvariable = v_transaction, font = FONT3)
LTR.place(x = 950, y = 75)


# SAVE BUTTON #
FB = Frame(T3)
FB.place(x = 650, y = 493)

def AddTransaction():
    #writetocsv('transaction.csv')
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = v_transaction.get()
    print(transaction, stamp, allmenu.values())

    for m in allmenu.values():
        m.insert(0, transaction)
        m.insert(1, stamp)
        writetocsv(m, 'transaction.csv')

    print(allmenu)
    ResetTable()
    UpdateTotal()

B = ttk.Button(FB, text = 'Save', command = AddTransaction)
B.pack()



#######Zone4 - Member points#######

# CF4 = Frame(T4)
# CF4.place(x = 150, y = 50)

# v_firstname = StringVar()
# v_lastname = StringVar()
# v_price = StringVar()
# v_point = StringVar()
# v_phone = StringVar()

# def UpdateTotal():
#     with open('transaction.csv', newline = '', encoding = 'utf-8') as file:
#         fr = csv.reader(file)
#         price = 0
#         point = 0 # 100 bath per 1 point
#         for row in fr:
#             price += int(row[5])
#         point = price // 100

#         v_price.set('Your current total price: ' + str(price) + ' baht')
#         v_point.set('You will earn: ' + str(point) + ' point(s)')

# def UpdateMember():
#     (firstname, lastname, phone) = (v_firstname.get(), v_lastname.get(), v_phone.get())
#     price = v_price.get()
#     price = price[26:-5]
#     point = v_point.get()
#     point = point[15:-9]
#     print(firstname, lastname, price, point, phone)
#     table_history.insert('', 'end', value = [firstname, lastname, phone, price, point])

#     v_firstname.set('')
#     v_lastname.set('')
#     v_phone.set('')
#     E1.focus()

#     UpdateTotal()


# L = Label(CF4, text = 'Point for betting', font = FONT1)
# L.pack(pady = OFFSET)

# L1 = Label(CF4, text = 'Firstname', font = FONT2)
# L1.pack(pady = OFFSET)

# E1 = ttk.Entry(CF4, textvariable = v_firstname, font = FONT1, justify = 'center')
# E1.pack(pady = OFFSET)
# E1.focus()

# L2 = Label(CF4, text = 'Lastname', font = FONT2)
# L2.pack(pady = OFFSET)

# E2 = ttk.Entry(CF4, textvariable = v_lastname, font = FONT1, justify = 'center')
# E2.pack(pady = OFFSET)


# L3 = Label(CF4, text = 'Phone', font = FONT2)
# L3.pack(pady = OFFSET)

# E3 = ttk.Entry(CF4, textvariable = v_phone, font = FONT1, justify = 'center')
# E3.pack(pady = OFFSET)

# L4 = Label(CF4, textvariable = v_price, font = FONT2)
# L4.pack(pady = OFFSET)

# L5 = Label(CF4, textvariable = v_point, font = FONT2)
# L5.pack(pady = OFFSET)

# UpdateTotal()

# B = ttk.Button(T4, text = 'Order History', command = HistoryWindow)
# B.place(x = 175, y = 400)

# B = ttk.Button(T4, text = 'Save', command = UpdateMember)
# B.place(x = 295, y = 400)

# header = ['Firstname', 'Lastname', 'Phone', 'Total price', 'Point']
# hwidth = [125, 125, 100, 100, 50]


# table_history = ttk.Treeview(T4, columns = header, show = 'headings', height = 15)
# table_history.place(x = 500, y = 75)

# allmember = {}


# for hd,hw in zip(header, hwidth):
#     table_history.heading(hd, text = hd)
#     table_history.column(hd, width = hw)


# GUI.bind('<F1>', HistoryWindow)


########ZONE 5 ###########

def ET(GUI, text, font = FONT1, justify = 'center'):
    v_strvar = StringVar()
    T = Label(GUI, text = text, font = font).pack()
    E = ttk.Entry(GUI, textvariable = v_strvar, font = font)
    return (T, E, v_strvar)


F5 = Frame(T5) #Frame in tab 5 number 1
F5.place(x = 150, y = 125)



v_membercode = StringVar()
v_membercode.set('M-1001')

L = Label(T5, text = 'Memberid: ', font = FONT2).place(x = 185, y = 90)
Lcode = Label(T5, textvariable = v_membercode, font = FONT2).place(x = 280, y = 90)


L, E51, v_fullname = ET(F5, 'fullname')
E51.pack(pady = OFFSET)

L, E52, v_tel = ET(F5, 'telephone')
E52.pack(pady = OFFSET)

L, E53, v_member = ET(F5, 'member')
E53.pack(pady = OFFSET)

L, E54, v_point = ET(F5, 'point')
E54.pack(pady = OFFSET)
v_point.set('0') #Default for initial run

def SetEmptyState():
    v_fullname.set('')
    v_tel.set('')
    v_member.set('')
    v_point.set('0')
    E51.focus()


def SaveMember(event = None):
    code = v_membercode.get()
    fullname = v_fullname.get()
    tel = v_tel.get()
    member = v_member.get()
    point = v_point.get()
    writetocsv([code, fullname, tel, member, point], 'member.csv')
    table_member.insert('', 0, value = [code, fullname, tel, member, point])
    UpdateTable_Member()
    SetEmptyState()


def Editmember():
    code = v_membercode.get()
    allmember[code][1] = v_fullname.get()
    allmember[code][2] = v_tel.get()
    allmember[code][3] = v_member.get()
    allmember[code][4] = v_point.get()
    UpdateCSV(list(allmember.values()), 'member.csv')
    UpdateTable_Member()

    BEdit.state(['disabled']) # Enable edit button
    BSave.state(['!disabled']) # Disable save button

    SetEmptyState()


def NewMember():
    UpdateTable_Member()
    BEdit.state(['disabled']) # Enable edit button
    BSave.state(['!disabled']) # Disable save button
    SetEmptyState()


def Bindstate(event):
    # print(BEdit.state())

    if BEdit.state() == ('disabled',):
        SaveMember()
    else:
        Editmember()


def DeleteAll():
    allmember.clear()
    filename = 'member.csv'
    with open(filename, 'w', newline = '', encoding = 'utf-8') as file:
        fw = csv.writer(file) 
        fw.writerows(allmember)
        UpdateCSV(list(allmember.values()), 'member.csv')
        UpdateTable_Member()

    SetEmptyState()

    BEdit.state(['disabled'])
    BSave.state(['!disabled'])


BNew = ttk.Button(T5, text = 'New', command = NewMember)
BNew.place(x = 120, y = 425)

BEdit = ttk.Button(T5, text = 'Edit', command = Editmember)
BEdit.place(x = 220, y = 425)

BSave = ttk.Button(T5, text = 'Save', command = SaveMember)
BSave.place(x = 320, y = 425)

BDel = ttk.Button(T5, text = 'Delete All', command = DeleteAll)
BDel.place(x = 890, y = 450)

E54.bind('<Return>', Bindstate)


#####TABLE#####

CF5 = Frame(T5)
CF5.place(x = 500, y = 100)

header = ['Code', 'Name', 'Tel', 'Member type', 'Point']
hwidth = [50, 150, 100, 100, 75]


table_member = ttk.Treeview(CF5, columns = header, show = 'headings', height = 15)
table_member.pack()


for hd,hw in zip(header, hwidth):
    table_member.heading(hd, text = hd)
    table_member.column(hd, width = hw)


def UpdateCSV(data, filename = 'member.csv'):
    # data = [[112, 33], [2, 3]]
    with open(filename, 'w', newline = '', encoding = 'utf-8') as file:
        fw = csv.writer(file) # fw = filewriter
        fw.writerows(data) # writerows = replace w/ list

# Delete data in table

def DeleteMember(event):
    select = table_member.selection()
    data = table_member.item(select)['values']
    # print(data)
    del allmember[data[0]]
    UpdateCSV(list(allmember.values()), 'member.csv')
    UpdateTable_Member()

    BEdit.state(['disabled']) # Enable edit button
    BSave.state(['!disabled'])

    SetEmptyState()

table_member.bind('<Delete>', DeleteMember)

#####TABLE#####

#####MEMBER#####

# Update member

def UpdateMemberInfo(event):

    select = table_member.selection()
    code = table_member.item(select)['values'][0]
    print(allmember[code])
    memberinfo = allmember[code]

    v_membercode.set(memberinfo[0])
    v_fullname.set(memberinfo[1])
    v_tel.set(memberinfo[2])
    v_member.set(memberinfo[3])
    v_point.set(memberinfo[4])

    BEdit.state(['!disabled']) # Enable edit button
    BSave.state(['disabled']) # Disable save button

table_member.bind('<Double-1>', UpdateMemberInfo)


last_member = ''
allmember = {}


def UpdateTable_Member():
    global last_member
    with open('member.csv', newline = '', encoding = 'utf-8') as file:
        fr = csv.reader(file)
        table_member.delete(*table_member.get_children())
        for row in fr:
            table_member.insert('', 0, value = row)
            code = row[0] # Query id
            allmember[code] = row
    try:   
        last_member = row[0]
        next_member = int(last_member.split('-')[1]) + 1
        v_membercode.set(f'M-{next_member}')
        # print(allmember)
    except:
        v_membercode.set('M-1001')
    
#####MEMBER#####

BEdit.state(['disabled'])

UpdateTable_Member()

GUI.mainloop()