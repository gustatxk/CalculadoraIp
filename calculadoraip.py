#Calculadora Ip
#Irei utilizar POO para fazer está calculadora

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
        IpBin = self.IpParaBinario(self.EnderecoIp).split(".") #Separando os octetoscem listas
        MascaraBin = self.MascaraSubredeParaBinario(self.MascaraSubrede).split(".") 
        EnderecoRedeBin = []
        for i in range(4):  #Como eu já sei que o IP e a máscara têm 4 octetos
            RedeOcteto = format(int(IpBin[i], 2) & int(MascaraBin[i], 2), '08b') #Aqui ta fazendo a operação AND bit a bit
            EnderecoRedeBin.append(RedeOcteto)
        return ".".join(str(int(octeto, 2)) for octeto in EnderecoRedeBin) #Tá tranformando de binário pra decimal e juntando os octetos
    
c1 = CalculadoraIp("192.168.1.10", "255.255.255.0")
print(f"IP em binário: {c1.IpParaBinario(c1.EnderecoIp)}")
print(f"Máscara de subrede em binário: {c1.MascaraSubredeParaBinario(c1.MascaraSubrede)}")
print(f"Endereço de rede: {c1.calcularEnderecoRede()}")

