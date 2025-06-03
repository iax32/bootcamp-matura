dic = {
    "sommer": "Der Sommer ist warm",  
    "winter": "Der Winter ist kalt"
}

userinp = input("Gebe ein Schlagwort ein (sommer, winter): ").lower()
print(dic.get(userinp))
