Automação de Cadastro de Produtos
Este script automatiza o processo de cadastro de produtos em um sistema web utilizando a biblioteca pyautogui. Ele realiza as seguintes etapas:

Passo a Passo:
Abrir o navegador e acessar o sistema
O script abre o navegador Chrome e acessa o link do sistema da empresa.

Realizar login
Insere o e-mail e senha nos campos de login e clica no botão "Entrar".

Importar a base de dados
Utiliza a biblioteca pandas para carregar os dados de produtos a partir do arquivo CSV localizado em Python PowerUP/produtos.csv.

Cadastrar os produtos
Para cada linha da tabela de produtos:

Preenche os campos de código, marca, tipo, categoria, preço unitário, custo e observações (se houver).
Clica no botão "Enviar" para cadastrar o produto.
Rola a tela para o início para preparar o próximo cadastro.

Requisitos:

Bibliotecas: pyautogui, pandas, time.
Arquivo CSV: Certifique-se de que o arquivo produtos.csv está no diretório correto e contém os dados necessários.

Observações:

As coordenadas de clique (pyautogui.click) e outros comandos dependem da resolução da tela e da posição dos elementos no sistema. Ajuste conforme necessário.
O tempo de pausa (pyautogui.PAUSE) pode ser configurado para garantir que o sistema tenha tempo suficiente para carregar os elementos.
