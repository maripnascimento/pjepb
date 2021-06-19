import requests

def get_lawsuit(cnj):
	print('fazendo requisicao do cabecalho do processo')

	clean_number = cnj_cleaner(cnj)
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
	print(data['general']
)	#import pdb; pdb.set_trace()
	lawsuit = parser(data)

	return lawsuit 
def cnj_cleaner(cnj):
	
	return cnj.replace('-','').replace('.','') 

def parser(data):
	print('filtrando as informacoes')


	related_people = get_related_people(data['dados']['capa'])
	activity_list = get_activity_list(data['dados']['movimentos'])
	basic_info = get_basic_info(data['dados']['cabecalho'])
	
	lawsuit = {
	'basic_info':basic_info,
	'related_people': related_people,
	'activity_list': activity_list
	}


print(get_lawsuit('0820115-36.2017.8.15.2001'))

#duvidas:
#pq o parametro muda do metodo do get_lawsuit e do parser?