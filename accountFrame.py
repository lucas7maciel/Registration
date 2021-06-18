#Account Frame Widgets
c.accntFr = tk.Frame(c.master, bg=c.color1)



c.accTitle = tk.Label(c.accntFr, bg=c.color1, font=('COURIER', 15, 'bold'), text='')
c.accTitle.pack(pady=(20, 15))


c.accCan1 = tk.Canvas(c.accntFr, bg=c.color2, width=250, height=200, highlightthickness=0)
c.accCan1.pack()

c.altNickBu = tk.Button(c.accCan1, text='Alter Nick', command = c.altNick)
c.altNickBu.grid(row=0, column=0)

c.altNickEn = tk.Entry(c.accCan1)
c.altNickEn.grid(row=1, column=0, padx=10, pady=(0, 15))

c.altPaswBu = tk.Button(c.accCan1, text='Alter Password', command = c.altPasw)
c.altPaswBu.grid(row=0, column=1, pady=15)

c.altPaswEn = tk.Entry(c.accCan1)
c.altPaswEn.grid(row=1, column=1, padx=10, pady=(0, 15))

c.accEnList = [c.altNickEn, c.altPaswEn]


c.accMes = tk.Label(c.accntFr, bg=c.color2, text='Messages')
c.accMes.pack(pady=(0, 5))


c.deleteAcBu = tk.Button(c.accntFr, bg='red', text='Delete account', command = c.delAcc)
c.deleteAcBu.pack(pady=10)


c.backkBu = tk.Button(c.accntFr, text='Back', command = lambda : c.chngFr(c.loginFr, c.accntFr, c.accEnList, c.accMes))
c.backkBu.pack(pady=10)
