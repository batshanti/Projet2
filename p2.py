from scrap import *
from csvv import *
from book import *
from category import *
"""Import de toutes les class de notre projet"""

url = "http://books.toscrape.com/index.html"
# Création d'une instance de la classe Scrap
ScrapPage = Scrap(url)

# Récupère toutes les urls de toutes les catégories dans un tableau et supprime le 1er élément
all_url_category = ScrapPage.get_categories()
del all_url_category[0]

for lines in all_url_category:
    newCat = Category(lines)
    newCat.set_name()
    newCat.set_urls()
    newCat.add_book()
    newCSV = Csv(newCat.name)
    newCSV.write_head()
    for line in newCat.books:
        newBook = Book(line)
        newBook.get_book_infos()
        liste_infos = [newBook.product_page_url, newBook.universal_product_code, newBook.title,
                       newBook.price_excluding_tax, newBook.number_available, newBook.product_description,
                       newBook.category, newBook.review_rating, newBook.image_url]
        newCSV.write_book_infos(liste_infos)
        newBook.get_image()

        