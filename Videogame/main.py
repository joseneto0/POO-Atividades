from videogame import Videogame
data = input('Digite a data de fabricacao: ')
marca = input('Digite a marca do seu videogame: ')
modelo = input('Digite o modelo do seu videogame: ')
hd = input('Capacidade de armazenamento: ')
videogame1 = Videogame(data, marca, modelo, hd)
qntdJogos = int(input('Quantos jogos você tem? '))
lista_jogos = []
for i in range(qntdJogos):
    jogos = input(f'Digite o jogo {i+1}: ')
    lista_jogos.append(jogos)
videogame1.instalar_jogos(lista_jogos)
print(videogame1)
print('=' * 20)
videogame2 = Videogame()
videogame2.marca = 'Xbox'
videogame2.modelo = 'One X'
videogame2.instalar_jogos(['Forza Horizon 5', 'Gears of War'])
print(videogame2)