#Calculadora Ip
#Irei utilizar POO para fazer está calculadora

class CalculadoraIp:
    def __init__(self, EnderecoIp: str, MascaraSubrede: str):
        self.EnderecoIp = EnderecoIp
        self.MascaraSubrede = MascaraSubrede

    #Convertendo o IP para binário
    def IpParaBinario(self, EnderecoIp: str):
        octetos = EnderecoIp.split(".") #Com minhas pesquisas acabei obtando por usar a função nativa "split()", ela vai separar os octetos de acordo com o delimitador que é "."
        BinarioIp = ""
        for octeto in octetos:
            BinarioIp += format(int(octeto), "08b") + "." 
        return BinarioIp[:-1]
    
    #Convertendo a mascara de subrede para binário
    def MascaraSubredeParaBinario(self, MascaraSubrede: str): #Aqui vou usar a mesma lógica que usei para o ip
        octetos = MascaraSubrede.split(".")
        BinarioMascara = ""
        for octeto in octetos:
            BinarioMascara += format(int(octeto), "08b") + "."
        return BinarioMascara[:-1]
        
    def calcularEnderecoRede(self):
        pass

c1 = CalculadoraIp("192.168.1.10", "255.255.255.0")
print(c1.IpParaBinario(c1.EnderecoIp))
print(c1.MascaraSubredeParaBinario(c1.MascaraSubrede))






