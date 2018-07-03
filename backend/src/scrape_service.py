from bs4 import BeautifulSoup
import urllib
from entities.film import Film


class Scrapeservice():


    @staticmethod
    def getFilm(domain, keyword):
        url = domain.url + urllib.parse.quote_plus(keyword)
        print(url)
        page = urllib.request.urlopen(url)
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

