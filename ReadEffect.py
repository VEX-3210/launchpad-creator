from imports import *

def Read(Path, e, Page2):
	f = open(Path)
	data = json.load(f)
	f.close()
	#print(data['Pages'][e-1+Page2*96]['Page1']['Button%s'%e]['Animation'])
	threading.Thread(target=PlaySound2, args=(data, e, Page2,)).start()
	threading.Thread(target=PlayEffect, args=(data, e, Page2,)).start()


def PlayEffect(data, e, Page2):
	Page3 = Page2+1
	if data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Effect'] == 0:
		ButtonClick[Page2][e-1] = 1
	else:
		ButtonClick[Page2][e-1] = ButtonClick[Page2][e-1]+1
	for unnecessary in range(data['Pages'][e-1+Page2*98]['Page%s'%Page3]['Button%s'%e]['Animation']['Anim%s'%ButtonClick[Page2][e-1]]['Loop']):
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