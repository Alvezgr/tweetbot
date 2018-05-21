import requests
import bs4
import random

def curioso():

	urls = ['http://notannuevo.blogspot.com.ar/2011/08/1001-curiosidades-que-no-conocias-iii.html',
			'http://notannuevo.blogspot.com.ar/2011/03/1001-curiosidades-que-no-conocias-parte.html',
			'http://notannuevo.blogspot.com.ar/2011/05/1001-curiosidades-que-no-conocias-parte.html']
	
	url  = random.choice(urls)
	resp = requests.get(url)
	html = resp.text
	sopa = bs4.BeautifulSoup(html,'html.parser')
	
	clases = sopa.find(class_='post-body entry-content').find_all('div')
	clases = clases[6:-4]
	
	lista_curioso = []
	lista_de_curiosidades = []

	#cleaning the list beacause the web has many tags useless!
	for clase in clases:
		clase_curioso = str(clase)
		clase_curioso = clase_curioso[37:-6]
		clase_curioso = clase_curioso.replace('</b>', '')
		clase_curioso = clase_curioso.replace('<b>', '')
		clase_curioso = clase_curioso.replace('<i>', '')
		clase_curioso = clase_curioso.replace('</i>', '')
		clase_curioso = clase_curioso.replace('<br/>', '')
	
		if '#00' in clase_curioso:
			lista_curioso.append(clase_curioso)

	for curioson in lista_curioso:
		curiosidad = str(curioson)
		curiosidad = curiosidad[6:]
		
		if not '<a' in curiosidad:
			lista_de_curiosidades.append(curiosidad)

	curiosidad_random = random.choice(lista_de_curiosidades)
	
	return curiosidad_random
if __name__ == '__main__':
	print(curioso())
