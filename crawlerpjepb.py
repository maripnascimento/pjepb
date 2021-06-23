import requests

def get_lawsuit(cnj_number):
	print('fazendo requisicao do cabecalho do processo')

	clean_number = cnj_cleaner(cnj_number)
	url_general = f'https://esb.tjpb.jus.br/cp-backend/sistemas/3/processos/{clean_number}?campos=completo'
	url_activity = f'https://esb.tjpb.jus.br/cp-backend/sistemas/3/processos/{clean_number}/movimentos'
	
	headers = {
	'User-Agent':'Mozilla/5.0'
	}
	
	response_general = requests.get(url_general, headers=headers)
	responde_activity = requests.get(url_activity, headers=headers)

	data = {
	'general':response_general.json(),
	'activity':responde_activity.json()
	}
	
	lawsuit = parser(data)

	return lawsuit 

def cnj_cleaner(cnj_number):
	
	return cnj_number.replace('-','').replace('.','') 

def parser(data):
	print('filtrando as informacoes')

	general = data['general']
	activity = data['activity']
	#serao os parametros da funcao no parser

	lawsuit = {
	'number': general['numeroProcesso'],
	'kind': general['classe'],
	'court_section': general['orgaoJulgador']['descricao'],
	'subject': general['assuntoPrincipal']['descricao'],
	'distribution_date': general['dataDistribuicao'],
	'value': general['valorAcao'],
	'status':  general['status']['descricao'],
	'justice_secret':general['sigiloso'],
	'related_people':[general['poloAtivo']['nomeParte'],general['poloPassivo']['nomeParte']],
	'activity': get_activity(activity)
	}

	return lawsuit 

def get_activity(data):
	print('extraindo os andamentos do processo')

	#import pdb; pdb.set_trace()
	activity_list = []
	for activity in data:
		moviment = {
		'date':activity['dataMovimentacao'],
		'text':activity['tipoMovimento']['descricao']
		}
		activity_list.append(moviment)
	
	return activity_list


print(get_lawsuit('0820115-36.2017.8.15.2001'))

