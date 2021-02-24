from imports import *

def Read(Path, e, Page2):
	with open(Path) as f:
		data = json.load(f)
	t1 = threading.Thread(target=PlaySound2, args=(data, e, Page2,)).start()
	t2 = threading.Thread(target=PlayEffect, args=(data, e, Page2,)).start()

#zaściweciło mi 4 ledy w środku i wywala 
def PlayEffect(data, e, Page2):
	Page3 = Page2+1
	if data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Effect'] == 0:
		ButtonClick[Page2][e-1] = 1
	else:
		ButtonClick[Page2][e-1] = ButtonClick[Page2][e-1]+1
	for _ in range(data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Loop']):
		for i in data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Frames']:
			for i2, val in enumerate(data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Frames'][i]['Button']): 
				if isinstance(val, int):
					lp.LedCtrlRawByCode(val, data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Frames'][i]['Color'][i2])
				else:
					if str(val[:1]) == 'e':
						if val[1:] != '':
							try:
								lp.LedCtrlRawByCode(e+int(val[1:]), data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Frames'][i]['Color'][i2])
							except:
								None
						else:
							lp.LedCtrlRawByCode(e, data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Frames'][i]['Color'][i2])

					else:
						lp.LedCtrlRawByCode(data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Frames'][i]['Button'][i2], data['Pages'][e-1+Page2*98]['Page1']['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Frames'][i]['Color'][i2])


			time.wait(data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Frames'][i]['Time'])
		
def PlaySound2(data, e, Page2):
	Page3 = Page2+1
	if data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonSound[Page2][e-1]]['Sound'] == 0:
		ButtonSound[Page2][e-1] = 1
	else:
		ButtonSound[Page2][e-1] = ButtonClick[Page2][e-1]+1
	sample = data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Sample'][ButtonSound[Page2][e-1]-1]
	playsound(sample)
