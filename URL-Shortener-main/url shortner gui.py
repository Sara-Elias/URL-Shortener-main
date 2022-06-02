import pyshorteners
from tkinter import *

# application window design
root = Tk()
root.geometry('400x420')
root.resizable(False, False)
root.title('URL Shortener')
root.config(bg='#7a536b')


url = StringVar()  # The long URL received by the user
url_short = StringVar()  # The short URL that will be obtained by the application

Label(root, text='URL Shortener', bg='#7a536b', fg='#ded6dc', font='Times 35 bold').place(x=40, y=90)  # Title printing

# This is where the long URL will be inserted
Label(root, text='Enter URL here', bg='#7a536b', fg='#ded6dc', font='Times 15 bold').place(x=50, y=210)
Entry(root, textvariable=url, width=35, font='Times 12').place(x=50, y=240)

# Here the short URL will be printed after a shortcut
Label(root, text='URl Shortener here', bg='#7a536b', fg='#ded6dc',
      font='Times 15 bold').place(x=50, y=320)
text = Entry(root, width=47, textvariable=url_short)
text.place(x=50, y=350)

# This function is responsible for shortening the URL using a directory function
def Convert_fun():
    con_url = pyshorteners.Shortener().tinyurl.short(url.get())
    url_short.set(con_url)

# This is a conversion button which calls the function Convert_fun() Which shortens the URL
Button(root, text='Convert', bg='#fff', fg='#000', font='Times 15 bold', command=Convert_fun).place(x=150, y=280)

# An endless loop of the application window so that the window is on the screen
root.mainloop()
