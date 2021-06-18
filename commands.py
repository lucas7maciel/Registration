import datetime, tkinter as tk


class Commands:
	exec(open('database.py').read())

	color1 = '#BFBFBF'
	color2 = '#8C8C8C'

	checkLogin = 'SELECT Nick FROM Data WHERE Nick = %s AND Pasw = %s'
	checkAcnts = 'SELECT Nick FROM Data WHERE Nick = %s'

	regCom = 'INSERT INTO Data (Nick, Pasw, Birth) VALUES (%s, %s, %s)'
	upNick = 'UPDATE Data SET Nick = %s WHERE Nick = %s'
	upPasw = 'UPDATE Data SET Pasw = %s WHERE Nick = %s'
	upDate = 'UPDATE Data SET Birth = %s WHERE Nick = %s'
	delCom = 'DELETE FROM Data WHERE Nick = %s'

	def chngFr(self, frame1, frame2, entryL, mesLabel):
		for entry in entryL:
			entry.delete(0, 'end')

		mesLabel.config(text='Messages')

		frame1.pack(fill='both', expand=1)
		frame2.forget()

	def enter(self):
		login = self.loginEn.get()
		password = self.passwEn.get()
		data = (login, password, )

		self.cursor.execute(self.checkLogin, data)
		self.acc = self.cursor.fetchone()

		if self.acc == None:
			self.logMes.config(text='Incorrect user or password')
			return

		self.accTitle.config(text=self.acc[0])
		self.chngFr(self.accntFr, self.loginFr, self.logEnList, self.logMes)

	def register(self):
		nick = self.nickEn.get()
		date = self.dateEn.get().replace("/", "-")
		pasw = self.paswEn.get()
		cpasw = self.confEn.get()
		data = (nick, pasw, date)

		Error = True

		#Check if the chosen nick already exists
		self.cursor.execute(self.checkAcnts, (nick,))

		if self.cursor.fetchone() != None:
			self.regMes.config(text='This nick already exists')

		elif len(nick) <= 2 or len(nick) > 10:
			self.regMes.config(text='Nick between 3 and 10 characters')

		elif len(date) != 10 or date[4] != '-' or date[7] != '-':
			self.regMes.config(text='Invalid date (must be yyyy/mm/dd)')

		elif not self.checkDate(date):
			self.regMes.config(text='Invalid date')

		elif len(pasw) <= 2 or len(pasw) > 10:
			self.regMes.config(text='Password between 3 and 10 characters')

		elif pasw != cpasw:
			self.regMes.config(text='Passwords are different')

		else: Error = False


		if Error:
			return

		try:
			self.cursor.execute(self.regCom, data)
			self.db.commit()

			self.regMes.config(text='Registered!')

		except:
			self.regMes.config(text='Record could not be done')

	def checkDate(self, date):
		date = date.split('-')

		try:
			datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
			return True

		except ValueError:
			return False

	def altNick(self):
		nick = self.acc[0]
		newNick = self.altNickEn.get()
		data = (newNick, nick)

		self.cursor.execute(self.checkAcnts, (newNick,))
		if self.cursor.fetchone() != None:
			self.accMes.config(text='This nick already exists')
			return
		
		elif len(newNick) < 3 or len(newNick) > 10:
			self.accMes.config(text='Between 3 or 10 characters')
			return

		try:
			self.acc = (newNick,)
			self.accTitle.config(text=self.acc[0])
			self.cursor.execute(self.upNick, data)
			self.db.commit()

			self.accMes.config(text='Nick successfully changed')

		except:
			self.accMes.config(text='Nick could not be changed')

	def altPasw(self):
		pasw = self.altPaswEn.get()
		nick = self.acc[0]
		data = (pasw, nick, )

		if len(pasw) < 3 or len(pasw) > 10:
			self.accMes.config(text='Password between 3 and 10 characters')
			return

		try:
			self.cursor.execute(self.upPasw, data)
			self.db.commit()

			self.accMes.config(text='Password successfully changed')

		except:
			self.accMes.config(text='Password could not be changed')

	def delAcc(self):
		self.cursor.execute(self.delCom, self.acc)
		self.db.commit()

		self.chngFr(self.loginFr, self.accntFr, self.accEnList, self.accMes)

		self.logMes.config(text='Account deleted')

