
# first = int(input("Enter the first intenger"))
# second = int(input("Enter the first intenger"))

# gsd = min(first,second)

# while not(first % gsd == 0 and second % gsd == 0):
#      gsd -= 1
# print(gsd)

#Задача шифр Цезара
#key = 3
#Alphabet
#For, if 

#def + <name> (параметри функції): --формула функції
def encrypt_by_key(message, key):
    #Тіло функції, все що в її середині
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(len(alpha))
    # message = "Brute is killer!!!"
    # key = 3
    #дешифрування з ключем -3 і зміна тексту в message
    # message ="EUXWH LV NLOOHU!!!"
    # key = -3
    cipher = ""
    message = message.upper() 
    for letter in message:
        if letter in alpha:
            index = (alpha.find(letter) + key) %len(alpha)
            cipher += alpha[index]
        else:
            cipher += letter
    
    print(cipher)
    return(cipher)
#Виклик функції    
encrypt_by_key("To be or not to be", 5)
encrypt_by_key("YT GJ TW STY YT GJ",-5)