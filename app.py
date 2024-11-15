#Uso a biblioteca streamlit para a interface
import streamlit as st #Importando todas as funções da biblioteca streamlit
from calculadoraip import CalculadoraIp  #Importando a classe CalculadoraIp de calculadora_ip.py

def main():
    st.title("Calculadora Ip para IPV4") #Título da página
    st.write("A calculadora IP analisa o endereço IP e sua máscara, mostrando informações como o endereço de rede, converte a máscara para o formato CIDR, primeiro e último host, endereço de broadcast, classe do IP, número de sub-redes, hosts por sub-rede, se o IP é público ou privado e exibe o intervalo de IPs disponíveis.") #Pequena descrição das funções
    enderecoIp = st.text_input("Digite o endereço IP (Ex: 192.168.0.1):")  #Campo do ip
    mascaraSubrede = st.text_input("Digite a máscara de sub-rede (Ex: 255.255.255.0):") #Campo da máscara
    
    if st.button("Calcular"): #Botão que chama a classe "CalculadoraIp"
        if enderecoIp and mascaraSubrede:
            try:
                calculadora = CalculadoraIp(enderecoIp, mascaraSubrede)
                tabela = calculadora.gerarTabela()
                st.write("Detalhes do Cálculo do IP:")
                st.dataframe(tabela, use_container_width=True, hide_index=True)
            except ValueError as e:
                st.error(f"Erro: {e}")
        else:
            st.warning("Por favor, insira tanto o endereço IP quanto a máscara de sub-rede.")

if __name__ == "__main__":
    main()
