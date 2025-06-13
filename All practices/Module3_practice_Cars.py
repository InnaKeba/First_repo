# {key,value}
cars = { 
    "Ford": 2005,
    "Mitsubishi": 2000,
    "BMW": 2019,
    "VW": 2005
    }
# print(cars.keys()) #Передає значення keys
# print(cars.items()) #Передає значення кортеджів, тобто - key,value

# for key in cars:
#     print(key) #Передає значення keys через цикл For in

models = list(cars.keys())
models.sort() #reverse=true відсортує в зворотньому порядку
header = " | ".join(models)
print(header)