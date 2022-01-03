# import random

# def generate_random_list(n,min,max):
#     l=[]
#     for i in range(n):
#         e=random.randint(min,max)
#         l.append(e)
#     return l

# def selection_sort(l):
#     for unsorted_index in range(0,len(l)-1):
#         min = l[unsorted_index]
#         min_index = unsorted_index
#         for i in range(unsorted_index+1, len(l)):
#             if l[i] < min:
#                 min=l[i]
#                 min_index= i         
#         l[min_index]=l[unsorted_index]
#         l[unsorted_index]=min


# l= generate_random_list(50,-1000,1000)
# print("UNSORTED: ", l)

# selection_sort(l)

# print("SORTED: ", l)
# import random
 
# sujets = ("un chasseur", "une grand mère", "un chat") # ligne A
# verbes = ("mange", "écrase", "parle à")              # ligne B
# complements = ("une vache", "un char", "une fleur") # ligne C
 
# sujet = sujets[random.randint(0, len(sujets)-1)] # ligne D
# verbe = verbes[random.randint(0, len(sujets)-1)] # ligne E
# complement = complements[random.randint(0, len(sujets)-1)] # ligne F
 
# phrase = sujet + " " + verbe + " " + complement # ligne G
# print(phrase)

# import random
 
# N = 28
 
# sujets = ("un chasseur", "une grand mère", "un chat")
# verbes = ("mange", "écrase", "parle à")
# complements = ("une vache", "un char", "une fleur")
 
# phrases = []
 
# while len(phrases) < N:
#     sujet = sujets[random.randint(0, len(sujets)-1)]
#     verbe = verbes[random.randint(0, len(verbes)-1)]
#     complement = complements[random.randint(0, len(complements)-1)]
 
#     phrase = sujet + " " + verbe + " " + complement
#     if not phrase in phrases:
#         phrases.append(phrase)
 
# print(len(phrases), "phrases générées")
# for p in phrases:
#     print(p)

# import random
 
# sujets = ("un chasseur", "une grand mère", "un chat")
# verbes = ("mange", "écrase", "parle à")
# complements = ("une vache", "un char", "une fleur")
 
# def generer_phrases(donnees, nb_phrases = 0):
#     if not donnees or len(donnees) == 0:
#         return None
#     phrases = []
 
#     max_comb = 1
#     for d in donnees:
#         max_comb *= len(d)
 
#     if nb_phrases == 0 or nb_phrases > max_comb:
#         nb_phrases = max_comb
    
#     while len(phrases) < nb_phrases:
#         phrase = ""
#         for d in donnees:
#             phrase += d[random.randint(0, len(d)-1)]
 
#         if not phrase in phrases:
#             phrases.append(phrase)
 
#     return phrases
 
 
# phrases_generees = generer_phrases((
#             ("un chasseur", "une grand mère"),
#             ("mange", "écrase", "parle à"),
#             ("une vache", "un char", "une fleur"),
#             "en chantant, dans un pré, sur un lac, en souriant" # ligneA 
#             ), 10)
 
# print(len(phrases_generees), "phrases générées")
# for p in phrases_generees:
#     print(p)

age = 17
 
if age == 17:
  print("Vous êtes presque majeur")

if age >= 18:
  print("Vous êtes majeur")
else:
  print("Vous êtes mineur")







