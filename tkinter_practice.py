from tkinter import *


users={
    "user1":"pass1",
    "user1":"pass2",
}
root = Tk()
root.geometry('1000x1000')
root.title('clarusway login')

logo =  Label(root,text='Welcome to Clarusway',bg='#0052cc',fg='#B284BE')
logo.pack()

user_name =Entry(root,width=50)
user_name.insert(0,'user name')
user_name.pack()

password = Entry(root,show='*',width=50)
password.insert(0,'password')
password.pack()

def submit():
    if user_name.get() not in users.keys():
        Label(root,text='User name is incorrect').pack()
    elif users.get(user_name.get()):
        Label(root,text='incorrect password').pack()
    else:
        Label(root,text='welcome in').pack()

submit_button =Button(root,text='Submit',command=submit)
submit_button.pack()
root.mainloop()