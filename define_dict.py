# empty dictionary
d = {}

d = dict() # same thing

d = {1: "one", 2: "two"}
print(d)

eng_to_spa = {
    "hello": "hola", "yes": "si",
    "dictionary": "dictionario", "one": "uno", "two": "dos",
    "no": "no"
}
print(eng_to_spa, len(eng_to_spa))
print(f"two in spanish is {eng_to_spa['two']}")
# print(eng_to_spa["three"])
eng_to_spa["three"] = "tres" # this is how I add
eng_to_spa["two"] = "Dos"  # this is how you change a value

print("Let me teach you Spanish:")
for i in eng_to_spa:
    print(f"{i} is {eng_to_spa[i]}")
