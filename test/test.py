import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Obtém o caminho absoluto do diretório onde o arquivo atual está localizado (__file__).
PROJECTROOT = os.path.dirname(os.path.abspath(__file__))

# Obtém o diretório pai de PROJECTROOT, que é essencialmente o diretório "base" ou "raiz" do projeto,
BASE_DIR = os.path.dirname(PROJECTROOT)

# Cria uma instância de `Options`, que permite configurar opções para o navegador Chrome.
chrome_options = Options()

# Adiciona uma opção experimental para o Chrome que mantém o navegador aberto após a execução do script Selenium.
chrome_options.add_experimental_option("detach", True)  

# Inicializa uma nova instância do navegador Chrome, aplicando as opções definidas em chrome_options.
driver = webdriver.Chrome(options=chrome_options)

# Abre um arquivo HTML local no navegador, utilizando o caminho completo para `sample-exercise.html`, 
driver.get(f"file://{BASE_DIR}/sample-exercise.html")

# Encontra o elemento pelo nome 'generate' e clica nele
driver.find_element(By.NAME, "generate").click() 

# Cria uma espera explícita
wait = WebDriverWait(driver, 10)

# Aguarda até que o elemento com o ID 'my-value' esteja visível, ou por até 10 segundos
generated_text = wait.until(EC.visibility_of_element_located((By.ID, 'my-value')))

# Localiza o elemento na página usando seu atributo ID "input" e o armazena na variável 'input'.
input = driver.find_element(By.ID, "input")
input.clear()

# Insere o texto contido em 'generated_text.text' no campo de entrada (que foi localizado anteriormente).   
input.send_keys(generated_text.text)

#Localiza o botão na página através de seu atributo NAME "button" e realiza um clique nesse botão.
driver.find_element(By.NAME, "button").click()
alert = Alert(driver) #Cria uma instância de `Alert`, que representa uma janela de alerta (popup) gerada no navegador.
alert.accept() # Clica no botão "OK" do alerta, fechando a janela.

# Localiza o elemento com ID "result" e armazena o texto contido nesse elemento na variável 'result'.
result = driver.find_element(By.ID, "result").text

# Armazena o valor de 'result' na variável 'mensagem_esperada' para comparação ou uso futuro.
mensagem_esperada = result  

# Compara se o texto gerado é igual ao resultado esperado caso não seja gera uma mensagem de erro
assert mensagem_esperada == result, f"Erro: Esperado '{mensagem_esperada}', mas encontrado '{result}'"

# Pausa o script por 3 segundos para ver o resultado
sleep(3)

# Fecha o navegador
driver.quit()