import sys
import random
import time





print ("Ola novo jogador")

jogador = input('qual o seu nome? ')

print('Digite o nome do seu adversário.')
adversario = input('')

print (f'Ola {jogador}, escolha seu pokemon inicial com base no numero do mesmo.')
print ('Disponíveis : charmander = 1')
print ('              squirtle = 2')
print ('              bulbassaur = 3')

pokemon = int(input())


#linha de codigo para verificar se a numeração que o usuário colocou estava errada

while (pokemon != 1) and (pokemon != 2) and (pokemon != 3):
      print("Escolha um pokémon valido por favor.")
      print(pokemon)
      pokemon = int(input())

if pokemon == 1:
	
	#Escolha do Charmander 
	
	print("Você escolheu o Charmander, boa!")
	print("level = 5")
	print("Ataques do Charmander:\nscratch: normal type\npower: 40 \nGrowl: normal type\npower: --\n")
	
	pokemon_jogador = "Charmander"
	Ataques = ['Scratch', 'Growl']
	
	#escolha do pokemon do adversário

	pokemon_adversario1 = "Squirtle"
	Ataques_adversario1 = ['tackle', 'tail whip']

	print(f'{adversario} escolheu {pokemon_adversario1}')


elif pokemon == 2:
	
	#Escolha do Squirtle
	
	print("Você escolheu o Squirtle, boa!")
	print("Level = 5")
	print("Ataques do Squirtle:\n------------------\ntackle: normal type\npower: 40 \n------------------\ntail whip: normal type\npower: --\n")
	
	pokemon_jogador = "Squirtle"
	Ataques = ['Tackle', 'tail whip']
	

	#escolha do pokemon do adversário

	pokemon_adversario1 = "Bulbassaur"
	Ataques_adversario1 = ['tackle', 'growl']
	
	print(f'{adversario} escolheu {pokemon_adversario1}')



elif pokemon == 3:
	
	#Escolha do bulbassauro abaixo
	
	print ("Você escolheu o bulbassaur, boa!!")
	print ("Level = 5")
	print ("ataques do Bulbassaur:\n------------------\ntackle: normal type\npower: 40 \n------------------\ngrowl: normal type\npower: --\n ")
	
	pokemon_jogador = "Bulbassaur"
	Ataques = ['tackle', 'growl']
	
	#escolha do pokemon do adversário

	pokemon_adversario1 = "Charmander"
	Ataques_adversario1 = ['scratch', 'growl']

	print(f'{adversario} escolheu {pokemon_adversario1}')



#parte em que o jogador escolhe sua proxima ação

print('agora que tens um Pokémon, pretende iniciar uma batalha? \nDigite 1 para sim ou 2 para não.')

resposta_do_jogador2 = int(input())

while (resposta_do_jogador2 != 1) and (resposta_do_jogador2 != 2):
	print('Por favor, digite uma resposta válida.')
	resposta_do_jogador2 = int(input(''))

if resposta_do_jogador2 == 1:

	print("\n" * 130) #linha de codigo para limpar o CMD
	
	
	print('A batalha vai iniciar!')
	print(f'{jogador} vs {adversario}')
	#função de batalha
	
	def batalha(pokemon_jogador, pokemon_adversario1):
		
		#variáveis de vida do pokemon do Usuário e do pokemon do Bot(adversário)
		
		life_pokemon_user = 100
		life_pokemon_adv = 100
		
		print('Mandem seus Pokemons') 
		print(f'{jogador} enviou {pokemon_jogador}')
		print(f'{adversario} enviou {pokemon_adversario1}')

		while(life_pokemon_user > 0) or (life_pokemon_adv > 0):
			
			random_atack_adv = random.choice(Ataques_adversario1)

			print(f'Escolha o ataque do seu pokemon, digite 1 para utilizar o primeiro ataque ou 2 para utilizar o segundo ataque!\n {Ataques} ')
			escolha = int(input())
			#Primeira escolha de ataques
			
			if escolha == 1:
				#Subtração da vida do pokemon adversário
				life_pokemon_adv = (life_pokemon_adv - 40)
				print("\n" * 130)
				print(f"Seu pokemon atacou!\nO {pokemon_adversario1} sofreu 40 de dano!")
				print(f"Vida do {pokemon_adversario1}:{life_pokemon_adv}")
			
			#Segunda escolha de ataque
			
			elif escolha == 2:
				#Subtração da vida do pokemon adversário
				life_pokemon_adv = (life_pokemon_adv - 0)
				print("\n" * 130)
				print(f"Seu pokemon atacou!\nO {pokemon_adversario1} sofreu 0 de dano e teve sua defesa reduzida!")
				print(f"vida do {pokemon_adversario1}:{life_pokemon_adv}")

			if (life_pokemon_adv <= 0):
				print("\n" * 130)
				print(f'{jogador} venceu a batalha! +80 de pokemoney foi adicionado para {jogador}!')
				break

			print("O adversário vai atacar...")
			
			#O oponente ataca
			if (random_atack_adv == "tackle") or (random_atack_adv == "scratch"):
				print(f'O {pokemon_adversario1} usou {random_atack_adv}!')
				#subtração da vida do pokemon do usuário!
				life_pokemon_user = (life_pokemon_user - 40)

				print(f"O {pokemon_jogador} sofreu 40 de dano!")
				print(f'Vida do {pokemon_jogador}: {life_pokemon_user}')
			
			elif (random_atack_adv == "tail whip"):
				print(f'O {pokemon_adversario1} usou {random_atack_adv}!')
				#subtração da vida do pokemon do usuário!
				life_pokemon_user = (life_pokemon_user - 0)

				print(f"O {pokemon_jogador} sofreu 0 de dano e teve sua defesa reduzida!")
				print(f'Vida do {pokemon_jogador}: {life_pokemon_user}')

			elif (random_atack_adv == "growl"):
				print(f'O {pokemon_adversario1} usou {random_atack_adv}!')
				life_pokemon_user = (life_pokemon_user - 0)
				print(f"O {pokemon_jogador} sofreu 0 de dano!")


			if (life_pokemon_user <= 0):
				print("\n" * 130)
				print(f'{adversario} venceu a batalha! -40 de pokemoney foi retirado de {jogador}!')
				break

	batalha(pokemon_jogador,pokemon_adversario1)
elif resposta_do_jogador2 == 2:
	print('Finalizando o jogo.')
	time.sleep(4)

print("Jogo finalizando, fechando o jogo! Obrigado por jogar!")
time.sleep(4)

