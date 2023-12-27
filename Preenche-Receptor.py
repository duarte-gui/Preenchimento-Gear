import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o navegador (por exemplo, o Chrome)
driver = webdriver.Chrome()

# Abre a página web desejada
driver.get("https://sistema.gear-tecnorise.com:7050")

# Encontra os campos de usuário e senha e preenche-os
usuario = "Usuário-Gear"
senha = "Senha-Gear"

campo_usuario = driver.find_element(By.ID, 'usuario')
campo_senha = driver.find_element(By.ID, 'password')

campo_usuario.send_keys(usuario)
campo_senha.send_keys(senha)
campo_senha.send_keys(Keys.RETURN)

# Aguarda um curto período para garantir que o processo de login seja concluído
time.sleep(5)

# Encontra o elemento que representa o link
driver.get("https://sistema.gear-tecnorise.com:7050/gear/automacao/receptor")
time.sleep(1)

# Carrega os dados do Excel usando pandas
df = pd.read_excel('Receptores.xlsx')

# Itera sobre as linhas do DataFrame
for index, row in df.iterrows():
    # Adiciona um módulo
    print (row['campo_condominio'], row['campo_name_modulo'])
    botao_add = driver.find_element(By.XPATH, "//button[@type='button']")
    botao_add.click()
    time.sleep(5)

    # Encontrar o elemento na página usando o XPath
    campo_condominio = driver.find_element(By.XPATH, '//div[@class="col-md-6"]//label[contains(text(), "Condom")]/following-sibling::div//input[contains(@id, "react-select-")]')

    # Enviar as teclas para o elemento encontrado
    campo_condominio.send_keys(row['campo_condominio'])
    campo_condominio.send_keys(Keys.TAB)
    campo_condominio.send_keys(Keys.TAB)
            
    time.sleep(1)

    # Encontrar o elemento na página usando o XPath
    campo_name_modulo = driver.find_element(By.XPATH, '//div[@class="col-md-6"]//label[contains(text(), "M")]/following-sibling::div//input[contains(@id, "react-select-")]')

    # Enviar as teclas para o elemento encontrado
    campo_name_modulo.send_keys(row['campo_name_modulo'])
    campo_name_modulo.send_keys(Keys.TAB)
    campo_name_modulo.send_keys(Keys.TAB)
            
    time.sleep(1)
    
    # Tipo do receptor
    campo_tipo_modulo = driver.find_element(By.XPATH, '//div[@class="col-md-6"]//label[contains(text(), "Tip")]/following-sibling::div//input[contains(@id, "react-select-")]')
    campo_tipo_modulo.send_keys(row['campo_tipo_modulo'])
    campo_tipo_modulo.send_keys(Keys.TAB)
    campo_tipo_modulo.send_keys(Keys.TAB)
    time.sleep(1)

    # Número de série
    campo_serie = driver.find_element(By.XPATH, '//div[@class="col-md-6"]//label[contains(text(), "Núm")]/following-sibling::div//input[contains(@id, "react-select-")]')
    campo_serie.send_keys("1")
    campo_serie.send_keys(Keys.TAB)
    campo_serie.send_keys(Keys.TAB)
    time.sleep(1)

    # Monitorar
    campo_name_receptor = driver.find_element(By.XPATH, '//*[@id="dsc_receptor"]')

    # Enviar as teclas para o elemento encontrado
    campo_name_receptor.send_keys(row['campo_name_modulo'])
    campo_name_receptor.send_keys(Keys.TAB)
    campo_name_receptor.send_keys(Keys.TAB)
    campo_name_receptor.send_keys(Keys.RETURN)
    time.sleep(1)

    
