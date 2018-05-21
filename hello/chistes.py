import requests
import bs4
import random

def get_chistes():
	page = random.choice(range(0,730,10))
	url  = 'http://www.chistes12.com/chistes-graciosos-rating31-{}.html'.format(page)
	
	resp = requests.get(url)
	html = resp.text
	soup = bs4.BeautifulSoup(html,'html.parser')
	graph= soup.find(class_="elements").find_all('p')
	graph= graph[:-2]
	
	jokes = []
	for chiste in graph:
		chistes = str(chiste)
		chistes = chistes.replace('<p>',' ')
		chistes = chistes.replace('</p>',' ')
		chistes = chistes.replace('<br/>',' ')
		chistes = chistes.replace('\r',' ')
		chistes = chistes.replace('\n',' ')
		chistes = chistes.replace('\t',' ')
		chistes = chistes.replace('\t',' ')
		chistes = chistes.replace('Â',' ')
		chistes = chistes.replace('Ã±','ñ')
		chistes = chistes.replace('Ã¡','á')
		chistes = chistes.replace('Ã©','é')
		chistes = chistes.replace('Ã³','ó')
		chistes = chistes.replace('Ã','í')
		jokes.append(chistes)

	return random.choice(jokes)

if __name__ == '__main__':
	print(get_chistes())