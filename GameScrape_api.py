from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from bs4 import BeautifulSoup
import urllib.request


app = Flask(__name__)
api = Api(app)
ps4_recent_url = 'http://www.metacritic.com/browse/games/release-date/new-releases/ps4/metascore'
xbox_recent_url = 'http://www.metacritic.com/browse/games/release-date/new-releases/xboxone/metascore'
switch_recent_url = 'http://www.metacritic.com/browse/games/release-date/new-releases/switch/metascore'
pc_recent_url = 'http://www.metacritic.com/browse/games/release-date/new-releases/pc/metascore'


def connect(url):
    # workaround for web crawler blockers
    req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib.request.urlopen(req)
    file = con.read()
    con.close
    return file


def parse_products(file):
    # parsing html page
    soup_page = BeautifulSoup(file, "html.parser")
    products = soup_page.findAll("div", {"class": "product_wrap"})
    return products


class Default(Resource):
    def get(self):
        return "add /xbox /ps4 /Switch or /pc at the end of the url to return the platforms respective top games and their MetaScores"


class Xbox(Resource):
    def get(self):
        file = connect(xbox_recent_url)
        products = parse_products(file)
        return {
            products[0].div.a.text.strip(): products[0].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[1].div.a.text.strip(): products[1].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[2].div.a.text.strip(): products[2].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[3].div.a.text.strip(): products[3].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[4].div.a.text.strip(): products[4].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[5].div.a.text.strip(): products[5].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[6].div.a.text.strip(): products[6].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[7].div.a.text.strip(): products[7].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[8].div.a.text.strip(): products[8].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[9].div.a.text.strip(): products[9].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip()
        }


class Ps4(Resource):
    def get(self):
        file = connect(ps4_recent_url)
        products = parse_products(file)
        return {
            products[0].div.a.text.strip(): products[0].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[1].div.a.text.strip(): products[1].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[2].div.a.text.strip(): products[2].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[3].div.a.text.strip(): products[3].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[4].div.a.text.strip(): products[4].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[5].div.a.text.strip(): products[5].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[6].div.a.text.strip(): products[6].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[7].div.a.text.strip(): products[7].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[8].div.a.text.strip(): products[8].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[9].div.a.text.strip(): products[9].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip()
        }


class Switch(Resource):
    def get(self):
        file = connect(switch_recent_url)
        products = parse_products(file)
        return {
            products[0].div.a.text.strip(): products[0].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[1].div.a.text.strip(): products[1].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[2].div.a.text.strip(): products[2].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[3].div.a.text.strip(): products[3].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[4].div.a.text.strip(): products[4].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[5].div.a.text.strip(): products[5].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[6].div.a.text.strip(): products[6].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[7].div.a.text.strip(): products[7].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[8].div.a.text.strip(): products[8].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[9].div.a.text.strip(): products[9].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip()
        }


class Pc(Resource):
    def get(self):
        file = connect(pc_recent_url)
        products = parse_products(file)
        return {
            products[0].div.a.text.strip(): products[0].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[1].div.a.text.strip(): products[1].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[2].div.a.text.strip(): products[2].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[3].div.a.text.strip(): products[3].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[4].div.a.text.strip(): products[4].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[5].div.a.text.strip(): products[5].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[6].div.a.text.strip(): products[6].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[7].div.a.text.strip(): products[7].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[8].div.a.text.strip(): products[8].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip(),
            products[9].div.a.text.strip(): products[9].find("div", {"class": "basic_stat product_score brief_metascore"}).text.strip()
        }


api.add_resource(Default, '/')
api.add_resource(Xbox, '/xbox')
api.add_resource(Ps4, '/ps4')
api.add_resource(Switch, '/switch')
api.add_resource(Pc, '/pc')


if __name__ == '__main__':
    app.run(debug=True)
