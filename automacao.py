# Importando as bibliotecas
import pyautogui
import pandas as pd
import time

# Importando a base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Tempo de espera entre os comandos
pyautogui.PAUSE = 1.0

# Abrindo o navegador e entrando no link
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=171, y=65)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(6)

# Fazendo login no sitema
pyautogui.click(x=428, y=377)
pyautogui.write("pauloautomacaoteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("testeautomacao")       
pyautogui.click(x=685, y=521)
time.sleep(6)

#cadastrando os produtos
for linha in tabela.index:
    pyautogui.click(x=411, y=258) # Clicando no primeiro campo do formulario
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"] # Atribuindo valor a variavel
    # Verificando se a coluna "obs" tem informação, se não tiver, nao preenche
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("enter") # Aperta o botão de enviar e cadastra o produto
    pyautogui.scroll(5000)
    # Vai prepetir o processo até cadstrar todos os produtos   
    