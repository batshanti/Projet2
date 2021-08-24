import requests
import bs4
import re

class Book:

    def __init__(self, url):
        self.product_page_url = url
        self.universal_product_code = ""
        self.title = ""
        self.price_including_tax = ""
        self.price_excluding_tax = ""
        self.number_available = ""
        self.product_description = ""
        self.category = ""
        self.review_rating = ""
        self.image_url = ""

    def get_book_infos(self):

# récupère les informations d'un livre sur l'url d'un seul livre

        page = requests.get(self.product_page_url)
        doc = bs4.BeautifulSoup(page.content, 'html.parser')
        recup_ligne_td = doc.find_all("td")
        infos = []
        for line in recup_ligne_td:
            infos.append(line.string)

        self.universal_product_code = infos[0]
        self.price_including_tax = infos[3]
        self.price_excluding_tax = infos[2]
        self.number_available = infos[5]
        self.review_rating = infos[6]

        recup_description = doc.find_all("p")
        self.product_description = recup_description[3].string

        recup_category = doc.find_all("a")
        a = []
        for lines in recup_category:
            a.append(lines.string)

        self.category = a[3]

        self.title = doc.find("h1").string

        recup_image = doc.find("img")
        image = recup_image['src']
        self.image_url = image.replace("../../", "http://books.toscrape.com/")


    def get_image(self):

        page = requests.get(self.image_url)
        title_clear = re.sub('[^A-Za-z0-9]+', '', self.title)
        
        with open("JPG_FILE/" title_clear+".jpg", "wb") as file:
            file.write(page.content)
