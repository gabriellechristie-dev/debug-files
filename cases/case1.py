import time
from visual import mostrar_titulo, mostrar_narrativa, mostrar_codigo, mostrar_output, mostrar_pistas, mostrar_diagnostico

#narrativa inicial
def run_case1(): 
    print("")
    caso = """📂 CASO 1"""
    titulo_caso = "Sistema Bancário"

    narrativa = """
Um banco recebeu diversos relatos de clientes afirmando que seus saldos desapareciam após operações de depósito e saque...
Os valores pareciam ser redefinidos de forma inesperada, comprometendo a integridade do sistema financeiro...
Sua missão é investigar o código e identificar o bug responsável pelo desaparecimento dos saldos...
                """
    mostrar_titulo(titulo_caso, caso)
    time.sleep(1.5)
    mostrar_narrativa(narrativa)
    time.sleep(1.5)

#código bugado
    codigo_bugado = """
    saldo_inicial = 100
    valor_deposito = 50

    def depositar(saldo, valor):
        saldo = valor
        return saldo

    resultado = depositar(saldo_inicial, valor_deposito)

    print("Saldo após depósito:", resultado)
    """

#output/comportamento observado
    output_observado = """ 
    "Saldo após depósito: 50"
    """
    mostrar_codigo(codigo_bugado)
    time.sleep(2)
    mostrar_output(output_observado)
    time.sleep(2)

#investigações
    menu_investigacao = """
1. Analisar variável saldo  
2. Testar depósito
    """ 

#diagnóstico
    pista_vista1 = False
    pista_vista2 = False
    mostrar_pistas(menu_investigacao)
    while pista_vista1 == False or pista_vista2 == False:
        
        escolha = int(input("Escolha uma opção para investigar: "))
        print("")
        if escolha == 1:
            if pista_vista1 == True:
                print("⚠ Você já investigou essa pista.")
            else:
                print("💡 PISTA ENCONTRADA \n\n O valor armazenado no saldo parece não permanecer após a operação.")
                print("")
                pista_vista1 = True
        
        elif escolha == 2:
            if pista_vista2 == True:
                print("⚠ Você já investigou essa pista.")
            else:
                print("💡 PISTA ENCONTRADA \n\n O valor final corresponde apenas ao último depósito realizado.")
                pista_vista2 = True
        else:
            print("Por favor, escolha a opção 1 ou 2!")
            
#resultado final
    menu_decisao_final = """1. A variável saldo está sendo reinicializada dentro da função
2. O sistema está exibindo o resultado incorretamente

    """

    mostrar_diagnostico(menu_decisao_final)

    
    decisao_final = int(input("Qual é a causa do bug? "))
    if decisao_final == 1:
        print("━━━━━━━━━━ ✅ DIAGNÓSTICO CONFIRMADO ━━━━━━━━━━ \n Causa do bug: \n A variável saldo está sendo reinicializada dentro da função,substituindo o valor anterior pelo valor do depósito. \n 🏆 Caso encerrado com sucesso.")
        return True
    elif decisao_final == 2:
        print("━━━━━━━━━━ ❌ DIAGNÓSTICO INCORRETO ━━━━━━━━━━\n A hipótese escolhida não explica o comportamento observado.")
        return False
    else:   
        print("Opção inválida. Por favor, escolha uma opção válida.")
        return False