import random

# empty dictionary
eng_to_spa = {
    "apple": "manzana",
    "banana": "plátano",
    "car": "coche",
    "dog": "perro",
    "cat": "gato",
    "house": "casa",
    "sun": "sol",
    "moon": "luna",
    "book": "libro",
    "computer": "computadora",
    "keyboard": "teclado",
    "mouse": "ratón",
    "tree": "árbol",
    "water": "agua",
    "food": "comida",
    "friend": "amigo",
    "family": "familia",
    "love": "amor",
    "happy": "feliz",
    "sad": "triste",
    "beautiful": "hermoso",
    "ugly": "feo",
    "hot": "caliente",
    "cold": "frío",
    "good": "bueno",
    "bad": "malo",
    "fast": "rápido",
    "slow": "lento",
    "big": "grande",
    "small": "pequeño",
    "old": "viejo",
    "young": "joven",
    "new": "nuevo",
    "old": "viejo",
    "right": "derecho",
    "left": "izquierda",
    "up": "arriba",
    "down": "abajo",
    "inside": "dentro",
    "outside": "fuera",
    "black": "negro",
    "white": "blanco",
    "red": "rojo",
    "green": "verde",
    "blue": "azul",
    "yellow": "amarillo",
    "purple": "morado",
    "orange": "naranja",
    "gray": "gris",
    "brown": "marrón",
    "pink": "rosa",
    "gold": "oro",
    "silver": "plata",
    "to": "a",
    "from": "de",
    "with": "con",
    "without": "sin",
    "in": "en",
    "on": "sobre",
    "under": "debajo",
    "near": "cerca",
    "far": "lejos",
    "between": "entre",
    "and": "y",
    "or": "o",
    "but": "pero",
    "if": "si",
    "when": "cuando",
    "where": "donde",
    "why": "por qué",
    "how": "cómo",
    "who": "quién",
    "what": "qué",
    "which": "cuál",
    "that": "ese",
    "this": "este",
    "these": "estos",
    "those": "esos",
    "the": "el",
    "a": "un",
    "an": "una"
}


# del(eng_to_spa["hello"])
if "hello" in eng_to_spa:
    print("I know how to say hello in spanish")
else:
    print("I do not know how to say hello in Spanish")

# print(list(eng_to_spa.values()))
# print(list(eng_to_spa.keys()))

print(f"Word of the day: ", random.choice(list(eng_to_spa.values())))

score = 0
for i in range(10):
    random_word = random.choice(list(eng_to_spa.keys()))
    answer = input(f"How do you say {random_word} in Spanish? ")
    if answer == eng_to_spa[random_word]:
        print("Well done")
        score += 1
    else:
        print(f"The correct answer was {eng_to_spa[random_word]}")
print("Final score: ", score)

print(f"Horse is {eng_to_spa.get('horse', 'not defined')}")
# if 'horse' in eng_to_spanish: ... else: not defined