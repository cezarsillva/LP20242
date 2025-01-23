def cadastrar_pessoa():
    print("Cadastro de Pessoa")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    nome_mae = input("Nome da Mãe: ")
    nome_pai = input("Nome do Pai: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")

    return {
        'nome': nome,
        'cpf': cpf,
        'nome_mae': nome_mae,
        'nome_pai': nome_pai,
        'data_nascimento': data_nascimento,
        'email': email,
        'telefone': telefone
    }

def cadastrar_produtos():
    produtos = []
    while True:
        print("\nCadastro de Produtos")
        nome_produto = input("Digite o nome do produto (ou '0' para encerrar): ")
        if nome_produto == '0':
            break

        try:
            valor_unitario = float(input(f"Digite o valor unitário do produto '{nome_produto}': R$ "))
            quantidade = int(input(f"Digite a quantidade do produto '{nome_produto}': "))
            total_compra = valor_unitario * quantidade
        except ValueError:
            print("Valor inválido! Tente novamente.")
            continue
        
        produtos.append((nome_produto, valor_unitario, quantidade, total_compra))
    
    return produtos

def gravar_em_arquivo(pessoa, produtos):
    with open("cadastro_completo.txt", "w") as arquivo:
        # Grava dados pessoais
        arquivo.write("Dados Pessoais:\n")
        arquivo.write(f"Nome: {pessoa['nome']}\n")
        arquivo.write(f"CPF: {pessoa['cpf']}\n")
        arquivo.write(f"Nome da Mãe: {pessoa['nome_mae']}\n")
        arquivo.write(f"Nome do Pai: {pessoa['nome_pai']}\n")
        arquivo.write(f"Data de Nascimento: {pessoa['data_nascimento']}\n")
        arquivo.write(f"E-mail: {pessoa['email']}\n")
        arquivo.write(f"Telefone: {pessoa['telefone']}\n")
        
        # Grava os produtos cadastrados
        arquivo.write("\nProdutos Cadastrados:\n")
        total_geral = 0
        for nome_produto, valor_unitario, quantidade, total_compra in produtos:
            arquivo.write(f"Produto: {nome_produto} - Valor Unitário: R$ {valor_unitario:.2f} - Quantidade: {quantidade} - Total da Compra: R$ {total_compra:.2f}\n")
            total_geral += total_compra
        
        # Grava o valor total de todas as compras
        arquivo.write(f"\nValor Total da Compra: R$ {total_geral:.2f}")
        
        print("\nCadastro completo gravado no arquivo 'cadastro_completo.txt' com sucesso.")

def main():
    pessoa = cadastrar_pessoa()
    produtos = cadastrar_produtos()
    gravar_em_arquivo(pessoa, produtos)

if __name__ == "__main__":
    main()