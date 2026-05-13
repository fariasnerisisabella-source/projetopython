"""
Projeto: Jogo de Investigação Criminal
Descrição:
Sistema interativo desenvolvido em Python utilizando:
- Variáveis
- Condicionais
- Laços de repetição
- Funções
- Listas
- Dicionários
- Tratamento de erros
- Biblioteca padrão (time)

O jogador deve investigar pistas e descobrir o culpado.
"""

import time

# =========================
# DICIONÁRIO DE SUSPEITOS
# =========================

suspeitos = {
    "mordomo": {
        "comportamento": "nervoso",
        "álibi": "Disse que estava limpando a cozinha."
    },
    
    "esposa": {
        "comportamento": "calma",
        "álibi": "Disse que estava lendo no quarto."
    },
    
    "jardineiro": {
        "comportamento": "assustado",
        "álibi": "Disse que estava no jardim."
    }
}

# =========================
# LISTA DE PISTAS
# (estrutura linear)
# =========================

pistas = []

# Variável principal
culpado = "mordomo"

# =========================
# FUNÇÕES
# =========================

def introducao():
    """Mostra a introdução do jogo."""

    print("🕵️ Bem-vindo ao jogo de investigação!")
    time.sleep(1)

    nome = input("Digite o nome do detetive: ")

    print(f"\nDetetive {nome}, um crime aconteceu!")
    time.sleep(1)

    print("\nUma pessoa foi encontrada morta em uma mansão...")
    time.sleep(1)

    return nome


def mostrar_menu():
    """Exibe o menu principal."""

    print("\n========== MENU ==========")
    print("1 - Investigar cozinha")
    print("2 - Investigar jardim")
    print("3 - Investigar escritório")
    print("4 - Interrogar suspeitos")
    print("5 - Ver pistas encontradas")
    print("6 - Acusar alguém")
    print("7 - Sair")


def investigar_cozinha():
    """Investiga a cozinha."""

    print("\n🔍 Você encontrou uma faca com sangue!")

    if "Faca com sangue" not in pistas:
        pistas.append("Faca com sangue")


def investigar_jardim():
    """Investiga o jardim."""

    print("\n🔍 Pegadas estranhas encontradas no jardim!")

    if "Pegadas no jardim" not in pistas:
        pistas.append("Pegadas no jardim")


def investigar_escritorio():
    """Investiga o escritório."""

    print("\n🔍 Você encontrou documentos rasgados!")

    if "Documentos rasgados" not in pistas:
        pistas.append("Documentos rasgados")


def interrogar_suspeitos():
    """Mostra informações dos suspeitos."""

    print("\n===== SUSPEITOS =====")

    for nome, dados in suspeitos.items():

        print(f"\n👤 {nome.title()}")
        print(f"Comportamento: {dados['comportamento']}")
        print(f"Álibi: {dados['álibi']}")

        time.sleep(1)


def ver_pistas():
    """Mostra todas as pistas coletadas."""

    print("\n===== PISTAS =====")

    if len(pistas) == 0:
        print("Nenhuma pista encontrada ainda.")

    else:
        for pista in pistas:
            print(f"📌 {pista}")


def acusar():
    """Permite acusar um suspeito."""

    suspeito = input("\nQuem é o culpado? ").lower()

    if suspeito == culpado:

        print("\n🎉 Parabéns!")
        print("Você resolveu o caso!")

        if len(pistas) >= 3:
            print("🏆 Investigação perfeita! Você encontrou todas as pistas!")

        return True

    else:
        print("\n❌ Você acusou a pessoa errada...")
        return False


# =========================
# PROGRAMA PRINCIPAL
# =========================

introducao()

while True:

    mostrar_menu()

    # Tratamento de erro
    try:
        escolha = int(input("\nEscolha uma opção: "))

    except ValueError:
        print("\n⚠️ Digite apenas números!")
        continue

    # Controle de fluxo
    if escolha == 1:
        investigar_cozinha()

    elif escolha == 2:
        investigar_jardim()

    elif escolha == 3:
        investigar_escritorio()

    elif escolha == 4:
        interrogar_suspeitos()

    elif escolha == 5:
        ver_pistas()

    elif escolha == 6:

        resultado = acusar()

        if resultado:
            break

    elif escolha == 7:
        print("\n👋 Encerrando investigação...")
        break

    else:
        print("\n⚠️ Opção inválida!")