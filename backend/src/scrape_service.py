from bs4 import BeautifulSoup
import urllib 
from urllib.request import Request
from urllib.error import URLError, HTTPError
from entities.film import Film


class Scrapeservice():


    @staticmethod
    def getFilm(domain, keyword):
        url = domain.url + urllib.parse.quote_plus(keyword)
        print(url)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
        	page = urllib.request.urlopen(url)
        except HTTPError as e:
        	print("Error code: ", e.code)
        	return [];
        except URLError as e:
        	print("Reason: ", e.reason)
        	return [];
        else:
        	soup = BeautifulSoup(page, 'html.parser')
        	return domain.scrap(domain,soup)
        # filmItemList = soup.find_all('div', attrs={'class': 'search-item'})
        # for item in filmItemList:
        #     title = item.find('strong', attrs={'class': 'list_title'}).text.strip()
        #     link = item.find('div', attrs={'class': 'fl-info'}).find('a').get('href')
        #     description = item.find('em').text.strip()
        #     film = Film(domain.name, title, link, description)
        #     result.append(film)
        #     print(film)
        # return result

