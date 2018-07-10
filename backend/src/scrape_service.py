from bs4 import BeautifulSoup
import urllib 
from urllib.request import Request
from urllib.error import URLError, HTTPError
from entities.film import Film
import lxml
import chardet

class Scrapeservice():


    @staticmethod
    def getFilm(domain, keyword):
        url = domain.url + urllib.parse.quote_plus(keyword, safe='', encoding=domain.encode)
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
            soup = BeautifulSoup(page, 'lxml')
            print(soup)
            return domain.scrap(domain, soup)

