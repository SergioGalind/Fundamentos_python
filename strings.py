my_string = "EstE eS un TeXtOo"
print(type(my_string))

print(my_string.capitalize())
print(my_string.upper())
print(my_string.lower())
print(my_string.title())

print(len(my_string))

# Indexing
my_string ="Mis compañeros me caen bien putos gordes"

print(my_string[30])
for letter in my_string:
    print(f"La letra {letter}")

print(my_string[-1])
print(my_string[-2])

#slicing
print(my_string[:])
print(my_string[0:3])
print(my_string[3:])
print(my_string[3:7])
print(my_string[:7])
print(my_string[::-1])
