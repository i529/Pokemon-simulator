import sys

cont = 0


print ("Ola novo jogador")

jogador = input('qual o seu nome? ')

print('Digite o nome do seu adversário.')
adversario = input('')

print (f'Ola {jogador}, escolha seu pokemon inicial com base no numero do mesmo.')
print ('Disponíveis : charmander = 1')
print ('              squirtle = 2')
print ('              bulbassaur = 3')

pokemon = int(input())

while (pokemon != 1) and (pokemon != 2) and (pokemon != 3):
      print("Escolha um pokémon valido por favor.")
      print(pokemon)
      pokemon = int(input())

if pokemon == 1:
	 #Escolha do Charmander
         pokemon_usuario1 = 'Charmander'
	 print("Você escolheu o Charmander, boa!")
	 print("level = 5")
	 print("Ataques do Charmander:\nscratch: normal type\npower: 40 \nGrowl: normal type\npower: --\n")

	 pokemon_adversario1 = 'squirtle'

	 print(f'{adversario} escolheu {pokemon_adversario1}')



elif pokemon == 2:
	#Escolha do Squirtle
        pokemon_usuario1 = 'Squirtle'
	print("Você escolheu o Squirtle, boa!")
	print("Level = 5")
	print("Ataques do Squirtle:\n------------------\ntackle: normal type\npower: 40 \n------------------\ntail whip: normal type\npower: --\n")

	pokemon_adversario1 = 'Bulbassaur'

	print(f'{adversario} escolheu {pokemon_adversario1}')

elif pokemon == 3:
	#Escolha do bulbassauro abaixo
        pokemon_usuario1 = 'Bulbassaur'
	print ("Você escolheu o bulbassaur, boa!!")
	print ("Level = 5")
	print ("ataques do Bulbassaur:\n------------------\ntackle: normal type\npower: 40 \n------------------\ngrowl: normal type\npower: --\n ")

	pokemon_adversario1 = 'Charmander'

	print(f'{adversario} escolheu {pokemon_adversario1}')

#parte em que o jogador escolhe sua proxima ação

print('agora que tens um Pokémon, pretende iniciar uma batalha? \nDigite 1 para sim ou 2 para não.')

resposta_do_jogador = int(input())

while (resposta_do_jogador != 1) and (resposta_do_jogador != 2):
	print('Por favor, digite uma resposta válida.')
	resposta_do_jogador = int(input())

if resposta_do_jogador == 1:
	print('A batalha vai iniciar!')
	print(f'{jogador} vs {adversario}')

elif resposta_do_jogador == 2:
	sys.exit()

print('Mandem seus Pokemons')

	


a = ('digite algo para sair')
