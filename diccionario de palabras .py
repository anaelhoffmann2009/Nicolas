# Recomendación: Poner el código en inglés para que más personas de todo el mundo puedan contribuir
class Dictionary():
            def __init__(self):
                        self.meme_dict = {
                        "CRINGE": "algo raro o embarazoso",
                        "LOL": "una respuesta a algo gracioso",
                        "ROFL":"una respuesta a una broma",
                        "SHEESH":"ligera desaprobación",
                        "CREEPY":"aterrador, siniestro",
                        "AGGRO":"ponerse agresivo/enojado",
                        "MC":"minecraft",
                        "CAUSA":"es como decir amigo",
                        }
                        self.search_in_Dictionary()
            # Function to search words that is on the dictionary
            def search_in_Dictionary(self):
                        word = str(input("Write a word that you don't understand (with capital letters): "))
                        for i in range(8):
                                    if word in self.meme_dict:
                                                print(self.meme_dict[word])
                                    else:
                                                print("Error! The word is not in dictionary, please, write other word")
            
dictionary = Dictionary()
