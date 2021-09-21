palvra = input("Palavra: ")

if palvra.endswith('o') or palvra.endswith('O'):
    print(f'{palvra}s')

else:
    print(f"\n{palvra} não termina com letra 'o'")