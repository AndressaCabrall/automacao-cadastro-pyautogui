import pyautogui

import time

pyautogui.PAUSE = 1

# Passo 01 -Entrar no sistema da empresa
   
pyautogui.press("win")         
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

# Passo 02- Fazer o login no site com usuario e senha   1

pyautogui.click(608, 465)
pyautogui.write("cabrallnegociosonline@gmail.com")

pyautogui.press("tab")
pyautogui.write("pastadedente")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 03 - Importar a base de dados

import pandas

tabela = pandas.read_csv("Python PowerUP/produtos.csv")

print(tabela)

for linha in tabela.index:

    pyautogui.click(604, 313)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(int(tabela.loc[linha, "categoria"]))
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo =str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"]) 
    if obs != "nan":
             
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.press("home")





















    

    
       

   
    
   #pyautogui.press("enter")

    #pyautogui.press("home")


# Passo 04 -Cadastrar os Produtos



    
   









 
