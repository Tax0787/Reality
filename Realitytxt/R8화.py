from TaxPak.TaxModle import Print as P
from TaxPak.TaxModle import Input as I
from model import war as w
from model import EndWhatError as e
go = lambda say, YON, ending: "def c():\n  a = I('{}(yes or no) : ', GUI_Bool = True, time = 0.0001)\n  if a.anser == '{}':\n    w('{}')\n    return e('{}')\n  elif a.anser == '{}':\n    return 'pass'\n  else:\n    P('yes or no 로 답해주세요', GUI_Bool = True, time = 0.0001)\n    return c()\nexec(c())\nw('''{}''')".format(say[0], YON[0], say[1], ending, YON[1], say[2])
b = 0
while b == 0:
  b = 1
  w('오렌만에 지구로 귀환했다.\n그런대 쉬어야만 할것 같았다.\n파랑색 펭귄 이 그려진 큰 호텔에 앞으로 갔다.\n그곳에는 수영장도 있었다.\n"일단 우린 돈이 있으니까(음하하하 10해원 flex), 저기 저 호텔에서 묵자."\n내가 진지하게 말했다.\n"네, 해커님!"\n엔버가 말했다.\n"그런대 날 오빠라고 불러주면 좋겠어... <해커님> 은 좀 부담스러워..."\n내가 부드럽고 부담스럽다듯이 말했다.\n"알겠어 오빠."\n엔버가 좋아하며 말했다.\n"다니엘 언제 엔버 고백 받아줄꺼야~ 크크킄"\n"하.. 조금 더 시간을줘... 흑..."\n내가 한숨을 쉬며 말했다.\n호탤의 잠자리에 누었다.\n"난 괜찮으니까, 너희 둘이 더 폭신하고 큰 침대에서자."\n에릭이 친절하게 말했다.\n\'오늘밤 같이 잤다고, 놀릴수 있겠지? 크킄!\'\n애릭이 속으로 악랄하게 생각했다.\n"난 찬성이야, 오빠!"\n엔버가 웃으며 말했다.\n"너희 의견이 그렇다면야...."\n내가 당황한체로 웃으며 말했다.\n다음날 아침,\n나는 너무 배가 고팠다.\n"하암... 애들 다 자고있네...."\n내가 일어나며 말했다.\n"샀던 삼김, 전자레인지에 돌려야지... 하아아암" 내가 졸린듯 하품하며 말했다.\n삼김이 따뜻해졌다.\n"킁킁"\n어디선가 작은 소리가 들렸다.\n"오라버니, 아니 오빠! 삼김 전자레인지에 돌렸어?" 엔버가 일어나서 귀엽게 좋아하며 말했다.\n"응..."\n내가 심쿵해서 어색하게 말했다.\n그렇게 삼김을 먹고...\n나갔는데....\n찾던 이가 있었다...\n"너가.. 왜.. 여기에...."\n제임스가 당황한체 말했다.\n"저기에 에릭이..."\n제임스가 뒷걸음질 치며 말했다.\n그리고 어떤 너튜버가 호텔 리뷰 스트리밍중,\n우리를 찍었다.\n"에잇!"\n중2병같은 손짓과 함께 사라졌다.\n"허...허억!..."\n내가 놀라서 뒷걸음질 쳤다.\n"예들아 잠시만..."\n잔뜩 긴장한체 진지하게 말했다.')
  exec(go(['나도 쫒아가야 할것 같다 갈까? ', '나는 재임스에게 암살당했다', '나도 중2병 같은 손짓과 함께 이동했다.\n"야!, 다니엘!... 어디가!!"\n에릭이 놀라서 소리쳤다.\n하지만 괌을 다 뒤질순 없었다... 이상태로\n카운터에는 나타나지 않았다.'], ['no', 'yes'], 'bed ending') + '\n' + go(['어떤 너튜버가 우릴찍었고 인터뷰 당할껏 같다, 엔버와의 시간을 망치기 싫은대 그냥 가만이 있을까 ', '나는 FBI에게 수사당하고 외계의 일을 평생 비밀로 두려움애 떨며 살다 죽었다', '"예들아..."\n내가 긴장한체 말했다.\n"이제는.... 도망쳐야해...."\n내가 눈물을 흘리며 말했다.\n"어떤 너튜버가 제임스가 순간이동하는걸 포착했어!!!"\n내가 소리쳤다.\n"뭐... 뭐라고?...."\n엔버가 놀라서 뒷걸음질 쳤다.\n" 이런 젠장!"\n에릭이 삼김을 입으로 던지며 말했다.\n"제보받기 전에 그녀석을 찾아야해..."\n그렇게 괌을 다 뒤졌지만 없었다...\n그러고는 에릭이 어제 일을 가지고 장난을 치기 치작했다.\n"야!, 너희들 대이트하기에는 하와이가 딱이야!, 같이 잔 사이인대!, 가자 크크킄"\n에릭이 놀렸다.\n"어휴.... 그러기에는 제임스는 그런..."\n나는 한숨을 쉬며 말하려던 찰나...'], ['yes', 'no'], 'Normal ending') + '\n' +go(['하와이!, 그곳에서 제임스의 기운이 강하게 느껴진다 갈까?(절대 엔버와만의 시간을 보내고 싶어서 그런개 아냐) ', '나는 FBI에게 수사당하고 외계의 일을 평생 비밀로 두려움애 떨며 살다 죽었다', '"설마 그 기운의 방향이 하와이!!!"\n내가 소리쳤다.\n"왜그래!"\n에릭이 소리쳤다.\n"헛... 그녀석을.... 찾을수 있는건강?\n엔버가 소리쳤다.\n"예들아!, 빨리 비행기 타자!!!"\n내가 소리쳤다.\n그렇게 비행기를 타고 하와이에 도착했다.\n"드디어... 하와이...."\n내가 말했다.\n"제임스의 기운이 강하게 느껴져!!!"\n내가 소리쳤다.\n"역시..."\n에릭이 말했다.\n"그러게 오빠"\n엔버가 말핬다.\n"... 너희 둘이 대이트하기 환상이야!!!"\n에릭이 개소리했다.\n"Look at them! haha"\n외국인이 우릴보고 웃었다.\n"I can speak Korean, but they can feel James\' energy. Are they crazy?"\n다른 외국인이 우릴 조롱했다.\n한편 제임스,\n"아... 이렇게 모이또 한잔 마시면서 Beach를 즐기는 것도 나쁘지 않네..."\n제임스가 즐기며 말했다.\n\'내가 내 신체나이를 성인으로 바꾸길 잘했어, 근데... 나 취한건가....\'\n제임스가 웃으며 생각했다.\n한편 다니엘 일행.\n"엔버야.... 일단... 호탤로 가자.."\n내가 긴장하며 말했다.\n"웅!"\n엔버가 좋아하며 말했다.\n한편... 도착한 마우이 리조트야, 4성급 호탤\n"엔버야... 생각해봤는데.... 나.... 너.... 좋아하는것.... 같....아..."\n내가 수줍게 말했다.\n"아앗! ... 그럼 우리 ... 1일 해요?,꺄아~!"\n엔버가 귀엽게 좋아하며 소리쳤다.'], ['no', 'yes'], 'Normal ending') + '\n' + go(['1일 할까? ', '"그럼 어쩌자는거야 #발 이재 마음 깨졌어 갈꺼야" 엔버가 말했다, 그후로는 앤버를 볼수가 없었다', '"그러자... 흡....."\n내 볼이 붉어지며 내가 답했다.\n"청혼해!, 청혼해!"\n에릭이 소리쳤다.\n"에릭오빠는 철이 안들었구먼...."\n엔버가 에릭이 한심한듯 한숨을 쉬었다.\n"엔버는 청혼 받아줘, 다니엘의"\n에릭이 신사처럼 말했다.\n"에이... 뭔소리야 ... 하하"\n나는 매우 당황하며 반대했다.\n그렇게 호텔에 묵고 있었다.\n"다음날에는 카이할 루루 비치에 갈꺼야"\n내가 진지하게 말했다.\n"거기서 그의 기운이 느껴지거든"\n내가 진지하게 덧붙였다.\n한편 제임스.\n"옆에 텐트를 쳤으니... 이제 자야지..."\n제임스가 기쁘게 말했다.\n"설마 다니엘녀석 또 오는건 아니겠지...\n제임스가 걱정하며 말했다.\n"에에.. 딸국 설마..."\n제임스가 방심하며 말했다.\n"그럼 처치하는 수밖에..... 히히... 딸국"\n제임스가 방심하며 말했다.\n다음날 아침,\n"이쪽이야..."\n내가 졸린상태로 말했다.\n그렇게 카이할 루루 비치로 갔다.\n그런대...\n"기필코 왔구만..."\n제임스가 진지하게 말했다.\n제임스는 자신이 잡히기 싫은것 같았다.\n"너부터 죽여주마.. 엔버!!!"\n제임스가 소리쳤다!\n곳 이어 고철들이 침이되어 공격했다!!!\n"앗!"\n엔버가 놀라 넘어졌다.\n"안돼!!!"\n에릭이 소리치며 엔버를 보호했다!!!\n"큭.. 으억...."\n에릭이 침을 맞으며 쓰러졌다.\n순식간에 애릭의 몸이 피범벅이 되었다!!!\n"에...에릭오빠..."\n"안돼... 이렇게 가면... 안돼!... 흑흑"\n엔버가 눈물을 흘리며 말했다!!!'], ['no', 'yes'], 'bed ending') + '\n' + go(['무섭다, 도망칠까? ', '나는 혼자 도망친 개극혐당할놈이 됬다 나는 울며 자살했다', '"제거해주마.... 제임스......"\n내가 살기와 함께 말했다.\n과거...\n"우린 깐부잖어, 깐부 사이에 니 껏 내 껏이 어디 있어~ 킄"\n"킄킄 , 아 안됭! 뭐... 멈췅 YO ~ 킄킄"\n"Tks쓰자"\n"으아악! 이 기계는 왜 자꾸 나한테 오는 거야"\n"이부분이 매인보드야, 충돌시켜!!!"\n에릭... 우리의 추억을 잘 간직할께...\n\n"...간다, 가자!"\n그때.... 그렇지만 않았어도....\n\n"/...r...m.......-......r.....f......!"\n\n이렇게도, 지금 이렇게도 되지 않았을탠대...\n\n나는 순간 소행성으로 벽을 만들고 안에,플라즈마를 넣어서 공격했고, 곳 블랙홀이 되어, 제임스를 빨아들이고, 제임스는 빨려들어갔다,, 블랙홀은 사라졌다...\n이건 모두 순식간의 일이였다\n\n\n"큭.... 다....니..엘.. 이...녀셕... 성...공했....구나....하.....하아....."\n에릭이 가쁜 숨을 쉬며 말했다.\n\n그렇게 우린 병원으로 갔다.\n"다행이도 금방 치료가 가능합니다!!!"\n의사가 말했다.\n나는 그 순간 마음이 놓였다.\n"흑! 감사합니다!!"\n내가 울며 말했다.\n그리고 치료후,\n"드디어 다 나았네!!"\n에릭이 기쁘고 활기차게 말했다.\n"그러게말이다 킄"\n내가 에릭 말투로 말했다.\n그런대...\n갑자기 파란색 포탈이 나와 우리를 빨아들였다.'], ['yes', 'no'], 'bed ending'))
  w('< 에필로그 > 에서 계속...')
  w('< 8화 > 클리어!!!')