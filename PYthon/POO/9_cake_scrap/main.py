from bs4 import BeautifulSoup, BeautifulStoneSoup

#ouverture du fichier
f = open("recette.html","r")
html_content = f.read()
f.close()
soup= BeautifulSoup(html_content, "html.parser")

#recherche
titre_h1= soup.find("h1")
paragraphe_description= soup.find("p", class_="description")
div_info = soup.find("div" , class_="info")
source_image = div_info.find("img")

print("Titre de la page HTML", titre_h1.text)
print("Paragraphe de description:", paragraphe_description.text)
print("Le src de l'image est", source_image["src"])

print()

