import tkinter
from tkinter import messagebox
def Logged_msg():
    username='keowe6'
    password ='!@!@Keka2009'

    if usernme_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title='Login Success', message='You have successfully logged in')
    else:
        messagebox.showerror(title='Login Failure', message='Invalid Username And Password')

home = tkinter.Tk()
home.title('Form')
home.geometry('400x600')
home.configure(bg='#000')

frame = tkinter.Frame(bg='#000')


# widgets creation
signup_lab = tkinter.Label(frame, text='Sign Up', bg='#000', fg='skyblue', font=('Times New Romans', 24))
usernme_lab = tkinter.Label(frame, text='Username', bg='#000', fg='antiquewhite', font=('Times New Romans', 12))
usernme_entry = tkinter.Entry(frame, font=('Times New Romans', 12))
password_entry = tkinter.Entry(frame, show='*', font=('Times New Romans', 12))
password_lab = tkinter.Label(frame, text='Paassword', bg='#000', fg='antiquewhite', font=('Times New Romans', 12))
signup_buttn = tkinter.Button(frame, text='LOGIN', bg='#060', fg='antiquewhite', font=('Times New Romans', 12), command=Logged_msg)

#widgets placing
signup_lab.grid(row=1, column=1, columnspan=2, sticky='news', pady=20)
usernme_lab.grid(row=2, column=1, pady=20)
usernme_entry.grid(row=2, column=2)
password_lab.grid(row=3, column=1)
password_entry.grid(row=3, column=2)
signup_buttn.grid(row=4, column=1, pady=20)

frame.pack()
home.mainloop()