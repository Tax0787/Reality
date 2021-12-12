class AOCtoAOO:
    def __init__(self,file_input):
        with open(file_input + '.AOC','r', encoding = 'utf-8') as f:
            lines = f.readlines()
            title = lines[0]
            icon = lines[1]
            option = eval(lines[2])
            file_output = lines[3]
        self.output(title,icon,option,file_output)
    def output(self,title,icon,option,file_output):
        print()
        with open(file_output + '.py','w', encoding = 'utf-8') as f:
            f.write('''try: from Tkinter import *
except: from tkinter import *
win = Tk()
win.title('{}')
win.iconbitmap('{}')
win.geometry('400x200+100+100')
from os import startfile as s
{}
{}
win.mainloop()'''.format(title[:len(title) -1],icon[:len(icon) -1],self.fungtions(option),self.buttons(option)))
    def buttons(self,option):
        sose = ''
        parts = '''btn_{} = Button(win, text = '{}', command = fungtion_{})
btn_{}.pack()
'''
        nom = 0
        for name in option.keys():
            str_nom = str(nom)
            sose += parts.format(str_nom,name,str_nom,str_nom)
            nom += 1
        return sose
    def fungtions(self,option):
        sose = ''
        parts = 'fungtion_{} = lambda : s(\'{}\')\n'
        nom = 0
        for fungtion in option.values():
            str_nom = str(nom)
            sose += parts.format(str_nom,fungtion)
            nom += 1
        return sose