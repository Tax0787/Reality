from TaxPak.TaxModle import Print as P
from TaxPak.TaxModle import Input as I
def war(a):
  with open('test.txt', 'w') as f:
    f.write(a)
  
  with open('test.txt' , 'r') as f:
      line = f.readlines()
      for i in line:
        P(i, time = 0.0001, GUI_Bool = True)

def EndWhatError(strs):
  from os import startfile as s
  s('GSH.m4a')
  return '''w("엔딩 : " + \'{}\')
w(\'''플래이 해주셔서 감사합니다!!!
      더 좋은 소설로 찾아오겠습니다!!!
      [현재 버전 : 1.3 : 태스트 버전 (1.5 버전에는 그림이 들어갑니다)]
      음악 재생을 넣었습니다, 미흡한 작곡 양해 부탁드리고
      음치 목소리 정말 죄송합니다
      더 완벽한 GUI 버전을 기대해 주세요!!!
      재작지원 :
              == 소설 ==
      소설 집필 : inhuan lee == Bz3
      소설 평가 : so*a jang
                 릴소사     == https://han.gl/jjQOU
              == 프로그래밍 ==
      담당 동아리 : Tax0787 == https://han.gl/fBRtn
      프로그래머 : inhuan lee == Bz3
    1.5 버전에는 GUI(창) 으로 찾아뵙고
    1.8 버전에는 PYTT를 사용해 찾아뵙겠습니다
    감사합니다!!!
              == the end ==\''')
exit()'''.format(strs)