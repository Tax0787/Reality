try: from Tkinter import *
except: from tkinter import *
win = Tk()
win.title('Reality - Game')
win.iconbitmap('C:\Windows\System32')
win.geometry('400x200+100+100')
from os import startfile as s
fungtion_0 = lambda : s('R프롤로그')
fungtion_1 = lambda : s('R1화')
fungtion_2 = lambda : s('R2화')
fungtion_3 = lambda : s('R3화')
fungtion_4 = lambda : s('R4화')
fungtion_5 = lambda : s('R5화')
fungtion_6 = lambda : s('R6화')
fungtion_7 = lambda : s('R7화')
fungtion_8 = lambda : s('R8화')
fungtion_9 = lambda : s('R에필로그')

btn_0 = Button(win, text = '프롤로그', command = fungtion_0)
btn_0.pack()
btn_1 = Button(win, text = '1화', command = fungtion_1)
btn_1.pack()
btn_2 = Button(win, text = '2화', command = fungtion_2)
btn_2.pack()
btn_3 = Button(win, text = '3화', command = fungtion_3)
btn_3.pack()
btn_4 = Button(win, text = '4화', command = fungtion_4)
btn_4.pack()
btn_5 = Button(win, text = '5화', command = fungtion_5)
btn_5.pack()
btn_6 = Button(win, text = '6화', command = fungtion_6)
btn_6.pack()
btn_7 = Button(win, text = '7화', command = fungtion_7)
btn_7.pack()
btn_8 = Button(win, text = '8화', command = fungtion_8)
btn_8.pack()
btn_9 = Button(win, text = '에필로그', command = fungtion_9)
btn_9.pack()

win.mainloop()