from bs4 import BeautifulSoup
import urllib.request
from entities.film import Film

class scrapeService():
	domainList = [
	'http://www.zimuzu.tv/search/index?keyword=',
	'http://s.ygdy8.com/plus/so.php?kwtype=0&searchtype=title&keyword='
	]
	@classmethod
	def getFilm(domain,keyword):
		result = []
		url  = domain + keyword;
		page = urllib.request.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		filmItemList = soup.find_all('div', attrs={'class':'search-item'})
		for item in filmItemList:
			title = item.find('strong', attrs={'class':'list_title'}).text.strip()
			link = item.find('div', attrs={'class':'fl-info'}).find('a').get('href')
			description = item.find('em').text.strip()
			film = Film(domain, title, link, description)
			result.append(film)
			print(film)
		return result