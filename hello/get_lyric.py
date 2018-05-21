import requests
import bs4
import random

def random_lyric():
	
	all_lirics   = ['965879/','1346715/','1485965/','26/',
				  '1554957/','1485965/','1009286/','last-hope/',
				  'aint-it-fun/','1009350/','hard-times/','1554957/',
				  'still-into-you/','rose-colored-boy/','1507342/','1895354/',
				  '1554958/','1483885/','idle-worship/','fake-happy/','one-of-those-crazy-girls/']
	random_music = random.choice(all_lirics)
	
	return random_music



def get_lyrics():
	
	music = random_lyric()
	url   = 'https://www.letras.com/paramore/' + music
	
	resp  = requests.get(url)
	html  = resp.text
	soup  = bs4.BeautifulSoup(html,'html.parser')
	letra = soup.find('article').find_all('p')
	letra = random.choice(letra)
	#print(letra)
	letra = str(letra)
	letra = letra[3:]
	till  = letra.find('<')
	
	return letra[:till]

if __name__ == '__main__':
	print(get_lyrics())
