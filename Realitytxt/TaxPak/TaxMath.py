#TaxMath.py
from TaxModle import *

class SonPrint(Print):
        pass

class SonInput(Input):
        pass

def helper(i_anser = 'none' , i_Object = 'none', i_time = 0.0625, i_str_option = '', i_seps = ' ', i_files_NOGUI =  sys.stdout, i_flush = False, i_new_line_bool_NOGUI = True,p_anser = 'none' , p_Object = 'none', p_time = 0.0625, p_str_option = '', p_seps = ' ', p_files_NOGUI =  sys.stdout, p_flush = False, p_new_line_bool_NOGUI = True):
        abcde = Input("오류 해결 도우미를 키시겠습니까?(응 or 아니): >>> ",anser = i_anser , Object = i_Object, time = i_time, str_option = i_str_option, seps = i_seps, files_NOGUI =  i_files_NOGUI, flush = i_flush, new_line_bool_NOGUI = new_line_bool_NOGUI)
        if abcde == "응":
            abcd = Input("몇번 물어보시겠습니까?(숫자만): >>> ",anser = i_anser , Object = i_Object, time = i_time, str_option = i_str_option, seps = i_seps, files_NOGUI =  i_files_NOGUI, flush = i_flush, new_line_bool_NOGUI = new_line_bool_NOGUI)
            for i in range(1, int(abcd) + 1):
                abcdef = Input( str(i) + "번째 도움말은 무었입니까?: >>> ",i_anser = i_anser , i_Object = i_Object, i_time = i_time, i_str_option = i_str_option, i_seps = i_seps, i_files_NOGUI =  i_files_NOGUI, i_flush = i_flush, i_new_line_bool_NOGUI = i_new_line_bool_NOGUI)
                Print("다음을 열린 웹사이트에서 변역하세요! , 도움말 : " + str(help(abcdef)) , anser = p_anser , Object = p_Object, time = p_time, str_option = p_str_option, seps = p_seps, files_NOGUI =  p_files_NOGUI, flush = p_flush, new_line_bool_NOGUI = new_line_bool_NOGUI) # (prints 몌게변수 편집을 전 문서에서 플리스 at 2021-11-19-7:19pm) Done
                import webbrowser
                webbrowser.open("https://papago.naver.com")
            Print("./종료합니다./" , anser = p_anser , Object = p_Object, time = p_time, str_option = p_str_option, seps = p_seps, files_NOGUI =  p_files_NOGUI, flush = p_flush, new_line_bool_NOGUI = new_line_bool_NOGUI)
        else:
            Print("./종료합니다./" , anser = p_anser , Object = p_Object, time = p_time, str_option = p_str_option, seps = p_seps, files_NOGUI =  p_files_NOGUI, flush = p_flush, new_line_bool_NOGUI = new_line_bool_NOGUI)

class MiddelSchool:
        global Print
        def __init__(self, add_script_string = ''):
                self.add_script_string = add_script_string
        
        def add_script(self, passward):
                strs = ''
                for i in [0xc774,0xac83,0xc744,0x20,0xc54c,0xc544,0xb0bc,0x20,0xc2e4,0xb825,0xc774,0x20,0xc788,0xc73c,0xba74,0x20,0xbe44,0xbc88,0xc744,0x20,0xc368,0xb3c4,0x20,0xb428]:
                        strs += chr(i)
                if passward == strs:
                        exec(self.add_script_string)
        class FirstGrader:
                global Print
                def __init__(self, add_script_string = ''):
                        self.add_script_string = add_script_string

                def add_script(self, passward):
                        strs = ''
                        for i in [0xc774,0xac83,0xc744,0x20,0xc54c,0xc544,0xb0bc,0x20,0xc2e4,0xb825,0xc774,0x20,0xc788,0xc73c,0xba74,0x20,0xbe44,0xbc88,0xc744,0x20,0xc368,0xb3c4,0x20,0xb428]:
                                strs += chr(i)
                        if passward == strs:
                                exec(self.add_script_string)

                class FirstSemester:
                        def __init__(self, add_script_string = ''):
                                self.add_script_string = add_script_string

                        def add_script(self, passward):
                                strs = ''
                                for i in [0xc774,0xac83,0xc744,0x20,0xc54c,0xc544,0xb0bc,0x20,0xc2e4,0xb825,0xc774,0x20,0xc788,0xc73c,0xba74,0x20,0xbe44,0xbc88,0xc744,0x20,0xc368,0xb3c4,0x20,0xb428]:
                                        strs += chr(i)
                                if passward == strs:
                                        exec(self.add_script_string)

                        class Unit1:
                                def __init__(self, add_script_string = ''):
                                        self.add_script_string = add_script_string

                                def add_script(self, passward):
                                        strs = ''
                                        for i in [0xc774,0xac83,0xc744,0x20,0xc54c,0xc544,0xb0bc,0x20,0xc2e4,0xb825,0xc774,0x20,0xc788,0xc73c,0xba74,0x20,0xbe44,0xbc88,0xc744,0x20,0xc368,0xb3c4,0x20,0xb428]:
                                                strs += chr(i)
                                        if passward == strs:
                                                exec(self.add_script_string)
                                def fac(self, a):					                #함수정의
                                    num = a					        #분해할수 정의 (a yas)
                                    su = 2					        #소수 변수를 2로 정의
                                    so = []					        #소인수들을 넣을 리스트 추가
                                    while su <= num:			        #소수 변수가 분해할 수보다 작은동안 반복
                                        if num % su == 0:		                #만약 분해할수 / 소수변수 의 나머지가 0이라면 (c)
                                            so.append(su)			        #소수 변수값을 소인수 리스트에 넣기(c yas)
                                            num //= su			        #수 분해하기
                                        else:				        #(c no)
                                            su += 1				        #소수 변수에 1만클 더하기
                                    return  so			                #다 분해 했으니까 소인수 리스트를 내보내기
                                
                                def print_minority(self, ender):
                                        lista = []
                                        for i in range(1, ender + 1):
                                                a = self.fac(i)
                                                if len(a) == 1: lista.append(a)
                                        return lista
                                
                                def gcd(self, X,Y):
                                    while Y:
                                        X, Y = Y, X % Y
                                    return X
                                
                                lcm = lambda self, x , y: (x * y) // self.gcd(x,y)

                        class Unit2:
                                def __init__(self, add_script_string = ''):
                                        self.add_script_string = add_script_string

                                def add_script(self, passward):
                                        strs = ''
                                        for i in [0xc774,0xac83,0xc744,0x20,0xc54c,0xc544,0xb0bc,0x20,0xc2e4,0xb825,0xc774,0x20,0xc788,0xc73c,0xba74,0x20,0xbe44,0xbc88,0xc744,0x20,0xc368,0xb3c4,0x20,0xb428]:
                                                strs += chr(i)
                                        if passward == strs:
                                                exec(self.add_script_string)
                                
                                def plus_minus(self,nom):
                                        global Print
                                        class Plus:
                                                def __init__(self, nom):
                                                        self.__nom = nom

                                                class PlusError(Exception):
                                                        pass
                                                
                                                @property
                                                nom = lambda self: self.__nom

                                                @nom.setter
                                                def nom(self, value):
                                                        if not value > 0:
                                                                raise self.PlusError('The new \'nom\' is not positive , nom : ' + str(value))
                                                        self.__nom = value
                                                
                                                def print_nom(self,p_anser = 'none' , p_Object = 'none', p_time = 0.0625, p_str_option = '', p_seps = ' ', p_files_NOGUI =  sys.stdout, p_flush = False, p_new_line_bool_NOGUI = True):
                                                        Print(str(self.nom))
                                        
                                        class Minus:
                                                def __init__(self, nom):
                                                        self.nom = nom

                                                class MinusError(Exception):
                                                        pass
                                                
                                                @property
                                                nom = lambda self: self.__nom

                                                @nom.setter
                                                def nom(self, value):
                                                        if not value < 0:
                                                                raise self.PlusError('The new \'nom\' is not negative , nom : ' + str(value))
                                                        self.__nom = value
                                                
                                                def print_nom(self,p_anser = 'none' , p_Object = 'none', p_time = 0.0625, p_str_option = '', p_seps = ' ', p_files_NOGUI =  sys.stdout, p_flush = False, p_new_line_bool_NOGUI = True):
                                                        Print(str(self.nom) , anser = p_anser , Object = p_Object, time = p_time, str_option = p_str_option, seps = p_seps, files_NOGUI =  p_files_NOGUI, flush = p_flush, new_line_bool_NOGUI = new_line_bool_NOGUI)
                                        class Zero:
                                                def __init__(self):
                                                        self.nom = 0
                                                def print_nom(self,p_anser = 'none' , p_Object = 'none', p_time = 0.0625, p_str_option = '', p_seps = ' ', p_files_NOGUI =  sys.stdout, p_flush = False, p_new_line_bool_NOGUI = True):
                                                        Print(str(self.nom) , anser = p_anser , Object = p_Object, time = p_time, str_option = p_str_option, seps = p_seps, files_NOGUI =  p_files_NOGUI, flush = p_flush, new_line_bool_NOGUI = new_line_bool_NOGUI)
                                                def __str__(self):
                                                        return 'Oh, my. It\'s zero.'
                                                def __int__(self):
                                                        return 0
                                        if nom < 0: return minus(nom)
                                        elif nom > 0: return plus(nom)
                                        elif nom ==0: return zero()
                                        else: raise TypeError('It\'s not the number entered or there\'s another error., nomber : ' + str(nom))

                                def absolute_price(self, nom):
                                        return abs(nom)
                                
                                def add(self, *noms):
                                        nom = 0
                                        for i in noms:
                                                nom += i
                                        return nom
                                
                                def subtraction(self, *noms):
                                        nom = noms[0] * 2
                                        for i in noms:
                                                nom -= i
                                        return nom
                                def Multiplication(self, *noms):
                                        nom = 1
                                        for i in noms:
                                                nom *= i
                                        return nom

                                def Divide(self, *noms):
                                        nom = 1
                                        for i in noms:
                                                nom /= i
                                        return nom

                        class Unit3:
                                def __init__(self, add_script_string = ''):
                                        self.add_script_string = add_script_string

                                def add_script(self, passward):
                                        strs = ''
                                        for i in [0xc774,0xac83,0xc744,0x20,0xc54c,0xc544,0xb0bc,0x20,0xc2e4,0xb825,0xc774,0x20,0xc788,0xc73c,0xba74,0x20,0xbe44,0xbc88,0xc744,0x20,0xc368,0xb3c4,0x20,0xb428]:
                                                strs += chr(i)
                                        if passward == strs:
                                                exec(self.add_script_string)

                                def Equation(self, Ceremony):
                                        a = Ceremony
                                        def trans(strt, inputs = ' ', outputs = ' '):
                                                    my_list = list(strt)
                                                    for index, value in enumerate(my_list):
                                                        if value == inputs:
                                                            my_list[index] = outputs
                                                    return "".join(my_list)
                                        if Ceremony in '*': transe(a, inputs = '*', outputs = '') #작성중, 교과서 68쪽 참고 (2021 -11 - 19), TaxModle 시험버전 1 완료
                                        if Ceremony in '/': transe(a, inputs = '/', outputs = '_over_')
                                        class Equations:
                                                
                                                def __init__(self, str_ceremony, unknown_quantitys):
                                                        if not type(str_ceremony) == str: raise TypeError('str_ceremony must be a str')
                                                        self.__str_ceremony = str_ceremony
                                                        if not self.alphabet_in_(str_ceremony): raise self.CeremonyError
                                                        for i in unknown_quantitys.split():
                                                                if i in locals():
                                                                        raise self.UnknownQuantitysError('the new value is already been defined, value : ' + str(i))
                                                        if not type(unknown_quantitys) == str: raise TypeError('unknown_quantitysmust be a str')
                                                        self.__unknown_quantitys = unknown_quantitys

                                                def alphabet_in_(self, here):
                                                        import string
                                                        bools = False
                                                        for i in list(string.ascii_lowercase):
                                                                bools = bools or (i in here)
                                                        return bools

                                                class CeremonyError(Exception):
                                                        def __init__(self):
                                                                super().__init__('str_ceremony must have unknown_quantitys')

                                                class UnknownQuantitysError(Exception):
                                                        pass
                                                
                                                @property
                                                nom = lambda self: self.__str_ceremony

                                                @nom.setter
                                                def str_ceremony(self, value):
                                                        if not type(str_ceremony) == str: raise TypeError('str_ceremony must be a str')
                                                        if not  self.alphabet_in_(value):
                                                                raise self.CeremonyError
                                                        self.__str_ceremony = value

                                                @property
                                                nom = lambda self: self.__unknown_quantitys

                                                @nom.setter
                                                def unknown_quantitys(self, value):
                                                        if not type(unknown_quantitys) == str: raise TypeError('unknown_quantitysmust be a str')
                                                        for i in value.split():
                                                                if i in locals():
                                                                        raise self.UnknownQuantitysError('the new value is already been defined, value : ' + str(i))
                                                        self.__unknown_quantitys = value

                                                return_fungtion = lambda self : 'assignment = lambda {}: {}'.format(self.__str_ceremony, self.__unknown_quantitys)

                                                list_ceremony =  lambda self: self.__str_ceremony.split()

                                                def coefficient(self, Index, unknown_quantitys):
                                                        a = Equation(self.str_ceremony()[Index], unknown_quantitys)
                                                        exec(a.return_fungtion())
                                                        return assignment(1)

                                                def constant_term(self):
                                                        exec(self.return_fungtion())
                                                        a = self.__unknown_quantitys.split(',')
                                                        for i in a:
                                                                assignment()