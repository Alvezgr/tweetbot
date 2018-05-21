import requests
import bs4
import random

def dykList():
	page = random.choice(range(0,50))
	url  = 'https://www.did-you-knows.com/?page={}'.format(page)
	
	resp = requests.get(url)
	html = resp.text
	soup = bs4.BeautifulSoup(html,'html.parser')
	dyknow = soup.find(class_="dykList").find_all('li')
	
	
	all_facts = []
	for fact in dyknow :
		facts = str(fact)
		facts = facts[64:-12]
		all_facts.append(facts)

	return random.choice(all_facts)

if __name__ == '__main__':
	print(dykList())

