import json

ar = list()

with open('cenz.txt', encoding='utf-8') as fr:
    for i in fr:
        n =  i.lower().split('\n')[0]
        if n != '':
            ar.append(n)
            
with open('cenz.json', 'w', encoding='utf-8') as fe:
    json.dump(ar, fe)