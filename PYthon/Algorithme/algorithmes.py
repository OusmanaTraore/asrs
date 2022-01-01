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
print(reverse_string2(s))