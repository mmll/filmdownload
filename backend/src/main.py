# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS
from scrape_service import Scrapeservice
from entities.domain import Domain
from bs4 import BeautifulSoup
from entities.film import Film

app = Flask(__name__)
CORS(app)

# def scrapZimuzu(self，domain, soup):
#     filmItemList = soup.find_all('div', attrs={'class': 'search-item'})
#     for item in filmItemList:
#         title = item.find('strong', attrs={'class': 'list_title'}).text.strip()
#         link = item.find('div', attrs={'class': 'fl-info'}).find('a').get('href')
#         description = item.find('em').text.strip()
#         film = Film(domain.name, title, link, description)
#         result.append(film)
#         print(film)
#     return result

def scrapZimuzu(domain, soup):
    filmItemList = soup.find_all('div',attrs={'class':'search-item'})
    result = []
    for item in filmItemList:
        title = item.find('strong', attrs={'class': 'list_title'}).text.strip()
        link = item.find('div', attrs={'class': 'fl-info'}).find('a').get('href')
        description = item.find('em').text.strip()
        film = Film(domain.name, title, link, description)
        result.append(film)
        print(film)
    return result

def scrapTang(domain, soup):
    filmItemTable = soup.find('div',attrs={'class':'co_content8'}).find_all('table')
    result = []
    for item in filmItemTable:
        title = item.find_all("a").text.strip()
        link = item.find_all("a").get('href')
        description = item.find('td', attrs={'colspan':3}).text.strip()
        film = Film(domain.name, title, link, description)
        result.append(film)
        print(film)
    return result

Domainlist = [
    Domain('zimuzu', 'http://www.zimuzu.tv/search/index?keyword=', scrapZimuzu),
    Domain('电影天堂', 'http://s.ygdy8.com/plus/so.php?kwtype=0&keyword=', scrapTang)]

# if needed, generate database schema


@app.route('/search/<keyword>')
def search_film(keyword):
    service = Scrapeservice()
    resultlist = []
    for item in Domainlist:
        result = service.getFilm(item, keyword)
        resultlist += result
    return jsonify(result=[e.serialize() for e in resultlist])

