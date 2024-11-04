#Calculadora Ip
#Irei utilizar POO para fazer está calculadora
#A interface será feita utilizando a bilioteca "Streamlit"

class CalculadoraIp:
    def __init__(self, EnderecoIp: str, MascaraSubrede: str):
        self.EnderecoIp = EnderecoIp
        self.MascaraSubrede = MascaraSubrede

    #Convertendo o IP para binário
    def IpParaBinario(self, EnderecoIp: str):
        octetos = EnderecoIp.split(".") #Com algumas pesquisas acabei obtando por usar a função nativa "split()", ela vai separar os octetos de acordo com o delimitador que é "."
        BinarioIp = ""
        for octeto in octetos:
            BinarioIp += format(int(octeto), "08b") + "." #Esse "08b" converte um número para binário sempre mostrando 8 bits, e coloca zeros à esquerda se precisar
        return BinarioIp[:-1]
    
    #Convertendo a mascara de subrede para binário
    def MascaraSubredeParaBinario(self, MascaraSubrede: str): #Aqui vou usar a mesma lógica que usei para o ip
        octetos = MascaraSubrede.split(".")
        BinarioMascara = ""
        for octeto in octetos:
            BinarioMascara += format(int(octeto), "08b") + "."
        return BinarioMascara[:-1]
    
    #Função para calcular o endereco de rede    
    def calcularEnderecoRede(self):
        IpBin = self.IpParaBinario(self.EnderecoIp).split(".") #Separando os octetos em listas
        MascaraBin = self.MascaraSubredeParaBinario(self.MascaraSubrede).split(".") 
        EnderecoRedeBin = []
        for i in range(4):  #Como eu já sei que o IP e a máscara têm 4 octetos
            RedeOcteto = format(int(IpBin[i], 2) & int(MascaraBin[i], 2), '08b') #Aqui ta fazendo a operação AND bit a bit
            EnderecoRedeBin.append(RedeOcteto)
        return ".".join(str(int(octeto, 2)) for octeto in EnderecoRedeBin) #Tá transformando de binário pra decimal e juntando os octetos

    #Função para calcular o endereço broadcast, usei quase a mesma lógica do endereço de rede só mudou que uso "or = |" nvés de "and = &" e também a mascara é invertida
    def calcularBroadcast(self):
        IpBin = self.IpParaBinario(self.EnderecoIp).split(".") #Nessa parte eu uso a mesma lógica para separa os octetos
        MascaraBin = self.MascaraSubredeParaBinario(self.MascaraSubrede).split(".")
        BroadcastBin = []
        for i in range(4):
            BroadcastOcteto = format(int(IpBin[i], 2) | (int(MascaraBin[i], 2) ^ 0xFF), '08b') #Aqui a máscara é invetida (inverte os bits) e também é realizado a operação OR com o IP, uso o "0xFF" porque ele transforma os bits de rede em 0 e os bits de host em 1
            BroadcastBin.append(BroadcastOcteto)
        return ".".join(str(int(octeto, 2)) for octeto in BroadcastBin)

c1 = CalculadoraIp("192.168.1.10", "255.255.255.0")
print(f"Endereço de rede: {c1.calcularEnderecoRede()}")
print(f"Endereço Broadcast: {c1.calcularBroadcast()}")

