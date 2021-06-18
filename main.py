import tkinter as tk
from commands import Commands

c = Commands()

if c.connected:
	c.master = tk.Tk()
	c.master.title('Cadastros')
	c.master.geometry("450x275")

	exec(open('loginFrame.py').read())
	exec(open('registerFrame.py').read())
	exec(open('accountFrame.py').read())

	c.master.mainloop()

else:
	print('The code will not be able to run as the connection to the database failed')
