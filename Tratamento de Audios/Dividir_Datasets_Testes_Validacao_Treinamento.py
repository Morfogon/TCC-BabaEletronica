import os
import random
import shutil

caminho_dataset = 'laugh/'
treinamento_dir = 'treinamento/'
validacao_dir = 'validacao/'
teste_dir = 'teste/'
porcentagem_treinamento = 0.7
porcentagem_validacao = 0.15
porcentagem_teste = 0.15

# Obtém o diretório atual do script
diretorio_atual = os.getcwd()
print(f"Diretório atual: {diretorio_atual}")

# Cria o diretório de treinamento na raiz do diretório atual
treinamento_dir_abs = os.path.join(diretorio_atual, treinamento_dir)
os.makedirs(treinamento_dir_abs, exist_ok=True)

# Obtém a lista de arquivos na pasta raiz do dataset
files = os.listdir(caminho_dataset)

# Conta o número de imagens para determinar a quantidade de imagens em cada conjunto
n_imagens = len(files)
n_treinamento = int(n_imagens * porcentagem_treinamento)
n_validacao = int(n_imagens * porcentagem_validacao)
n_teste = n_imagens - n_treinamento - n_validacao

# Embaralha a lista de arquivos para selecionar aleatoriamente as imagens para cada conjunto
random.shuffle(files)

# Copia as imagens para cada conjunto, respeitando a proporção de cada um
for i, file in enumerate(files):
    if i < n_treinamento:
        dst_dir = treinamento_dir_abs
    elif i < n_treinamento + n_validacao:
        dst_dir = os.path.join(caminho_dataset, validacao_dir)
        os.makedirs(dst_dir, exist_ok=True)
    else:
        dst_dir = os.path.join(caminho_dataset, teste_dir)
        os.makedirs(dst_dir, exist_ok=True)
    shutil.copy(os.path.join(caminho_dataset, file), os.path.join(dst_dir, file))
