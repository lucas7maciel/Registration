#Register Frame Widgets
c.regstFr = tk.Frame(c.master, bg=c.color1)



c.regTitle = tk.Label(c.regstFr, bg=c.color1, font=('COURIER', 15, 'bold'), text='Register')
c.regTitle.pack(pady=20)


c.regCan1 = tk.Canvas(c.regstFr, bg=c.color2, width=250, height=400, highlightthickness=0)
c.regCan1.pack()

c.nickLa = tk.Label(c.regCan1, bg=c.color2, fg='white', text='Nick')
c.nickLa.grid(row=0, column=0)

c.nickEn = tk.Entry(c.regCan1)
c.nickEn.grid(row=0, column=1, pady=5)

c.dateLa = tk.Label(c.regCan1, bg=c.color2, fg='white', text='Birth')
c.dateLa.grid(row=1, column=0)

c.dateEn = tk.Entry(c.regCan1)
c.dateEn.grid(row=1, column=1, pady=5)

c.paswLa = tk.Label(c.regCan1, bg=c.color2, fg='white', text='Password')
c.paswLa.grid(row=2, column=0)

c.paswEn = tk.Entry(c.regCan1, show='*')
c.paswEn.grid(row=2, column=1, pady=5)

c.confLa = tk.Label(c.regCan1, bg=c.color2, fg='white', text='Confirm password')
c.confLa.grid(row=3, column=0, padx=10)

c.confEn = tk.Entry(c.regCan1, show='*')
c.confEn.grid(row=3, column=1, padx=10, pady=5)

c.regEnList = [c.nickEn, c.dateEn, c.paswEn, c.confEn]


c.regMes = tk.Label(c.regstFr, bg=c.color2, fg='white', text='Messages')
c.regMes.pack()


c.regCan2 = tk.Canvas(c.regstFr, bg=c.color1, width=200, height=100, highlightthickness=0)
c.regCan2.pack(pady=20)

c.backBu = tk.Button(c.regCan2, text='Back', command = lambda : c.chngFr(c.loginFr, c.regstFr, c.regEnList, c.regMes))
c.backBu.grid(row=0, column=0, padx=(0, 30))

c.regsBu = tk.Button(c.regCan2, text='Sign Up', command = c.register)
c.regsBu.grid(row=0, column=1)
