import menu

while True:
    choice = menu.menu()

    if choice == "1":
        print("Iniciando o jogo...")
    elif choice == "2":
        print("Saindo do jogo...")
        break
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")
        
