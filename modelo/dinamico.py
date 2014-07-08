'''
Created on 24/02/2014

@author: marco
'''


dinamico=True
SelectAmb={
		'nrolineasxpag':66,
		'saltopag':['\f'],
		'actuarunavez':True,
		
		#Seleccion de ambiente
		
		'amb1':'factura',
			'selector':[
						{
						   'condicion1':{'fila':1,"columna":2,'texto':'Factura'},  		#Condicion Y
						   'condicion2':{'fila':3,"columna":4,'texto':'Copia Fac'},		#Condicion Y
						   'condicion3':{'fila':8,"columna":5,'texto':'Total'}
						}
						],
		'amb2':'factura', #Condicion O
			'selector':[
						{
						   'condicion1':{'fila':1,"columna":40,'texto':'Factura'},  		
						}
						],
			'amb3':'nota',#Otro ambiente
			'selector':[
						{
						   'condicion1':{'fila':1,"columna":2,'texto':'Factura'},
						   'condicion2':{'fila':1,"columna":2,'texto':'Factura'},
						   'condicion3':{'fila':1,"columna":2,'texto':'Factura'}
						}
						]
		}

