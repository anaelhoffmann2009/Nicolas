
meme_dict = {
            "CRINGE": "algo raro o embarazoso",
            "LOL": "una respuesta a algo gracioso",
            "ROFL":"una respuesta a una broma",
            "SHEESH":"ligera desaprobación",
            "CREEPY":"aterrador, siniestro",
            "AGGRO":"ponerse agresivo/enojado",
            "MC":"minecraft",
            "CAUSA":"es como decir amigo",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("esa palabra no esta en este diccionario")
