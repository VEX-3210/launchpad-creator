try:
	import json
	import os
except ImportError:
    print("ERROR: loading imports failed - Save")
    exit(0)

def crateExampleProject():
	trying = True
	try:
		if os.path.exists("Projects/example/example.json"): 
			os.remove("Projects/example/example.json") 

		f = open('Projects/example/example.json', 'w')
	except:
		print('Error: To load file - Save')
		trying = False

	if trying:
		data = {}

		data['Project'] = []
		data['Pages'] = []
		data['Project'].append({
			'Project Name': 'example',
			'Orginal Video': '-',
			'Project Autor': '-'
		})
		for r in range(8):
			p = r+1 
			for i in range(98):
				nmb = i+1
				data['Pages'].append({
					'Page%s'%p: {
						'Button%s'%nmb:{

							'Sample':['Projects/example/Kick.wav'],

							'Animation':{
								'Anim1':{

									'Effect': 0,                 #if effect == 1 to dwie animacje effect == 0 jedna animacja na przycisku
									'Sound': 0,
									'Loop': 1,

									'Frames':{
										'Frame1':{
											'Button': ['e'],
											'Time':   2,
											'Color':  [1]
										},
									}
								},
							}
						}
					}
				})

		with f as outfile:
			json.dump(data, outfile)
		f.close()