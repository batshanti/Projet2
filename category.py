import requests
import bs4

class Category:

    def __init__(self, url):
        self.name = ""
        self.url = url
        self.books = []
        self.urls = []

    def set_name(self):
        
# Récupère le nom de la catégorie
        
        self.name = self.url.split("/books/")[1].split("/index.html")[0].split("_")[0]

    def set_urls(self):

# Récupère le nombre de livre par catégorie et détermine le nombre de pages et leurs urls

        page = requests.get(self.url)
        doc = bs4.BeautifulSoup(page.content, 'html.parser')
        soup = doc.find(class_="form-horizontal")
        nombre_de_livre_par_cat = int(soup.find("strong").string)
        nombre_de_page_par_cat = nombre_de_livre_par_cat // 20
        reste = nombre_de_livre_par_cat % 20

        pageUrl = []

        if nombre_de_page_par_cat > 0 and reste > 0:
            for x in range(nombre_de_page_par_cat + 1):
                x = x + 1
                pageUrl.append(self.url.replace("index.html", "page-") + str(x) + ".html")

        if nombre_de_page_par_cat == 0 and reste > 0:
            pageUrl.append(self.url)

        self.urls = pageUrl

    def add_book(self):

# Ajoute les UrLs de chaques livres d'une catégorie dans un tableau

        for line in self.urls:
            page = requests.get(line)
            soupPage = bs4.BeautifulSoup(page.text, "html.parser")
            soup = soupPage.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
            for lines in soup:
                self.books.append((lines.h3.a['href']).replace("../../../", "http://books.toscrape.com/catalogue/"))
