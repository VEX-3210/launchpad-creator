import json

trying = True
try:
	f = open('./.Projects/Kaskobi - Paris/Kaskobi - Paris.json', 'x')
except:
	trying = False

if trying:
	data = {}

	data['Project'] = []
	data['Pages'] = []
	data['Project'].append({
	    'Project Name': 'Kaskobi - Paris',
	    'Orginal Video': 'https://www.youtube.com/watch?v=NEWPXKJKFSc',
	    'Project Autor': 'Kaskobi (VEX remake)'
	})
	for r in range(8):
		p = r+1 
		for i in range(98):
			nmb = i+1
			data['Pages'].append({
			    'Page%s'%p: {
					'Button%s'%nmb:{

						'Sample':['',],

						'Animation':{
							'Anim1':{

								'Effect': 0,                 #if effect == 1 to dwie animacje effect == 0 jedna animacja na przycisku
								'Sound': 0,
								'Loop': 1,

								'Frames':{
									'Frame1':{
										'Button': [0],
										'Time':   0,
										'Color':  [0]
									},
								}
							},
						}
					}
				}
			})

	f = open('./.Projects/Kaskobi - Paris/Kaskobi - Paris.json', 'w')
	with f as outfile:
	    json.dump(data, outfile)