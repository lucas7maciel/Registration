#Login Frame Widgets
c.loginFr = tk.Frame(c.master, bg=c.color1)



c.logTitle = tk.Label(c.loginFr, bg=c.color1, font=('COURIER', 25, 'bold'), text='Enter')
c.logTitle.pack(pady=20)


c.logCan1 = tk.Canvas(c.loginFr, bg=c.color2, width=225, height=200, highlightthickness=0)
c.logCan1.pack()

c.loginLa = tk.Label(c.logCan1, bg=c.color2, fg='white', text='Login')
c.loginLa.grid(row=0, column=0, pady=10)

c.loginEn = tk.Entry(c.logCan1)
c.loginEn.grid(row=0, column=1, padx=10)

c.passwLa = tk.Label(c.logCan1, bg=c.color2, fg='white', text='Password')
c.passwLa.grid(row=1, column=0, pady=10)

c.passwEn = tk.Entry(c.logCan1, show='*')
c.passwEn.grid(row=1, column=1, padx=10)

c.logEnList = [c.loginEn, c.passwEn]


c.logMes = tk.Label(c.loginFr, bg=c.color2, fg='white', text='Welcome!')
c.logMes.pack()


c.logCan2 = tk.Canvas(c.loginFr, bg=c.color1, width=200, height=100, highlightthickness=0)
c.logCan2.pack(pady=(25, 20))

c.enterBu = tk.Button(c.logCan2, text='Enter', command = c.enter)
c.enterBu.grid(row=0, column=0, padx=20)

c.regisBu = tk.Button(c.logCan2, text='Sign Up', command = lambda : c.chngFr(c.regstFr, c.loginFr, c.logEnList, c.logMes))
c.regisBu.grid(row=0, column=1, padx=20)


c.loginFr.pack(fill='both', expand=1)
