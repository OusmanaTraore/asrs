fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT","vacances.jpeg","planning","data.dat")

definition_extensions = (
    ("doc", "Document Word"),
    ("exe", "Executable"),
    ("txt", "Document Texte"),
    ("jpeg","Image JPEG")
)

definition_extensions_dict = {
    "doc": "Document Word",
    "exe": "Executable",
    "txt": "Document Texte",
    "jpeg":"Image JPEG"}


def extraire_extension(nom_fichier):
    nom_fichier_split = nom_fichier.split('.')
    if len(nom_fichier_split) > 1:
        return nom_fichier_split [-1]
    return None

def obtenir_extension_definition(extension,definition):
    for d in definition:
        if  d[0].lower() == extension.lower():
            return d[1]
    return None


for fichier in fichiers:
    ext = extraire_extension(fichier)
    if ext:
        definition = definition_extensions_dict.get(ext.lower())
        if not definition:
            definition = "Extension non connue"
    else:
        definition="Aucune extension"
    print(fichier + " (" + definition + ")")

