class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome.ljust(20)} | {self.categoria.ljust(20)} | {self.ativo}"

    def listar_restaurantes():
        print(
            f"{'NOME DO RESTAURANTE'.ljust(20)} | {'CATEGORIA'.ljust(20)} | {'ATIVO'}"
        )
        for restaurante in Restaurante.restaurantes:
            print(
                f"{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}"
            )

    @property
    def ativo(self):
        return "Ativo" if self._ativo else "Desativado"


restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")

Restaurante.listar_restaurantes()
