for i in range(7):
    print(meme_dict)
    meme_dict = {
                "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
                "LOL": "Częsta reakcja na coś zabawnego",
                "XD": "Reakcja na jakiś żart lub coś zabawnego",
                "ROFL": "odpowiedź na żart",
                "SHEESH": "lekka dezaprobata",
                "CREEPY": "straszny, złowieszczy",
                "AGGRO": "stać się agresywnym/zły"
                }
                
    
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
        meme_dict = {"OK": "Reakcja na słowo"}
    else:
        print("nie ma jeszcze takiego słowa")
