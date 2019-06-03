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
import random


def get_html(url):
    try:
        user_agent={"user-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)"}
        user_agents =['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Beamrise/17.2.0.9 Chrome/17.0.939.0 Safari/535.8','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)','Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50','Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50','Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11','Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11']
        i=random.randint(0,7)
        user_agent['user-agent']=user_agents[i]

        response = requests.get(url, headers = user_agent)

        if response.status_code == 200:
            return response.text
        else:
            return None
        
    except RequestException:
        return None
    
def get_url(movie):
    try:
        base_url = "https://www.amazon.com/s?k=moviename+movie"
        base_url = re.sub("moviename", movie, base_url)
        base_url = re.sub(" ", "+", base_url)
    except:
        return None
    return base_url

def parse_page(html, movie):
    soup = BeautifulSoup(html, 'lxml')
    items = range(5)
    for item in items:
        yield{
            'image': soup.select('img.s-image')[item]["src"],
            'movie': movie,
            'link': "https://www.amazon.com" + str(soup.select('h5 a.a-link-normal')[item]["href"]),
        }

def get_items_details(name): # get the item details
    url = get_url(name)
    # print(url)
    html = get_html(url)
    for item in parse_page(html, name):
        print(item)
#         save_data1(item)
    return None

get_items_details("the dark knight")