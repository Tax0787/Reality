from TaxPak.TaxModle import Print as P
from TaxPak.TaxModle import Input as I
from model import war as w
from model import EndWhatError as e
go = lambda say, YON, ending: "def c():\n  a = I('{}(yes or no) : ', GUI_Bool = True, time = 0.0001)\n  if a.anser == '{}':\n    w('{}')\n    return e('{}')\n  elif a.anser == '{}':\n    return 'pass'\n  else:\n    P('yes or no 로 답해주세요', GUI_Bool = True, time = 0.0001)\n    return c()\nexec(c())\nw('''{}''')".format(say[0], YON[0], say[1], ending, YON[1], say[2])
b = 0
while b == 0:
  b = 1
  w('파랑색 포탈을 타고 온곳은\n저번에 싸웠던 AI전쟁터가 보이는 우주선이였다.\n"여기까지 와주셔서 감사합니다."\n"그리고, 그동안 저희를 위해 싸워주셔서\n감사합니다."\n천사가 상냥하게 말했다.\n"제임스는 블랙홀에서 꺼네서 우주평화국 감옥에 수감했습니다."\n천사가 진지하게 말했다.\n"혹시 그때... 절 보고 반했었던것 같엤는대...\n여기 남으실껀가요?"\n천사가 기대하며 말했다.')
  exec(go(['좋아한다고 하자 ', '"지금 뭐라는거야 #발 이재 마음 깨졌어 갈꺼야" 엔버가 말했다, 그후로는 앤버를 볼수가 없었다', '"아니요, 이제는 지켜야할 사랑하는 사람이 생겼습니다."\n내가 미안하게 말했다.\n"아아...."\n천사가 아쉬운듯 말했다.\n이제 우리는 집에 가야했다.\n"네, 그럼 가시지요."\n천사가 포탈을 열어주었다.\n"근데, 그동안 궁금했는데... 정체가 무엇인가요?" 내가 궁금하게 말했다.\n"저는 우주평화국 국장입니다, 현실 해커이지요." 국장님이 진지하게 말했다.\n"참, 그 컴퓨터는 이제 현실 해킹 기능은 없어졌습니다, 엡이 하나 깔렸지요? 그 엡에서 도움 호출이 오면 현실해킹 기능이 살아날 겁니다!" 국장님이 말했다.\n"넵!, 그동안 감사했습니다, 안녕계세요!"\n내가 밝개 말했다.\n그리고 포탈을 타고 도착한곳은 집,\n"엇!, 엔버야 너는 왜.. 온거야?"\n내가 말했다.\n"난 가족이 없어.. 흑..."\n엔버가 귀엽게 울며 말했다.\n"아... 그럼 우리집에 같이 살래?" 내가 말했다.\n"엇!"\n엔버가 그 제안에 좋아서 솔깃하였다.\n"웅!"\n곳이여 심쿵하게 답했다.\n"알았어!! 거래가 성사되었습니다"\n내가 말했다.\n그렇게 같이 살게 되었다...\n10년후,\n"오빠, 우리가 만난지 10년이 지났넹..."\n성인이 된 엔버가 가는 목소리로 말했다.\n"응.. 결혼한지는 1년이 지났고..."\n성인이 된 내가 말했다.\n"그때... 그... 전투"\n내가 폰 화면을 보며 말했다.\n"어제 장본 음식들이 좋더라"\n엔버가 요리를 끝내며 말했다.(사실 엔버는 요리밖에 못한다.)\n"헤헤... 밥이다..."\n에릭이 웃으며 말했다\n"오늘은 제발 설거지 미루지 말자 에릭"\n내가 더러워진 씽크대를 보며 말했다.\n폰을 끄려는 순간...\n폰엡에서 소리가 났다.\n"대규모 우주해적이 알파 1구역에 출연"\n"이제 가볼까?"\n내가 기대하며 말했다.\n'], ['yes', 'no'], 'bed ending'))
  w('    ====    THE END    ====    ')
  exec(EndWhatError('해피 엔딩'))