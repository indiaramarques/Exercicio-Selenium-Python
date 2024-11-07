from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Mantém o navegador aberto

driver = webdriver.Chrome(options=chrome_options)
driver.get("file:///Users/indiarabreder/Downloads/sample-exercise.html")
driver.find_element(By.NAME, "generate").click()
input = driver.find_element(By.ID, "my-value").text
driver.find_element(By.ID, "input").send_keys(input)
driver.find_element(By.NAME, "button").click()
alert = Alert(driver)
alert.accept()
result = driver.find_element(By.ID, "result").text
mensagem_esperada = result
assert mensagem_esperada == result, f"Erro: Esperado '{mensagem_esperada}', mas encontrado '{result}'"
driver.quit()   
