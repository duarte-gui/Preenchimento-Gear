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
driver.get("https://sistema.gear-tecnorise.com:7050/gear/automacao/modulo")
time.sleep(1)

# Carrega os dados do Excel usando pandas
df = pd.read_excel('dispositivos.xlsx')

# Itera sobre as linhas do DataFrame
for index, row in df.iterrows():
    # Adiciona um módulo
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
    campo_tip_modulo = driver.find_element(By.XPATH, '//div[@class="col-md-6"]//label[contains(text(), "Tipo")]/following-sibling::div//input[contains(@id, "react-select-")]')

    # Enviar as teclas para o elemento encontrado
    campo_tip_modulo.send_keys("Control id")
    campo_tip_modulo.send_keys(Keys.TAB)
    campo_tip_modulo.send_keys(Keys.TAB)
            
    time.sleep(1)
    
    # Nome do equipamento
    campo_name_modulo = driver.find_element(By.XPATH, '//*[@id="dsc_equipamento"]')
    campo_name_modulo.send_keys(row['campo_name_modulo'])
    campo_name_modulo.send_keys(Keys.TAB)
    campo_name_modulo.send_keys(Keys.TAB)
    time.sleep(1)

    # Número de série
    campo_serie = driver.find_element(By.XPATH, '//*[@id="mac"]')
    campo_serie.send_keys(row['campo_serie'])
    campo_serie.send_keys(Keys.TAB)
    campo_serie.send_keys(Keys.TAB)
    time.sleep(1)

    # Monitorar
    campo_monitor = driver.find_element(By.XPATH, '//div[@class="col-md-4"]//label[contains(text(), "Monitorar")]/following-sibling::div//input[contains(@id, "react-select-")]')

    # Enviar as teclas para o elemento encontrado
    campo_monitor.send_keys("SIM")
    campo_monitor.send_keys(Keys.TAB)
    campo_monitor.send_keys(Keys.TAB)
    time.sleep(1)

    # IP
    campo_IP = driver.find_element(By.XPATH, '//*[@id="dsc_host"]')
    campo_IP.send_keys(row['campo_IP'])
    campo_IP.send_keys(Keys.TAB)
    time.sleep(1)

    # Porta
    campo_porta = driver.find_element(By.XPATH, '//*[@id="dsc_porta"]')
    campo_porta.send_keys(row['campo_porta'])
    campo_porta.send_keys(Keys.TAB)
    time.sleep(1)

    # Usuário
    campo_user = driver.find_element(By.XPATH, '//*[@id="dsc_login"]')
    campo_user.send_keys("admin")
    campo_user.send_keys(Keys.TAB)
    time.sleep(1)

    # Senha
    campo_passwd = driver.find_element(By.XPATH, '//*[@id="dsc_senha"]')
    campo_passwd.send_keys(row['campo_passwd'])
    campo_passwd.send_keys(Keys.TAB)
    campo_passwd.send_keys(Keys.TAB)
    campo_passwd.send_keys(Keys.TAB)
    campo_passwd.send_keys(Keys.RETURN)
    time.sleep(8)
