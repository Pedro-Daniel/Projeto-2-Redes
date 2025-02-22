import networkx as nx
import matplotlib.pyplot as plt
from hierarchy import hierarchy_pos as h
class NetworkSimulator:
    def __init__(self):
        self.graph = nx.Graph()
        self.nodes = {}
        self.build_topology()
        self.labels={}

    def add_node(self, name, ip, node_type):
        #Adiciona um nó à rede com nome, IP e tipo (host, router ou switch).
        self.graph.add_node(name, ip=ip, type=node_type)
        self.nodes[name] = {"ip": ip, "type": node_type}

    def add_edge(self, node1, node2, link_type="ethernet"):
        #Cria um enlace entre dois nós, podendo definir o tipo de conexão.
        self.graph.add_edge(node1, node2, link=link_type)

    def build_topology(self):
        # Nó central
        self.add_node("Core", "192.168.1.160", "switch")

        # Switches de agregação
        self.add_node("a1", "192.168.1.128/28", "router")
        self.add_node("a2", "192.168.1.144/28", "router")

        # Switches de borda (subredes)
        self.add_node("Edge1", "192.168.1.0/27", "switch")   # Subrede e1 (capacidade para 24 hosts)
        self.add_node("Edge2", "192.168.1.32/27", "switch")  # Subrede e2 (capacidade para 24 hosts)
        self.add_node("Edge3", "192.168.1.64/27", "switch")  # Subrede e3 (capacidade para 15 hosts ou mais)
        self.add_node("Edge4", "192.168.1.96/27", "switch")  # Subrede e4 (capacidade para 15 hosts ou mais)

        # Hosts (um por subrede para exemplificar)
        self.add_node("Host1", "192.168.1.6", "host")
        self.add_node("Host2", "192.168.1.55", "host")
        self.add_node("Host3", "192.168.1.71", "host")
        self.add_node("Host4", "192.168.1.100", "host")

        # Conexões da topologia:
        # Conecta o Core aos switches de agregação
        self.add_edge("Core", "a1")
        self.add_edge("Core", "a2")

        # Conecta os switches de agregação aos switches de borda
        self.add_edge("a1", "Edge1")
        self.add_edge("a1", "Edge2")
        self.add_edge("a2", "Edge3")
        self.add_edge("a2", "Edge4")

        # Conecta cada switch de borda ao seu host que será usado para exemplo
        self.add_edge("Edge1", "Host1")
        self.add_edge("Edge2", "Host2")
        self.add_edge("Edge3", "Host3")
        self.add_edge("Edge4", "Host4")

        # Cria os labels que mostram o ip e nome de cada node
        self.labels = {node: f"{node}\n{data['ip']}" for node, data in self.graph.nodes(data=True)}

    def find_node_by_ip(self, ip):
        for node, data in self.graph.nodes(data=True):
            if data["ip"] == ip:
                return node
        return None

    def ping(self, source_ip, dest_ip):
        # Simula o comando ping:
        #  - Procura os nós de origem e destino a partir do IP.
        #  - Busca o caminho (shortest path) entre eles.
        #  - Exibe o caminho e estatísticas simuladas de pacotes.
        
        src = self.find_node_by_ip(source_ip)
        dest = self.find_node_by_ip(dest_ip)

        if src is None or dest is None:
            print("Endereço IP não encontrado na rede.")
            return

        try:
            path = nx.shortest_path(self.graph, src, dest)
            print("\nPing bem-sucedido!")
            # Estatísticas simuladas
            print("\n--- Estatísticas do Ping ---")
            print("Pacotes: Enviados = 4, Recebidos = 4, Perdidos = 0 (0% perda)")
        except nx.NetworkXNoPath:
            print("Destino inalcançável.")

    def traceroute(self, source_ip, dest_ip):
        # Simula o comando traceroute:
        #  - Encontra os nós de origem e destino a partir do IP.
        #  - Exibe os hops (saltos) do caminho encontrado.

        src = self.find_node_by_ip(source_ip)
        dest = self.find_node_by_ip(dest_ip)

        if src is None or dest is None:
            print("Endereço IP não encontrado na rede.")
            return

        try:
            path = nx.shortest_path(self.graph, src, dest)
            print("\nTraceroute:")
            for idx, hop in enumerate(path):
                ip = self.graph.nodes[hop]["ip"]
                print(f"Hop {idx+1}: {hop} ({ip})")
        except nx.NetworkXNoPath:
            print("Destino inalcançável.")

    def draw(self):
        self.labels = {node: f"{node}\n{data['ip']}" for node, data in self.graph.nodes(data=True)}
        pos = h(sim.graph,"Core")  
        nx.draw(sim.graph,pos=pos,labels=sim.labels,node_size=400,with_labels=True,font_size=9)
        plt.savefig('hierarchy.png')

if __name__ == "__main__":
    sim = NetworkSimulator()
    print("Bem-vindo ao simulador de rede!\n")
    print("Exemplos de IPs disponíveis na rede:")
    sim.draw()
    while True:
        print("\nComandos disponíveis: ping, traceroute, exit")
        cmd = input("Digite o comando: ").strip().lower()
        if cmd == "exit":
            print("Encerrando o simulador.")
            break
        elif cmd == "ping":
            source = input("Digite o IP de origem: ").strip()
            dest = input("Digite o IP de destino: ").strip()
            sim.ping(source, dest)
        elif cmd == "traceroute":
            source = input("Digite o IP de origem: ").strip()
            dest = input("Digite o IP de destino: ").strip()
            sim.traceroute(source, dest)
        else:
            print("Comando não reconhecido.")
