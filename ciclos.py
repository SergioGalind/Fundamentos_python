#ciclos
#While exp_booleana

i=1
num=24
while i<=10:
    print (f"{num}*{i}={num*i}")
    i += 1
else:
    print("termina ciclo")

#Coclo for
# permite recorrer iterables 
# iterable -> objeto que se puede recorrer 
# for item iterable 

my_string = "Hola a todos"
for letter in my_string:
    print(letter, end=', ' )
print()

my_list= ["Uno", "dos", "tres", "cuatro"]
for item in my_list:
    print(item, end=', ')
print()

#function rangel()
# range(end)

for i in range(10):
    print(i, end=', ')
print()
# range(start, end)
for i in range(10, 20):
    print(i, end=', ')
print()
#range
for i in range(10, 100, 10):
    print(i, end=', ')
print()
