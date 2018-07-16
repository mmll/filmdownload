# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS
from scrape_service import Scrapeservice
from entities.domain import Domain
from bs4 import BeautifulSoup
from entities.film import Film
import chardet

app = Flask(__name__)
CORS(app)


def scrap_zimuzu(domain, soup):
    filmItemList = soup.find_all('div', attrs={'class': 'search-item'})
    result = []
    for item in filmItemList:
        link = domain.id + item.find('div', attrs={'class': 'fl-info'}).find('a').get('href')
        if "/resource/" in link:
            title = ''
            if hasattr(item.find('strong', attrs={'class': 'list_title'}),"text"):
                title = item.find('strong', attrs={'class': 'list_title'}).text.strip()
            description = item.find('em').text.strip()
            film = Film(domain.name, title, link, description)
            result.append(film)
            print(film)
    return result


def scrap_tang(domain, soup):
    print(soup)
    filmItemTable = []
    if (soup.find('div', attrs={'class': 'co_content8'})):
        filmItemTable = soup.find('div', attrs={'class': 'co_content8'}).find_all('table')
    result = []
    for item in filmItemTable:
        title = item.find("a").text
        link = domain.id + item.find("a").get('href')
        description = ''
        if hasattr(item.find('td', attrs={'colspan': 3}),'text'):
            description = item.find('td', attrs={'colspan': 3}).text.strip()
        film = Film(domain.name, title, link, description)
        result.append(film)
        print(film)
    return result


Domainlist = [
    Domain('http://www.zimuzu.tv', '字幕组', 'http://www.zimuzu.tv/search/index?keyword=', scrap_zimuzu, 'utf-8'),
    Domain('http://s.ygdy8.com', '电影天堂', 'http://s.ygdy8.com/plus/so.php?kwtype=0&keyword=', scrap_tang, 'gb2312')
]


# if needed, generate database schema


@app.route('/search/<keyword>')
def search_film(keyword):
    service = Scrapeservice()
    resultlist = []
    for item in Domainlist:
        result = service.getFilm(item, keyword)
        resultlist += result
    return jsonify(result=[e.serialize() for e in resultlist])
