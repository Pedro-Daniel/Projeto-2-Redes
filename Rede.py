import networkx as nx

class No:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Roteador(No):
    def __init__(self, nome , endereco): #endereço ip
        super().__init__(nome, endereco)
        self.tabela_rotas = {}

    def adicionar_rota(self, destino, proximo):
        self.tabela_rotas[destino] = proximo

class Rede:
    def __init__(self):
        self.grafo = nx.Graph()
        self.nos = {}
    
    def adicionar_no(self, no):
        self.nos[no.nome] = no
        self.grafo.add_node(no.nome)
    
    def adicionar_link(self, no1,no2, custo=1):
        self.grafo.add_edge(no1, no2, weight=custo)
        #self.grafo.add_edge(no2, no1, custo=custo)

    def ping(self, origem, destino):
        try:
            caminho = nx.shortest_path(self.grafo, source=origem, target=destino)
            print(f"Ping de {origem} para {destino} foi um sucesso! Caminho: {caminho}")
        
        except nx.NetworkXNoPath:
            print(f"Ping de {origem} para {destino} falhou! Não há caminho entre os nós")
    
    def tracarrota(self , origem , destino):
        try:
            caminho = nx.shortest_path(self.grafo, source=origem, target=destino)
            print("Rota Traçada:")

            for i, no in enumerate(caminho):
                print(f"{i + 1}: {no}")
        
        except nx.NetworkXNoPath:
            print(f"Não há caminho entre os nós, falha ao traçar rota")
    def printar(self):
        print(self.nos)
        print(self.grafo)