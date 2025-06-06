import pyautogui

import time

pyautogui.PAUSE = 1

# Passo 01 -Entrar no sistema da empresa
#abrir o chome

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

# Passo 02- Fazer o login com usuário e senha e botão de entrar

pyautogui.click(582,507)
pyautogui.write("cabrallnegociosonline@gmail.com")

pyautogui.press("tab")
pyautogui.write("pastadedente")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 03 - Importar a base de dados

import pandas

tabela = pandas.read_csv("Python PowerUP/produtos.csv")

# Passo 04 -Cadastrar os Produtos

for linha in tabela.index:


    pyautogui.click(602, 358)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    
    pyautogui.press("tab")  
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
   
    pyautogui.press("tab")  
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)


    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") 
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
              
        pyautogui.write(obs)

    time.sleep(1)

# Clica duas vezes diretamente no botão Enviar, nas coordenadas certas

    pyautogui.doubleClick(863, 667)
    pyautogui.press("enter")

# voltar ao inicio da tela
    pyautogui.scroll(10000)









 
