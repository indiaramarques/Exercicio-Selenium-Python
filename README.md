# Utilizando Selenium para automação de testes com Python


Este script utiliza o Selenium WebDriver para automatizar a interação com uma página HTML de exemplo e verificar o funcionamento dos elementos da interface de usuário. O teste inclui a verificação de elementos visíveis, o preenchimento de campos de entrada e a confirmação de alertas.

# Pré-requisitos

1.	Python (versão 3.7 ou superior)
2.	Selenium WebDriver: instale o Selenium com o comando:
•	pip install selenium
3.	ChromeDriver: para controlar o navegador Chrome, baixe e instale o ChromeDriver. Certifique-se de que o chromedriver está no seu PATH ou no mesmo diretório deste script.

# Estrutura do Código

Importações

•	Selenium: utilizado para controle do navegador e interação com elementos da página.

•	WebDriverWait e Expected Conditions: usados para espera explícita de elementos na página.

•	Alert: utilizado para lidar com alertas JavaScript.

# Funções Principais do Script

1.	Configuração do ChromeDriver:
•	Define as opções do Chrome para manter o navegador aberto após a execução.
2.	Navegação para a Página de Exercício:
•	Carrega uma página HTML local sample-exercise.html para teste.
3.	Interação com Elementos da Página:
•	Encontra o botão "generate" e clica nele.
•	Espera que o elemento com o ID my-value fique visível e obtém seu valor.
•	Insere o valor gerado em um campo de entrada.
•	Confirma a ação clicando em outro botão e interage com o alerta exibido.
4.	Validação do Resultado:
•	Verifica se o texto gerado é igual ao texto do resultado.
•	Gera uma mensagem de erro caso os valores não coincidam.
5.	Encerramento do Script:
•	Pausa o script por 3 segundos e fecha o navegador.

# Como Executar o Script

1.	Coloque a página sample-exercise.html no diretório page dentro do diretório de trabalho atual.
2.	Execute o script com o comando:
•	python test.py

O navegador abrirá a página e executará o teste. Após a execução, o navegador será fechado automaticamente.

# Configuração do ChromeDriver e abertura do navegador

chrome_options = Options()


chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)


