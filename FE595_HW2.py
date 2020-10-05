import requests
from bs4 import BeautifulSoup as bs
import time

def webscraper():
    res = list()
    for i in range(0, 50):
        try:
            web = requests.get('http://3.95.249.159:8000/random_company')
            script = web.text
            soup = bs(script, 'html.parser')
            for x in soup.find_all('li'):
                content = x.text.split(':')
                if (content[0] == 'Name') or (content[0] == 'Purpose'):
                    res.append(content)
        except:
            res = ['error']

    with open("output.txt", 'w') as out_file:
        for t in range(len(res)):
            res2 = ""
            res2 += str(res[t])
            res2 += "\n"
            out_file.write(res2)
            time.sleep(0.5)

if __name__ == "__main__":
    webscraper()