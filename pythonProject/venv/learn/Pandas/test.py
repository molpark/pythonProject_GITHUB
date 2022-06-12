import sys
from tkinter import Button,mainloop

x=Button(text='Press me',command=(lambda :sys.stdout.write('Hello,World\n')))
x.pack()
x.mainloop()

