def cria_conta(numero, agencia, titular, saldo, limite):
    conta = {"numero":numero, "agencia":agencia, "titular":titular, "saldo":saldo, "limite":limite}
    return conta
    
def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Conta: {} \nAgencia: {} \nSaldo: R$ {} ,00 \nLimite: R$ {} ,00".format(conta["numero"],conta["agencia"],conta["saldo"],conta["limite"]))
