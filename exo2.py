my_dict =   { 
            "dad": "Eise", 
            "sister_1": "Iris",
            "sister_2": "Nicky"
            }
key = "dad"

if key in my_dict:
    print('dad is in the dictionary!')

my_dict1 = {"fruit": "Apple", 
           "vegetable":"Capsicum"
           }
key = "meat"

if key not in my_dict1:
    my_dict1["meat"] = "empty"
    print("meat is not in the dictionary! The new dictionary is:", my_dict1)
