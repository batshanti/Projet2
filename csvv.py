import csv

class Csv:
    """Class utilisée pour la création des fichiers csv"""
    def __init__(self, cat_name):
        self.head = ["product_page_url", "universal_product_code", "title", "price_including_tax",
                     "price_excluding_tax", "number_available", "product_description", "category", "review_rating",
                     "image_url"]
        self.cat_name = cat_name

    def write_head(self):
        """Crrer un fichier csv qui porte le nom de la catégie + ajoute l'en-tête"""  

        with open(self.cat_name + ".csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(self.head)

    def write_book_infos(self, liste_infos):
        """Ecrire les informations de chaques livres d'une catégirue"""

        with open(self.cat_name + ".csv", "a", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(liste_infos)
