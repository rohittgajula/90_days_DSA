

def Flames(name1, name2):
    
    remaining_char = []
    hashMap = {}

    for char in name1:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1
    for char in name2:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1
    
    for key, value in hashMap.items():
        if value == 1:
            remaining_char.append(key)
    
    len_remaining_char = len(remaining_char)

    flames = ['f', 'l', 'a', 'm', 'e', 's']
    index = 0

    while len(flames) > 1:
        index = (index + len_remaining_char - 1) % len(flames)
        flames.pop(index)

    flames_full = {'f':'Friends', 'l':'Love', 'a':'Affection', 'm':'Marriage', 'e':'Enemy', 's':'Sister'}

    return flames_full[flames[0]]

name1 = input("Enter your name: ")
name2 = input("Enter your mates's name: ")
print(Flames(name1, name2))

