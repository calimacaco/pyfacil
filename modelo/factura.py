'''
Created on 27/02/2014

@author: marco
'''
globales = {
	'papel':'carta',
	'orientarcion':'vertical',
	'copias':1,
	'compaginadas':False,
	'duplex':0,													#0 No, 1 Largo, 2 corto 
	'saltopag':['\f','fin de pagina'],
	'antesfinpag':False,
	'eliminarLnIncio':{'primerpag':1,'todas':1,'ultima':1},
	'eliminarLnFinal':{'primerpag':1,'todas':1,'ultima':1},
	'libro':True,												#La primera con la ultima
	'Cuadernillo':4,
	'PagLog':4
}


seleccion={'campo1':[
		
			{
			'tipo':'texto',
			'fila':[1,2],
			'columna':[1,10],
			#'prefijo':'Col',
			#'campo':2,
			'letra':'Arial',
			'tam':12,
			'negrilla':False,
			'cursiva':False,
			'alinar':0,			#0=izquierda, 1 derecha, 2 centro,3 justificado
			}		
		
		],
		'campo2':[
		
			{
			'tipo':'nomPDF',
			'selector':[
						{'prefijo':'Col','campo':3}
						]
			}		
		
		],
		'campo3':[
				{'tipo':'correo',
				'asunto':[
						{'prefijo':'Col','campo':3}
						],
				'enviar':[
						{'fila':[1,1],'columna':[3,10]}
						],
				'copia':[
						{'fila':[2,1],'columna':[3,10]}
						],
				'copiabs':[
						{'fila':[2,1],'columna':[38,10]}
						],
				'contenido':[
						{'fila':[2,1],'columna':[38,10]}
						],
				#los adjunto falta
				
				}
				
				]
		
}