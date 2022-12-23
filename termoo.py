import json
import random

f = open("word.json", encoding="utf8")

words = json.load(f)
choice_c = random.choice(list(words.keys()))

print ("Olá, seja bem vindo!")
print ("########################")

n_choices = 5

while n_choices > 0:
    print("Dica: " + words[choice_c])
    answer_user = input("Data: DDMMAAAA\n")

    if len(answer_user) != 8
        print("Erro na entrada. A resposta deve conter 8 digitos.")
        continue

    if answer_user.isdigit():
        check = []
        for i in range(8):
            if answer_user[i] == choice_c[i]:
                check.append("V")
            else:
                check.append("F")

        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(answer_user))
        print("#####################\n")
    else:
        print("Erro na entrada. A resposta deve ser uma data!")
        continue
    n_choices = n_choices -1