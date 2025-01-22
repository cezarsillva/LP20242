import os

cadastrar_cliente = 's'
nomearquivo = "clientes.txt"
nomeempresa = "EMPRESA CSS TECNOLOGIAS LTDA"
separador = "----------" * len(nomeempresa)
cabecalho =  separador + "\n" + nomeempresa + "\n" + separador

if not os.path.exists(nomearquivo):
    arquivo_cadastro = open(nomearquivo, 'w+t', encoding="utf-8")
    arquivo_cadastro.write(cabecalho)
    arquivo_cadastro.close()
    
def salvar_cliente(aluno):
    arquivo_cadastro = open(nomearquivo, "r", encoding="utf-8")
    posicao_cliente = arquivo_cadastro.read().count("Cliente") + 1
    arquivo_cadastro.close()
    
    arquivo_cadastro = open(nomearquivo, 'a+t', encoding="utf-8")
    arquivo_cadastro.write("\nCliente " + str(posicao_cliente) + "\n")
    
    for chave in cliente:
        arquivo_cadastro.write("- " + chave + ": " + cliente[chave] + "\n")
    
    arquivo_cadastro.write(separador)
    arquivo_cadastro.close()

while cadastrar_cliente == 's':
    #cadastro do cliente
    cliente = {
      "Nome": "",
      "CPF": "",
      "Mãe": "",
      "Pai": "",
      "Data de Nascimento": "",
      "Telefone": "",
    
    }
    
    cliente["Nome"] = input("Digite o nome do Cliente: ")
    cliente["CPF"] = input("Digite o CPF do Cliente: ")
    cliente["Mãe"] = input("Digite o nome da mãe do Cliente: ")
    cliente["Pai"] = input("Digite o nome do Pai do Cliente: ")
    cliente["Data de Nascimento"] = input("Digite a data de nascimento do Cliente: ")
    cliente["Telefone"] = input("Digite o Telefone do Cliente: ")
    
    '''    
    print("Digite os campos abaixo para cadastrar um cliente:")
    for chave in cliente:
        cliente[chave] = input(chave + ":")
    '''

    salvar_cliente(cliente)
    
    cadastrar_cliente = input("Deseja cadastrar mais um aluno? (s ou n)").lower()

#comando_abrir_arquivo = "notepad " + nome_arquivo
#os.system(comando_abrir_arquivo)







#Interface Grafica Cadastro de Clientes



