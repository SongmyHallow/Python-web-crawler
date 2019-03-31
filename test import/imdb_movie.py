try:
    import requests
except:
    import os
    os.system('pip install requests')
    import requests
from requests.exceptions import RequestException

try:
    import lxml
except:
    import os
    os.system('pip install lxml')
    import lxml

try:
    import bs4
except:
    import os
    os.system('pip install bs4')
    import bs4 
    
from bs4 import BeautifulSoup
import csv
import re


def get_movie_details(name): # get the movie details
    url = get_url(str(name))
    html = get_html(url)
    for item in parse_page(html):
        print(item)
        # save_data1(item)
    return None



def get_html(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36'
        }

        response = requests.get(url, headers = headers)

        if response.status_code == 200:
            return response.text
        else:
            return None
        
    except RequestException:
        return None


def get_url(name):
    try:
        base_url = "https://www.imdb.com/find?ref_=nv_sr_fn&q=moviename&s=tt"
        base_url = re.sub("moviename", name, base_url)
        base_url = re.sub(" ", "+", base_url)
        result_html = get_html(base_url)
        soup = BeautifulSoup(result_html,'lxml')
        url = soup.select_one(' td.primary_photo > a')['href']
        url = 'https://www.imdb.com'+url
    except:
        return None
    return url


def parse_page(html):
    soup = BeautifulSoup(html, 'lxml')
    items = range(1)
    for item in items:
        yield{
            'poster': get_poster(soup.select('div.poster img')[item]["src"]),
            'name': get_name(soup.select('div.title_wrapper h1')[item].text),
            'score': soup.select('span[itemprop="ratingValue"]')[item].string,
            'time': soup.select('span#titleYear > a')[item].string,
            'ratings': get_ratings(soup.select('span[itemprop="ratingCount"]')[item].string),
            'director': soup.select('div.credit_summary_item a[href$="_dr"]')[item].string,
            'star': get_stars(soup.select('div.credit_summary_item a[href$="_sm"]')),       
            'movie_length': get_movie_length(soup.select('div.subtext > time')[item].string),
            'movie_type': get_movie_type(soup.select('div.subtext a[href*="/search/title?genres"]')),
            'storyline': soup.select('div.article div.inline span')[item].text.strip(' '),
        }
    

def get_movie_length(data):
    try:
        movie_length_form = re.compile(r'\d.*min')
        movie_length = re.search(movie_length_form, data)
        length = movie_length.group().replace(' ','')
    except:
        return None
    return length

def get_movie_type(data):
    try:
        movie_type = []
        for i in range(len(data)):
            movie_type.append(data[i].string)
        genres = ",".join(movie_type)
    except:
        return None
    return genres

def get_ratings(data):
    try:
        data = data.replace(',','')
    except:
        return None
    return data

def get_stars(data):
    starlist = []
    for i in range(len(data)):
        starlist.append(data[i].string)
    starlist.pop()
    stars = ",".join(starlist)
    return stars

def get_poster(src):
    src_prefix_form = re.compile(r'.*@')
    src_prefix = re.search(src_prefix_form, src)
    
    src_suffix_form = re.compile(r'_\..*')
    src_suffix = re.search(src_suffix_form, src)
    src_suffix = re.sub("_", "", src_suffix.group())
    
    if (src_prefix == None):
        src_prefix_form = re.compile(r'.*\._')
        src_prefix = re.search(src_prefix_form, src)
        src_prefix = re.sub("._", "", src_prefix.group())
        return src_prefix+src_suffix
    
    return src_prefix.group()+src_suffix


def get_name(data):
    try:
        name1 = re.sub(r'\\.*', '', data)
        name2 = re.sub(r'\(\d+\)', '', name1)
    except :
        return None
    return name2

def save_data1(items):
    with open('imdb_movie.csv', 'a', encoding='utf_8_sig', newline='') as f:
        fieldnames = ['poster', 'name', 'score', 'time', 'ratings', 'director', 'star',
                      'movie_length', 'movie_type', 'storyline']
        w = csv.DictWriter(f, fieldnames = fieldnames)
        w.writerow(items)