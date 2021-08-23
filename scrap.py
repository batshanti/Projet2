import requests
import bs4

class Scrap:

    def __init__(self, url):
        self.url = url

    def getCategories(self):

# récupère la liste de toutes les catégories + kes Urls

        allCategories = []
        homePage = requests.get(self.url)
        soupHomePage = bs4.BeautifulSoup(homePage.text, 'html.parser')
        listeOfListe = soupHomePage.findAll('li')
        for item in listeOfListe:
            try:
                a = item.find('a')
                link = a['href']
                if link.find("category") > -1:
                    categoryUrl = self.url.split("index.html")[0] + link
                    allCategories.append(categoryUrl)

            except:
                pass

        return allCategories
