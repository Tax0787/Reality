import sys
def 카운트_다운(nom = 'input(\'>>> \')'):
    from time import sleep as s
    while True:
        a = eval(nom)
        if a == 'br' : return
        for i in reversed(range(int(a))):
            if new_line_bool: print(i)
            s(1)
class Input:
    def __init__(self, strs,  GUI_Bool =False, anser = 'none' , Object = 'none', txt = 'none', time = 0.0625, str_option = '', seps = ' ', files_NOGUI =  sys.stdout, flush = False, new_line_bool_NOGUI = False):
        self.strs = strs
        self.Object = Object
        self.anser= anser
        if not GUI_Bool:
            self.Object = Print(strs, GUI_Bool =GUI_Bool, time = time, str_option = str_option, seps = seps, files_NOGUI = files_NOGUI, flush = flush, new_line_bool_NOGUI = new_line_bool_NOGUI)
            self.anser = input('')
        else:
            self.input2()

    def ipd(self):
        self.anser = self.txt.get()

    def input2(self):
        from TaxPak.tks import Tks as T
        root = T(name = 'win', sose = 'win.title(\'Tks\')\nwin.geometry(\'400x200+100+100\')')
        exec(root.sose(root.wiget('lbl', 'Label',' , text=self.strs') + '\n' + root.wiget('self.txt', 'Entry','') + '\n' + root.wiget('btn', 'Button',', text="OK", width=15, command = self.ipd')))

class Print:
    def __init__(self, strs,  GUI_Bool =False, time = 0.0625, str_option = '', seps = ' ', files_NOGUI =  sys.stdout, flush = False, new_line_bool_NOGUI = True, str1 = 'window'): #add_printx_1 = False,files =  'self.ClassA', new_line_bool = False 가 원래 더 있었음
        if GUI_Bool: self.printx_2(strs, str1 = str1) #add_printx_1 = add_printx_1, time = time, str_option = str_option, seps = seps, files = files, new_line_bool = new_line_bool 가 원래 더 있었음
        else: self.printx_1(strs, time = time, str_option = str_option, seps = seps, files =  files_NOGUI , flush = flush, new_line_bool = new_line_bool_NOGUI)
    def printx_1(self, strs,time = 0.0625, str_option = '', seps = ' ', files =  sys.stdout, flush = False, new_line_bool = True):
        from time import sleep as s
        for i in strs:
            for j in i:
                print(j , end = str_option, sep = seps, file = files, flush = False)
                s(time)
        if new_line_bool: print()
                
    class printx_2:
        class ClassA:
            def wirte(strs):
                pass
        
        def __init__(self, str2, str1 = 'window' ): # add_printx_1 = False, time = 0.0625, str_option = '', seps = ' ', files =  'self.ClassA', new_line_bool = False 가 원래 더 있었음
            try: import Tkinter as tk
            except: import tkinter as tk
            prints = tk.Tk()
            prints.title(str1)
            prints.geometry('400x200+100+100')
            self.txt = str2 #원래 self.txt = '' 임
            lb = tk.Label(prints, text = self.txt)
            lb.pack() #10122이인환
            prints.mainloop() #추가됨 (옮겨짐)
            '''
            #10122이인환
            (내 학번과 이름) 이 쓰인곳이 / 전 소스

            여기부터
            
            if add_printx_1: printx_2_1(str2, time = time, str_option = str_option, seps = seps, files =  eval(files), new_line_bool = new_line_bool)
            else: self.txt = str2
            prints.mainloop()
        
        def change_text(self,text, fs = 'self.ClassA'):
            f = eval(fs)
            for index, value in enumerate(my_list):
                self.text.set(text)
                f.write(strs)

        def trans(strt, inputs = ' ', outputs = ' '):
            my_list = list(strt)
            for index, value in enumerate(my_list):
                    if value == inputs:
                            my_list[index] = outputs
            return "".join(my_list)
        
        def printx_2_1(self, strs,time = 0.0625, str_option = '', seps = ' ', files =  'self.ClassA', new_line_bool = False):
            f = eval(files)
            from time import sleep as s
            for i in range(strs):
                self.change_text(self.trans(strs[:i], output = seps), f = f)
                s(time)
                if new_line_bool: self.change_text(self.text + '\n')

                여기까지 이 소스들은 오류가 나서 포기한다'''

    def Br():
        print('테스트용')

until = lambda bool, sose : 'while not {}:\n{}'.format(bool,sose)

repeat = lambda nom, sose : 'for i in range({}):\n{}'.format(nom, sose)

def main():
    print('\'\'\'먼저 Print와 untile\'\'\'')
    s = input('>>>')
    exec(until('s ==\'Br\'', '''
    print('until (입력값) == \\'Br\\'')
    a = Print(eval(s))
    s = input('>>>')'''))
    a = Print('#자, 이제 테스트가 잘 됬다면, 이 문장이 출력 될 것이고 이제부터는 이 Print 로 간다, 먼저 a 라는 오브젝트(Print의)를 태스트 할것이다')
    exec(until('s == \'br\'', '''
    exec('a' + s)
    s = input('>>>')'''))
    a = Print('#오호 이것도 통과다, 자, 이제 테스트가 잘 됬다면, 이 문장이 출력 될 것이고 다시 이 Print 로 간다')
    a.printx_1('이제 입력값만큼 개소리를 출력할 것이다, repeat 함수 와 Input 함수 태스트이다')
    b = Input('>>>')
    c = str(b.anser)
    repeat(c, '''
    Print('멍멍, 뀨~, 아르르르르르?, 멍멍~, 핵핵,,,,, 멍~!')''')
    b = Input('다시 메인함수를 호출하시려면 불 데이터를 입력해주세요')
    c = eval(b.anser)
    if c: main()

#if __name__ == '__main__': main()
