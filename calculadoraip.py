#Calculadora Ip
#Irei utilizar POO para fazer está calculadora
#Vou usar a biblioteca "ipaddress" para fazer os cálculos
#A tabela que exibi os dados irei utilizar a biblioteca "Pandas"

from ipaddress import *  #Importando a biblioteca ipaddress para os cálculos
import pandas as pd  #Importando pandas para fazer a tabela

class CalculadoraIp:
    def __init__(self, enderecoIp, mascaraSubrede):  #Aqui é o método construtor da classe
        self.enderecoIp = enderecoIp  
        self.mascaraSubrede = mascaraSubrede  
        self.rede = IPv4Network(f"{enderecoIp}/{mascaraSubrede}", strict=False)  #Cria um objeto de rede IPv4 com o endereço IP e a máscara
        self.classeEndereco = self.definirClasseIp(enderecoIp)  #chama a função para definir a classe do IP

    def mascaraParaPrefixo(self):  #função para a conversão da máscara de sub-rede para o formato de prefixo CIDR
        mascara_ip = self.mascaraSubrede.split(".")
        prefixo = sum([bin(int(part)).count("1") for part in mascara_ip])  #Conta os bits 1 de cada octeto e soma
        return f"/{prefixo}"  #Retorna o prefixo no formato CIDR (ex: /24)

    def definirClasseIp(self, ip):  #Função para definir a classe do IP
       primeiroOcteto = int(ip.split('.')[0]) 
       if 1 <= primeiroOcteto <= 126:
            return 'A'  
       elif 128 <= primeiroOcteto <= 191:
            return 'B' 
       elif 192 <= primeiroOcteto <= 223:
            return 'C'  
       elif 224 <= primeiroOcteto <= 239:
            return 'D' 
       elif 240 <= primeiroOcteto <= 255:
            return 'E'
       else:
            return 'Desconhecida'

    def calcularEnderecoRede(self):  #Aqui tá calculando o endereço de rede a partir do IP e da máscara
        return self.rede.network_address 

    def calcularPrimeiroHost(self):  #Aqui tá calculando o primeiro host disponível na rede
        return list(self.rede.hosts())[0] 

    def calcularUltimoHost(self):  #Aqui tá calculando o último host disponível na rede
        return list(self.rede.hosts())[-1]

    def calcularEnderecoBroadcast(self):  #Aqui tá calculando o endereço de broadcast da rede
        return self.rede.broadcast_address

    def calcularNumeroSubredes(self):
        prefixoAtual = self.rede.prefixlen  #Notação CIDR atual da máscara de sub-rede
        prefixoBase = { #Determina o CIDR base de acordo com a classe de endereço
            'A': 8,
            'B': 16,
            'C': 24
        }.get(self.classeEndereco, None)
        if prefixoBase is None:
            raise ValueError(f"Classe de endereço {self.classeEndereco} inválida para cálculos de rede.")
        bitsEmprestados = prefixoAtual - prefixoBase
        if bitsEmprestados < 0:
            raise ValueError(f"A máscara de sub-rede ({self.mascaraSubrede}) é inválida para a classe {self.classeEndereco}.")
        numSubredes = 2 ** bitsEmprestados
        if numSubredes <= 0:
            raise ValueError("Número de sub-redes calculado é inválido, verifique a máscara de sub-rede.")
        return numSubredes
    
    def calcularHostsTotalPorSubrede(self):  #Calculando o número de hosts por sub-rede
        return self.rede.num_addresses
    
    def calcularHostsUtilizaveisPorSubrede(self):
        return self.rede.num_addresses - 2
    
    def verificarPublicoPrivado(self):  #verifição pra saber se o endereço IP é público ou privado
        return "Privado" if self.rede.is_private else "Público"
    
    def gerarTabela(self): #Gera a tabela de resultados com oq foi obtido
        dados = {
            'Detalhes': [ #Aqui está sendo definido oq vai aparecer na coluna detalhes
                'Endereço IP',  
                'Máscara de Sub-rede',  
                'Notação CIDR',  
                'Endereço de Rede', 
                'Primeiro Host',  
                'Último Host',  
                'Endereço de Broadcast',  
                'Classe do Endereço',  
                'Número de Sub-redes',  
                'Número total de Hosts por Sub-rede', 
                'Número de Hosts por Sub-rede utilizáveis', 
                'Público/Privado',  
                'Intervalo de IPs de host utilizável',  
            ],
            'Valores': [ #Aqui vai exibir os valores obtidos
                self.enderecoIp,  
                self.mascaraSubrede, 
                self.mascaraParaPrefixo(),  
                str(self.calcularEnderecoRede()),  
                str(self.calcularPrimeiroHost()),  
                str(self.calcularUltimoHost()), 
                str(self.calcularEnderecoBroadcast()),  
                self.classeEndereco,
                self.calcularNumeroSubredes(),  
                self.calcularHostsTotalPorSubrede(), 
                self.calcularHostsUtilizaveisPorSubrede(),
                self.verificarPublicoPrivado(),
                f"{str(self.calcularPrimeiroHost())} até {str(self.calcularUltimoHost())}",
            ]
        }
        
        df = pd.DataFrame(dados)  #Cria um DataFrame pandas com o dicionário dados
        return df
