import json
import random

f = open("word.json", encoding="utf8")

words = json.load(f)
choice_c = random.choice(list(words.keys()))

print ("Olá, seja bem vindo!")
print ("########################")

answer_user = input("Data: DDMMAAAA\n")