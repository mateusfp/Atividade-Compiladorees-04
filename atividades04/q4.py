def split(word):
    return [char for char in word]

lst1 = [11, 18, 19, 99, 99, 19,18,25,82,0,5,82,152,1222,]

word = input('Adicione um Palavra: ').upper()
lst2 = split(word)

print(''.join([str(a) + b for a, b in zip(lst1, lst2)]))