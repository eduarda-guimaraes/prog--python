# Banco.py
import json
import os
import uuid

from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

ARQ_CC = "contas_corrente.json"
ARQ_CP = "contas_poupanca.json"


# ---------- utilitários ----------
def le_string(msg: str) -> str:
    return input(f"{msg}: ")


def le_float(msg: str) -> float:
    while True:
        try:
            return float(input(f"{msg}: "))
        except ValueError:
            print("Valor inválido. Tente de novo (ex.: 123.45).")


# ---------- persistência ----------
def salvar_cc(lista):
    data = []
    for c in lista:
        data.append({
            "titular": c.titular,
            "identificador": getattr(c, "identificador", None),
            "senha": c.senha,
            "saldo": float(c.saldo),
            "limite": float(getattr(c, "limite", 0.0)),
        })
    with open(ARQ_CC, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def salvar_cp(lista):
    data = []
    for c in lista:
        data.append({
            "titular": c.titular,
            "identificador": getattr(c, "identificador", None),
            "senha": c.senha,
            "saldo": float(c.saldo),
        })
    with open(ARQ_CP, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def carregar_cc():
    if not os.path.exists(ARQ_CC):
        return []
    with open(ARQ_CC, "r", encoding="utf-8") as f:
        bruto = json.load(f)
    lista = []
    for d in bruto:
        # assinatura comum: (titular, senha, limite)
        c = ContaCorrente(d["titular"], d["senha"], d.get("limite", 0.0))
        c.identificador = d.get("identificador")
        c.saldo = d.get("saldo", 0.0)
        lista.append(c)
    return lista


def carregar_cp():
    if not os.path.exists(ARQ_CP):
        return []
    with open(ARQ_CP, "r", encoding="utf-8") as f:
        bruto = json.load(f)
    lista = []
    for d in bruto:
        # tente a sua assinatura; ajuste se precisar
        try:
            cp = ContaPoupanca(d["titular"], d.get("identificador"), d.get("saldo", 0.0), d["senha"])
        except TypeError:
            cp = ContaPoupanca(d["titular"], d["senha"], d.get("saldo", 0.0))  # alternativa comum
        cp.identificador = d.get("identificador")
        cp.saldo = d.get("saldo", 0.0)
        lista.append(cp)
    return lista


# ---------- menus ----------
def acessa_cc(c1: ContaCorrente):
    print(f"\nAcessando a conta {c1.identificador}")
    print(f"Bem-vindo, {c1.titular}")
    while True:
        print("\nSelecione uma opção")
        print("d - realizar um depósito")
        print("s - realizar um saque")
        print("v - verificar o saldo")
        print("a - alterar a senha")
        print("e - sair")
        opc = le_string("").lower()

        if opc == "d":
            valor = le_float("Qual valor deseja depositar")
            c1.depositar(valor)
            print("Depósito realizado!")
        elif opc == "s":
            valor = le_float("Qual o valor do saque")
            if c1.sacar(valor):
                print("Saque realizado")
            else:
                print("Saldo + limite insuficientes")
        elif opc == "v":
            print(c1.verificaSaldo())
        elif opc == "a":
            c1.senha = le_string("Qual a nova senha")
            print("Senha alterada com sucesso!")
        elif opc == "e":
            break
        else:
            print("Opção inválida.")


def acessa_cp(c1: ContaPoupanca):
    print(f"\nAcessando a conta {c1.identificador}")
    print(f"Bem-vindo, {c1.titular}")
    while True:
        print("\nSelecione uma opção")
        print("d - realizar um depósito")
        print("s - realizar um saque")
        print("v - verificar o saldo")
        print("a - alterar a senha")
        print("e - sair")
        opc = le_string("").lower()

        if opc == "d":
            valor = le_float("Qual valor deseja depositar")
            c1.depositar(valor)
            print("Depósito realizado!")
        elif opc == "s":
            valor = le_float("Qual o valor do saque")
            if c1.sacar(valor):
                print("Saque realizado")
            else:
                print("Saldo insuficiente")
        elif opc == "v":
            print(c1.verificaSaldo())
        elif opc == "a":
            c1.senha = le_string("Qual a nova senha")
            print("Senha alterada com sucesso!")
        elif opc == "e":
            break
        else:
            print("Opção inválida.")


def cadastra_cc():
    titular = le_string("Qual o titular da conta")
    senha = le_string("Qual a senha")
    limite = le_float("Qual o limite inicial")
    c1 = ContaCorrente(titular, senha, limite)
    if not getattr(c1, "identificador", None):
        c1.identificador = uuid.uuid4().hex[:8]
    print(f"Conta cadastrada com o identificador {c1.identificador}")
    return c1


def cadastra_cp():
    titular = le_string("Qual o titular da conta")
    senha = le_string("Qual a senha")
    deposito = le_float("Qual valor depositar")
    # ajuste a assinatura conforme sua classe
    try:
        c1 = ContaPoupanca(titular, senha, deposito)  # ex.: (titular, senha, deposito_inicial)
    except TypeError:
        c1 = ContaPoupanca(titular, None, 0.0, senha)
        c1.saldo += deposito
    if not getattr(c1, "identificador", None):
        c1.identificador = uuid.uuid4().hex[:8]
    print(f"Conta cadastrada com o identificador {c1.identificador}")
    return c1


# ---------- execução direta (sem if __name__) ----------
lista_cc = carregar_cc()
lista_cp = carregar_cp()
print(f"{len(lista_cc)} contas correntes carregadas.")
print(f"{len(lista_cp)} contas poupança carregadas.")

while True:
    print("\nSelecione uma opção")
    print("cc - cadastrar conta corrente")
    print("cp - cadastrar conta poupança")
    print("ac - acessar conta corrente")
    print("ap - acessar conta poupança")
    print("e  - sair (salvar)")
    opc = le_string("").lower()

    if opc == "cc":
        lista_cc.append(cadastra_cc())

    elif opc == "cp":
        lista_cp.append(cadastra_cp())

    elif opc == "ac":
        ident = le_string("Qual o identificador")
        senha = le_string("Qual a senha")
        pos = next((i for i, c in enumerate(lista_cc) if c.validaAcesso(ident, senha)), -1)
        if pos >= 0:
            acessa_cc(lista_cc[pos])
        else:
            print("Conta inexistente ou senha incorreta!")

    elif opc == "ap":
        ident = le_string("Qual o identificador")
        senha = le_string("Qual a senha")
        pos = next((i for i, c in enumerate(lista_cp) if c.validaAcesso(ident, senha)), -1)
        if pos >= 0:
            acessa_cp(lista_cp[pos])
        else:
            print("Conta inexistente ou senha incorreta!")

    elif opc == "e":
        salvar_cc(lista_cc)
        salvar_cp(lista_cp)
        print("Dados salvos. Até mais!")
        break

    else:
        print("Opção inválida.")
