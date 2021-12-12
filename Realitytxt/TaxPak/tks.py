from TaxPak.tks_option import debug
from TaxPak.TaxModle import Print as P
from TaxPak.TaxModle import Input as I
import sys
def IDP(strs,  GUI_Bool =False, time = 0.0625, str_option = '', seps = ' ', files_NOGUI =  sys.stdout, flush = False, new_line_bool_NOGUI = True, str1 = 'window', dibug = False):
    global debug
    if debug: P(strs,  GUI_Bool =GUI_Bool, time = time, str_option = str_option, seps = seps, files_NOGUI =  files_NOGUI, flush = flush, new_line_bool_NOGUI = new_line_bool_NOGUI, str1 = str1, dibug = dibug)
IDP('prints로 쓰기 시도')
IDP('prints 정의 성공, 그래서 지금 prints로 씀')
IDP('prints로 쓰기 성공')
IDP('helper 정의 시작')
def helper():
    IDP('helper 호출 성공')
    IDP('오류 해결 도우미 물음')
    abcde = I("오류 해결 도우미를 키시겠습니까?(응 or 아니): >>> ")
    if abcde == "응":
        IDP('Y')
        IDP('질문 횟수 I()')
        abcd = I("몇번 물어보시겠습니까?(숫자만): >>> ")
        for i in range(1, int(abcd) + 1):
            IDP('도움말 질문')
            abcdef = I( str(i) + "번째 도움말은 무었입니까?: >>> ")
            IDP('도움말 출력')
            P("다음을 열린 웹사이트에서 변역하세요! , 도움말 : " + str(help(abcdef)))
            import webbrowser
            IDP('파파고 오픈')
            webbrowser.open("https://papago.naver.com")
            IDP('종료')
        prints("./종료합니다./")
    else:
        prints("./종료합니다./")
IDP('prints로 format 포함으로 쓰기 시도 ( 하하와, 하하가 쓰였는지 알기 ) ')
IDP('하하 를 쓰기 : {}, 성공? : {}'.format('하하',str('하하' == '하하')))
IDP('prints로 format 포함으로 쓰기 성공 ( 하하와, 하하가 쓰였는지 알기 ) ')
IDP('Tks 정의 시작')
class Tks: #Tkinter - upgrade Korean middle school club tax0787 Service
    IDP('__init__ 정의 시작')
    def __init__(self,add_script_string = '',**option):
        IDP('Tks 호출 완료 option과 add_script_string를 self 속에 넣는다')
        self.option = option
        self.add_script_string = add_script_string
    IDP('__init__ 정의 완료')
    IDP('add_script 정의 시작')
    def add_script(self, passward):
        IDP('add_script 호출 완료, 비밀번호를 넣을 strs 정의')
        strs = ''
        for i in [0xc774,0xac83,0xc744,0x20,0xc54c,0xc544,0xb0bc,0x20,0xc2e4,0xb825,0xc774,0x20,0xc788,0xc73c,0xba74,0x20,0xbe44,0xbc88,0xc744,0x20,0xc368,0xb3c4,0x20,0xb428]:
            strs += chr(i)
        IDP('strs에 비밀번호다 집어넣음')
        IDP('실행')
        if passward == strs: exec(self.add_script_string)
    IDP('add_script 정의 완료')
    IDP('wiget 정의 시작')
    def wiget(self,name,command,option, add = ''):
        IDP('객체 대이터를 objects 로 지정 성공')
        objects = self.option
        IDP('객체 대이터를 objects 로 지정 성공')
        IDP('return "{} = {}({}{})\\n{}.pack()\\n{}".format(name,command,objects[\'name\'],option,name, add) 실행 시작')
        return "{} = {}({}{})\n{}.pack()\n{}".format(name,command,objects['name'],option,name, add)
    IDP('wiget 정의 성공')
    IDP('sose 정의 시작')
    def sose(self,body, head = ''):
        IDP('객체 대이터를 objects 로 지정 시작')
        objects = self.option
        IDP('객체 대이터를 objects 로 지정 성공')
        IDP('''return ''\'try:
   from Tkinter import *
except:
    from tkinter import *
{}
{} = Tk()
{}
{}
{}
{}.mainloop()''\'.format(head,objects['name'],objects['sose'],body,objects['name']))
실행''')
        return 'try: from Tkinter import *\nexcept: from tkinter import *\n{}\n{} = Tk()\n{}\n{}\n{}.mainloop()'.format(head,objects['name'],objects['sose'],body,objects['name'])
    IDP('sose 정의 성공')
    IDP('what_is_Tks 정의 시작')
    def what_is_Tks(self):
        IDP('클래스 메소드 what_is_Tks 호출 성공, 이제 설명 시작')
        P('''Tkinter - upgrade
Korean middle school club tax0787
Service''')
    IDP('what_is_Tks 정의 성공')
IDP('Tks 정의 성공')
def main():
    class Test():
        def __init__(self):
            RO = Tks(name = 'self.root', sose = 'self.root.geometry("250x100")\nself.text = StringVar()\nself.text.set("Original Text")')
            exec(RO.sose(RO.wiget('self.buttonA', 'Button', ', textvariable=self.text') + RO.wiget('self.buttonB', 'Button', ',text="Click to change text", command=self.changeText')))
        def changeText(self):
            self.text.set(input('업대이트할 택스트 : '))
    app=Test()

if __name__ == "__main__": main()
