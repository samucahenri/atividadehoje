class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        return self.preco - desconto

    def exibir_info(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")

def main():
    
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produto = Produto(nome, preco)
    print("\n Dados do Produto ")
    produto.exibir_info()
    percentual = float(input("\nDigite o percentual de desconto: "))
    novo_preco = produto.aplicar_desconto(percentual)
    print(f"Preço com desconto: R$ {novo_preco:.2f}")


if __name__ == "__main__":
    main()