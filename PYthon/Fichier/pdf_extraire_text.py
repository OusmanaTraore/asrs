from PyPDF2 import PdfFileWriter,PdfFileReader

f = open("recap.pdf", "rb")
reader = PdfFileReader(f)

page0= reader.getPage(0)
texte = page0.extractText()
texte = texte.replace("”","é").replace("‘","è").replace("‹","à").replace("Ò","'").replace("’","ê")

f.close()

print(texte)