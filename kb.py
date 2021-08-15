import json

with open("key_dic.json", "r") as jsonf:
    json_dic = json.load(jsonf)

hex_dic = json_dic

def DebugDic():
    print(type(hex_dic))
    print(hex_dic)

def ConvertUserKey():
    if key.isupper() == True and key in hex_dic:
        print("Hex value for", key, "is:", hex_dic[key])
        uskey_c = int(hex_dic[key], 0)
        print("its Dec value is:", uskey_c)
    elif key.isupper() == False and key.upper() in hex_dic:
        key_c = key.upper()
        print(key_c)
        print("Hex value for", key, "is:", hex_dic[key_c])
        uskey_c = int(hex_dic[key_c], 0)
        print("its Dec value is:", uskey_c)
    else:
        print("NO VALIDO")
        print("RAZON:")
        if key not in hex_dic:
            print("No existe en el diccionario")
        else:
            print("no implementado")
    



print("INSERT YOUR KB KEY to get DECIMAL value")

key = input("Ingrese La tecla a convertir:")

ConvertUserKey()
