from rich.console import Console
from rich.panel import Panel


console = Console()


def mostrar_titulo(titulo_caso,caso):
     
    
    console.print(caso)
    console.print(titulo_caso)


def mostrar_narrativa(narrativa):
    
    panel = Panel(narrativa, title="📋 RELATÓRIO DO CASO",expand = False)
    console.print(panel)


def mostrar_codigo(codigo_bugado):
    panel = Panel(codigo_bugado, title="💻 CÓDIGO SUSPEITO",expand = False)
    console.print(panel)


def mostrar_output(output_observado):
    panel = Panel(output_observado, title="🖥 COMPORTAMENTO OBSERVADO",expand = False)
    console.print(panel)

    
def mostrar_pistas(menu_investigacao):
    panel = Panel(menu_investigacao, title="🔍 PISTAS DISPONÍVEIS",expand = False)
    console.print(panel)

def mostrar_diagnostico(menu_decisao_final):
    panel = Panel(menu_decisao_final, title="⚠ DIAGNÓSTICO FINAL",expand = False)
    console.print(panel)

def mostrar_tela_inicial():
    cabecalho = "DEBUG CASES"

    boas_vindas = """
Bem-vindo, Investigador.
Sua missão é analisar sistemas defeituosos,
coletar pistas e descobrir a causa dos bugs.""" 

    opcoes = """
1. Iniciar Investigação
2. Sair """
    
    panel = Panel(cabecalho, expand = False, border_style ="red")
    console.print(panel)
    console.print(boas_vindas)
    console.print(opcoes)
