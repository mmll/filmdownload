# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS
from scrap_service import scrapeService


# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema



@app.route('/search/<keyword>')
def search_film(keyword):
    service = scrapeService()
	result = service.getFilm('http://www.zimuzu.tv/search/index?keyword=','keyword')
    return jsonify(result)


@app.route('/exams', methods=['POST'])
def add_exam():
    # mount exam object

    return jsonify('hello'), 201