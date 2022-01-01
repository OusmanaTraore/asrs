# Inverser une chaîne
def reverse_string(text):
    text_inverser = ""
    for i in text:
        text_inverser = i + text_inverser
    return text_inverser

def reverse_string2(text):
    return text[::-1]

s ="Bonjour mon ami"

# print(reverse_string(s))

#=============================
#
# print(reverse_string2(s))

# Trouver le mot le plus long et le mot le plus court dans une phrase

#ordre d'apparence dans la phrase
def get_min_and_max_words(sentence):
    words = sentence.split(" ")
    min_word =min(words, key=len)
    max_word =max(words, key=len)
    return (min_word,max_word)

#ordre alphabetique en premier
def get_min_and_max_words_sorted(sentence):
    words = sentence.split(" ")
    min_word, max_word = get_min_and_max_words(sentence)

    all_min_words = [w for w in words if len(w) == len(min_word)]
    all_max_words = [w for w in words if len(w) == len(max_word)]
    
    all_min_words.sort()
    all_max_words.sort()

    return all_min_words[0] ,all_max_words[0]


def get_min_and_max_words_sorted2(sentence):
    words = sentence.split(" ")
    words.sort()
    min_word =min(words, key=len)
    max_word =max(words, key=len)
    return (min_word,max_word)



s ="Un  chasseur sachant chasser sans son chien est un bon chasseur"

min_word, max_word = get_min_and_max_words_sorted2(s)

print("Mot le plus petit: ", min_word)
print("Mot le plus petit: ", max_word)