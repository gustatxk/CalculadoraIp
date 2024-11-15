# Calculadora de IP para IPv4
 Este projeto é uma Calculadora de IP desenvolvida em Python utilizando a programação orientada a objetos (POO). O objetivo do projeto é analisar um endereço IP e sua máscara de sub-rede, fornecendo informações como:
- Endereço de rede
- Primeiro e último host
- Endereço de broadcast
- Classe do IP
- Número de sub-redes
- Hosts por sub-rede
- Se o IP é público ou privado
- Intervalo de IPs disponíveis
Além disso, a aplicação tem uma interface gráfica simples desenvolvida com Streamlit, permitindo que o usuário insira o endereço IP e a máscara de sub-rede para visualizar os cálculos.

# Funcionalidades
- Conversão da máscara de sub-rede para o formato CIDR (ex: /24).
- Cálculos de rede, incluindo:
    Endereço de rede
    Primeiro e último host
    Endereço de broadcast
- Classificação de IP nas classes A, B, C, D e E.
- Cálculo do número de sub-redes e hosts por sub-rede.
- Verificação de IP público ou privado.
- Exibição dos resultados em uma tabela gerada com a biblioteca pandas.

  # Dependências
  Este projeto requer a instalação de algumas bibliotecas. Você pode instalar todas as dependências necessárias utilizando o arquivo requirements.txt.
  Bibliotecas utilizadas:
    - streamlit: Para criar a interface gráfica interativa e fácil de usar.
    - pandas: Para gerar e exibir a tabela de resultados.
    - ipaddress: Para cálculos de redes IPv4 e manipulação de endereços IP (já incluída no Python 3.3 ou superior).

  # Como instalar as dependências
  1. Clone o repositório para sua máquina local:
     'git clone https://github.com/seu-usuario/calculadora-ip.git'
  2. Navegue até a pasta do projeto:
     'cd CalculadoraIp'
  3. Instale as dependências:
     'pip install -r requirements.txt'

  # Como executar
  Após instalar as dependências, você pode executar a aplicação com Streamlit para visualizar a interface gráfica.
  1. Para iniciar a aplicação, use o comando:
     'streamlit run app.py' caso não funcione use 'python -m streamlit run app.py' 
  2. Isso abrirá a interface no seu navegador (geralmente em http://localhost:8501), onde você poderá inserir o endereço IP e a máscara de sub-rede. O sistema calculará e exibirá as informações detalhadas sobre a rede, como endereço de rede, primeiro e último host, endereço de broadcast, entre outros.

 # Estrutura do Projeto
 CalculadoraIp/
 │
 ├── app.py                  # Interface gráfica com Streamlit
 ├── calculadoraip.py         # Lógica de cálculos de IP e geração da tabela
 ├── requirements.txt         # Arquivo de dependências
 └── README.md                # Este arquivo de instruções

calculadoraip.py: 
Este arquivo contém a implementação da Calculadora de IP, utilizando Programação Orientada a Objetos (POO) para realizar cálculos de rede.

app.py:
O arquivo app.py contém a interface do usuário feita com o Streamlit. Ele coleta o IP e a máscara de sub-rede inseridos pelo usuário e chama os métodos da classe CalculadoraIp para exibir os resultados em uma tabela.

requirements.txt:
Este arquivo lista todas as dependências do projeto. Você pode instalá-las facilmente com o comando:
 'pip install -r requirements.txt'

# Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.


