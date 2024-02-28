# Baba Eletrônica Para Pais Deficientes Auditivos ( BabyCare )
Trabalho de conclusão de curso de Engenharia da Computação, Instituto Mauá de Tecnologia

![LOGO](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/7d08ad6b-0077-4f26-a73d-57623e4b9266)

O projeto consiste em:
- [x] Criação de modelos de aprendizagem para classificação e detecção de choro @NULLBYTE-RGH
- [x] Fazer captura de Som e Imagem do bebê com uma Webcam (Streaming) @NULLBYTE-RGH
- [x] Criar um Barramento de eventos para gerenciar a comunicação entre o serviço de classificação e periféricos @NULLBYTE-RGH
- [x] Criar meios de Autenticação e implementar criptografia @NULLBYTE-RGH
- [x] Fazer comunicação entre bracele e Baba eletrônica @NULLBYTE-RGH
- [x] Criar metodo de configuração da Baba a rede WIFI via bluetooth @NULLBYTE-RGH
- [x] Criação e implementação de um bracelete de uso do bebê para captura de movimentos e comunicação com a central (Intel NUC) @NULLBYTE-RGH
- [x] Criação e implementação de Modulo de controle de iluminação @NULLBYTE-RGH
- [x] Implementar serviços de forma eficiente, visando baixo uso de recursos @NULLBYTE-RGH
- [x] Criação e integração de um relógio inteligente que ligado ao celular via bluetooth recebe notificações e alerta os pais por meio de vibração e ou alerta visual @NULLBYTE-RGH
- [x] Criação de modelos de braceletes para impressao 3D para o pai e para o bebe @NULLBYTE-RGH
- [x] Criação de APP para comunicação com a baba eletrônica, possibilitando a visualização do bebê em tempo real bem como acesso a logs de choro @NULLBYTE-RGH @Morfogon

Status do projeto:

![](https://geps.dev/progress/100?dangerColor=800000&warningColor=ff9900&successColor=006600)

-----------------------------------------------------------------------------------------------------------------------------------------------

![ConjuntoBABA](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/e46ebc9c-1e64-436a-8965-7629d726ed42)

-----------------------------------------------------------------------------------------------------------------------------------------------

## ✔️ Técnicas, tecnologias e Recursos utilizados

- ``Python 3.10``
- ``Thony 3.3.13``
- ``Flask 2.2.3``
- ``Requests 2.28.2``
- ``Socket``
- ``Json``
- ``Numpy 1.23.5``
- ``Pyaudio 0.2.13``
- ``Time``
- ``Librosa 0.10.0.post2``
- ``Sklearn``
- ``Pickle``
- ``Datetime``
- ``Cv2 4.7.0.72``
- ``PIL``
- ``Io``
- ``Threading``
- ``Serial``
- ``RPi``
- ``Tensorflow 2.8.0``
- ``Soundfile 0.12.1``
- ``Machine``
- ``Imu``
- ``Math``
- ``matplotlib 3.7.1``
- ``os``
- ``Pydub 0.25.1``
- ``Scipy 1.10.1``
- ``Noisereduce``
- ``Comunicação UART``
- ``Comunicação I2C``
- ``Postman 10.13.0``
- ``Openssl``
- ``PyCharm Professional 231.8770.66, built on April 27, 2023`` ❤️
- ``DataSpell 231.8770.72, built on May 3, 2023`` ❤️

## 💻 Hardware para Treinamento e Desenvolvimento

- ``NVIDIA GeForce RTX 2060``
- ``Intel Core i7-8750H 2.20 GHz``
- ``16 GB RAM``

## Central da Baba
- ``Intel nuc dn2820fykh``
  ![image](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/6f07fb3d-7888-414c-95e2-204e3261b381)
-----------------------------------------------------------------------------------------------------------------------------------------------
## Diagrama do projeto

![Baba eletronicav3 drawio](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/7d587a2c-ba17-4efa-91f0-1eff974211ac)

![VISAO COMPLETA BABA](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/31a9ce14-5ccb-4c1c-8fb6-43752564e8a6)

## Modelos Testados:
#### Modelos clássicos, apresentaram uma boa precisão porém para a quantidade de dados disponíveis nos Datasets não foram eficientes
### SVC: 
![SVC](https://user-images.githubusercontent.com/79452652/229323958-1179f42a-b6ea-4bda-816b-1142be0c3871.png)
### RandomForest:
![Random](https://user-images.githubusercontent.com/79452652/229323982-d48644b7-b291-4772-99a9-cc61e5b4923f.png)
### DecisionTree:
![Decision](https://user-images.githubusercontent.com/79452652/229324015-5e20694f-53c6-4711-af0e-0ad549f13d7e.png)

-----------------------------------------------------------------------------------------------------------------------------------------------

#### Classificador MLP
#### 100 Neurônios para classificação de Choro, Silencio, Barulho e Risadas:
![100Camadas](https://user-images.githubusercontent.com/79452652/229324097-402b247e-876a-49e7-a42f-ebabcce5a87c.png)
#### 600 Neurônios para classificação de Cólica, Arroto, Desconforto, Fome e cansaço:
![600Camadas](https://user-images.githubusercontent.com/79452652/229324105-898f83d6-9817-4476-ae4e-096016865c0d.png)
#### 100 Neurônios com audios passados pelo microfone (Modelo mais recente):
![output](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/1753584b-e42d-4059-b754-871a38748235)
#### A precisão máxima é atingida em vários momentos com diferentes features e com testes foi verificado que apesar de com 1 feature a precisão ser de 84%, com o uso de 26 Features, que também resulta em uma precisão de 84%, o modelo se sai melhor.
##### A classe CryingV2 utilizada no Neural.ipynb nada mais é do que uma pasta contendo ['belly_pain','discomfort','hungry','tired', 'Crying']
##### E o aprendizado foi feito em um ambiente utilizando Python versão 3.10
#### Sendo assim os modelos que serão utilizados em testes sem ruídos e estao disponiveis na pasta /Modelos são:
#### [x] modelo_Apenas_ChoroV4.pkl -> 95%
#### [x] modelo_Tipos_De_ChoroV4.pkl -> 84%
#### [x] Novo_Modelo_MLP_NormalizadoV3.pkl ->94.64%
##### É possível que o MLP tenha obtido melhores resultados porque ele é capaz de extrair mais informações relevantes dos dados de áudio e generalizar melhor para novos dados. Como mencionado anteriormente, os outros modelos podem ter limitações em termos de capacidade de lidar com dados mais complexos e não lineares.

##### Além disso, o fato de que o MLP teve um desempenho melhor no teste real pode ser uma indicação de que ele não sofreu tanto de overfitting quanto os outros modelos. O overfitting ocorre quando o modelo é ajustado demais aos dados de treinamento e não generaliza bem para novos dados. Se o MLP generalizou melhor para novos dados, é possível que ele tenha sofrido menos de overfitting do que os outros modelos.

-----------------------------------------------------------------------------------------------------------------------------------------------
 
### Problemas na captura de Áudio via Microfone:
#### Ao capturar o mesmo áudio que foi utilizado no treinamento via microfone foi observado uma diferença gritante:
### Espectrograma:
#### Louise é o audio original do dataset:
![Espectrograma-Louise](https://user-images.githubusercontent.com/79452652/229637672-e9ca86f7-2c7a-49a9-b076-b0e680d6794c.png)
#### Som do Bebe é o audio da Louise do dataset regravado a partir do microfone do computador:
![Espectrograma Captura_WebCam](https://user-images.githubusercontent.com/79452652/229637756-b76c3b9d-d239-462b-a75b-bc9a67d6a4cc.png)

### Gráfico de Frequência:
#### Louise é o audio original do dataset:
![Frequencia_Louise](https://user-images.githubusercontent.com/79452652/229637981-59fa82f9-a12c-4736-8a50-69c95b9749d7.png)
#### Som do Bebe é o audio da Louise do dataset regravado a partir do microfone do computador:
![Frequencia_WebCam](https://user-images.githubusercontent.com/79452652/229637790-4b92a990-719d-4ba7-8417-e1e74add95cb.png)

#### Foi testado o Treinamento do MLP com áudios gravados pelo Microfone, ao invés do uso do Dataset original, esses áudios do microfone nada mais são do que os áudios do dataset original, porém passados pelo Microfone que será usado para captura do áudio do Bebê, assim eliminando a interferência do Transdutor no reconhecimento.
#### Foi testado com 5 áudios de cada categoria e foi verificado que se obteve uma precisão de acerto de 4 em 5 dessa forma. Isso com 26 MFCCs e 100 Neurônios na camada. E apenas 20 dados para aprendizado sendo que dos 20, 20 % foram utilizados na validação resultando em 75 % de precisão. 
(Modelo: modelo_Tipos_De_ChoroVMicrofone.pkl)

### Áudios comparados (Original) e mesmo áudio, porém com influência do transdutor e com menor amplitude de dB:

#### Espectrogramas dessa vez com taxa de amostragem correta (Pois nos datasets baixados existem vários áudios fora do padrão 22k, isso foi corrigido junto ao tempo de áudio variado, agora limitados a 5 segundo e salvos em pastas com V2 no final do nome, dentro da pasta datasets) e com o microfone de um Galaxy s20+ ao invés do microfone da webcam:

![Espectrograma Audio Original](https://user-images.githubusercontent.com/79452652/230244042-4b1c2bfc-fce6-4756-a392-361d3a335fb4.png)

![Espectrograma Audio passado pelo Microfone](https://user-images.githubusercontent.com/79452652/230244051-11335f38-e909-4493-afca-525563bdf34b.png)

### Influência do dB na normalização do MFCC (Muito baixa a quase nula) assim comprovando que o volume não influencia na extração de fatures para criação do modelo/classificação:
##### Por camadas internas, entenda Neuronios, pois foi feito com apenas 1 camada, tirando a SoftMax
![MFCC1](https://user-images.githubusercontent.com/79452652/230245027-b7db51e4-dbf1-491e-b15c-298d1a2904d0.png)


![MFCC2](https://user-images.githubusercontent.com/79452652/230245039-cbcb2345-ef11-401f-94e6-07e4732836e8.png)


![MFCC3](https://user-images.githubusercontent.com/79452652/230245052-2a1e93a8-129b-48be-a6e0-5abdfdffba39.png)


![MFCC4](https://user-images.githubusercontent.com/79452652/230245059-2d31432c-5134-46b5-abff-37ac7f1c2607.png)

#### Novos datasets foram criados a partir dos datasets existentes, porém os áudios foram tocados em caixas de som que foram capturadas por uma webcam com microfone integrado, esses áudios então foram segmentados e salvos em suas respectivas classes, que foram utilizadas para treinamento do novo modelo e mais preciso de todos até o momento, com 95.38% de precisão, o modelo (modelo_Tipos_De_ChoroVMicrofone.pkl) faz uso de 90 mfcc's, 300 neurônios e 30% do dataset para validação. (dataset utilizado foi o Dataset_Microfone, onde todos os áudios limpos, em questão de samples e duração, foram tocados por uma caixa de som e capturados pelo microfone da webcam)

### O modelo mais recente:

#### O modelo atual 
[Novo_Modelo_MLP_NormalizadoV3.pkl](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Modelos/Novo_Modelo_MLP_NormalizadoV3.pkl) junto ao 
[Scaler](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Modelos/scalers_Novo_Modelo_MLP_NormalizadoV3.pkl)
faz uso de 1 camada interna com apenas 40 Neurônios e tem como entrada da rede 100 mfccs sendo o modelo mais leve e menos complexo ate o momento, atingindo uma precisao de 94.64%. Ele foi treinado com um novo dataset, que na verdade sao usados os mesmo audios que tinham no V2, porem eles foram tocados atraves de uma caixa de som nova e mais robusta, e alem disso foi feita uma limpeza manual em cada audio, removendo audios ruins ou inconsistentes com a classe. Junto a isso com a uma limpeza adicional nos audios, resultou em uma diminuição do Dataset, resultando em 76 audios de choro, 38 de risada e 72 de barulhos externos, visto um certo desbalanceamento foi tantado fazer ajustes ao modelo aplicando diferentes pesos as clases e fazendo dados sinteticos, e  resultado final foi :

![Metricas Classificador](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/62ac5f01-3c93-4a2d-b967-e197cd986869)


#### As especificações da nova caixa de som é : modelo: ep310, rms: 5w, resposta a frequencia: 200hz - 18 khz, sensibilidade de entrada: 350 mv, voltagem: 5v dc, conexão: p2
![image](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/0fee7c38-8723-44e9-bc11-3dc9bfdad1dd)
#### Os audios foram reproduzidos com o som maximo da caixa de som, porem com o nivel 80 % do windows, e a distancia entre a webcan e a caixa de som é de cerca de 1 metro
-----------------------------------------------------------------------------------------------------------------------------------------------

## Bracelete do Bebê
#### Componentes:
##### [X] RP2040
##### [X] HC05
##### [X] GY-521

![Schematic_Braceletes_2023-05-07](https://user-images.githubusercontent.com/79452652/236659943-06a6c9fd-1885-46ea-8e11-d2c3af3c8430.png)

[Schematic_Braceletes_2023-05-07.pdf](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/files/11414012/Schematic_Braceletes_2023-05-07.pdf)


![20230507_024705](https://user-images.githubusercontent.com/79452652/236660184-9f637797-effc-456f-886f-73b34f7a8ef3.jpg)
![20230507_024719](https://user-images.githubusercontent.com/79452652/236660185-396e8231-055a-4ce1-a304-7e582b9e6548.jpg)
![20230507_024641](https://user-images.githubusercontent.com/79452652/236660186-10f37fd1-2ff8-4fbd-b65c-1b289e9078fc.jpg)

-----------------------------------------------------------------------------------------------------------------------------------------------

## Bracelete dos Pais
#### Componentes:
##### [X] RP2040
##### [X] HC05
##### [X] Motor Vibrador 3v

![Schematic_Bracelete PAI_2023-05-12](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/1fb97f53-3dd6-4d68-89f7-043d6df2f9ff)

-----------------------------------------------------------------------------------------------------------------------------------------------
## Modulo de Iluminação

![Schematic_Luz_2023-09-06](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/65935636-0d7a-4391-a9e0-b1ee5dcd6adb)

-----------------------------------------------------------------------------------------------------------------------------------------------

## 🔨 Funcionalidades: [Barramento de eventos](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/tree/main/Barramento%20de%20eventos)
#### Ao [iniciar](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Fluxograma/Inicializa%C3%A7%C3%A3o.pdf) o dispositivo o [serviço de inicialização](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Barramento%20de%20eventos/servi%C3%A7os/Servico_de_Inicializacao.py) entra em execução, se for a primeira inicialização, o usuario deverá, parear seu celular com a Raspberry pi 3 e segurar o botão nela contido por X segundos, sendo assim o serviço: [Serviço_de_conexao_wifi](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Barramento%20de%20eventos/servi%C3%A7os/Servico_Rede_WIFI.py) entrara em funcionamento, a partir desse momento o usuário por meio do app deverá informar o SSID(nome) da rede [wifi](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Fluxograma/Rede%20WIFI.pdf) e sua senha, quando conectado corretamente, é retornado o IP da Baba eletronica na rede local e é solicitado a criação de pelo menos um usuario e uma senha, tendo a opção da criação de multiplas contas. Ao finalizar, o serviço [Barramento](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Barramento%20de%20eventos/Barramento.py) entrara em execução, juntamente aos serviços : [Bracelete](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Barramento%20de%20eventos/Bracelete.py), [Camera](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Barramento%20de%20eventos/Camera.py), [Microfone](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Barramento%20de%20eventos/Microfone.py) e [iluminacao](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Barramento%20de%20eventos/iluminacao.py)
##### Exemplo de saida quando a Baba esta sendo configurada pelo [Serviço_de_conexao_wifi](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Barramento%20de%20eventos/servi%C3%A7os/Servi%C3%A7o_de_conexao_wifi.py), essa saida foi gerada com uso do app [Serial Bluetooth Terminal](https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal&pli=1) para Android, fazendo as requisições que serao feitas pelo APP:
![Screenshot_20230508_000623_Serial Bluetooth Terminal](https://user-images.githubusercontent.com/79452652/236725361-afcc1b19-0861-4c39-8b8e-2f947ae8eb28.jpg)
-----------------------------------------------------------------------------------------------------------------------------------------------
## [Rotas](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Fluxograma/Barramento.pdf)

##### O Barramento em si [Barramento.py](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Barramento%20de%20eventos/Barramento.py) tem diversas rotas e roda na porta padrão 5000 (Atualmente tudo funciona por meio de HTTP, futuramente sera implementado HTTPS, para uma maior segurança da baba como um todo):
###### Para todas as requisições (Exceto /camera), deve ser fornecido tanto o usuario como a senha : (usuario&senha) em formato JSON no corpo da requisição como : 
##### {
##### "usuario":"user1",
##### "senha":"pass1"
##### }
##### ``Caso tenha um metodo associado a rota (?tipo=X)``
##### Para criar o certificado e par de chaves para usar HTTPS TLS use o OpenSSL: 
##### ``openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`` 
##### Este comando criará um certificado autoassinado com uma chave RSA de 4096 bits e uma validade de 365 dias
###### As requisições podem ser consultadas [aqui](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Requisi%C3%A7%C3%B5es/Barramento.postman_collection.json)
-----------------------------------------------------------------------------------------------------------------------------------------------
### '[/](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Fluxograma/Barramento.pdf)'
###### Deve ser acessada via método POST, essa rota serve para escrever o celular como Observer dos eventos do bebê, para evitar excessivo tráfego na rede. Ao momento que o celular sabe o endereço da baba na rede, ele envia essa requisição ao celular e o barramento se encarrega de avisar o celular caso tenha ocorrido alguma mudança na movimentação do bebê ou caso tenha ocorrido choro. assim o [celular](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Barramento%20de%20eventos/Simular_Celular.py) como simulado, pode tomar a decisão de alertar o usuário. Mais detalhadamente, essa rota ao receber a requisição extrai o IP do celular na rede, bem como a porta em que o celular escolheu para ouvir notificações, essa porta é enviada pelo celular no corpo da requisição, essa porta é de escolha do celular, podendo ser modificada caso necessário, em tempo de Execução.
![image](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/7a589f67-842a-40cf-9b56-e7d45701c1ce)
![image](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/d10818a0-2d8a-4cb7-b021-31437dce7746)
-----------------------------------------------------------------------------------------------------------------------------------------------
### '/evento'
###### É uma rota de método POST na qual ``o usuário não deve acessar`` (para isso é feita uma checagem de IP na hora que o barramento recebe a requisição, assegurando que o IP do cliente é da rede de loopback, assim só permitindo que serviços locais, iniciem requisiçoes a essa rota), essa rota é de acesso dos serviços em execução, ao ocorrer alguma mudança de estado dos servicos execução,o serviço alerta o barramento por meio desta rota, a qual se encarrega de notificar o celular, que se inscreveu como Observer na rota '/'. Mais detalhadamente: os serviços bracelete e microfone que fazem acesso a essa rota, fazendo uma requisição do tipo: 'http://127.0.0.1:5000/evento?tipo=1' o argumento (?tipo=X) é o que determina de onde o alerta surgiu, sendo tipo = 1 Evento de Movimentação, tipo = 2 Evento do Microfone.
-----------------------------------------------------------------------------------------------------------------------------------------------
### '/[camera](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Fluxograma/Camera.pdf)'
###### Essa rota faz uso do método GET e caso a requisição seja feita com o argumento tipo (?tipo=1) o retorno é uma imagem tirada pela webcam do bebê, caso seja diferente de (?tipo=1) como (?tipo=2 etc) o barramento entende a requisição como sendo de streaming de vídeo.
![Requisição](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/f7d28ac4-2a27-4be7-aaea-31779c29909d)
-----------------------------------------------------------------------------------------------------------------------------------------------
### '/[microfone](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Fluxograma/Microfone.pdf)'
###### Faz uso do método POST e possui 2 métodos de acesso, (?tipo=1) retorna o que o modelo está detectando no momento da requisição, como (choro, silencio, barulho ou risada), podendo ter um retorno vazio caso o modelo não esteja detectando nada no momento e o método de acesso (?tipo=2) que retorna o LOG de todas as detecções já realizada até o momento, contendo o que foi detectado, hora e minuto, bem como data, tudo em formato JSON.
![RequisiçãoMicrofone](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/3c190435-3cb5-4729-89b9-48f2f61fc2d2)
-----------------------------------------------------------------------------------------------------------------------------------------------
### '/[iluminacao](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Fluxograma/Ilumina%C3%A7%C3%A3o.pdf)'
###### Usa o método POST e possui 3 tipos de operações: (?tipo=1) liga a luz do quarto do bebê, (?tipo=2) desliga a luz do quarto do bebê e (?tipo=3) retorna o status da luz do quarto do bebê, sendo acesa ou apagada.
-----------------------------------------------------------------------------------------------------------------------------------------------
### '/[bracelete](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/blob/main/Fluxograma/Servi%C3%A7o%20Bracelete.pdf)'
###### Faz uso do método POST e possui 2 modos de operação: (?tipo=1) retorna o status do bebê, como se movimentando ou não, hora, dia, minuto e temperatura do quarto. Caso não ele é um valor JSON vazio e (?tipo=2) retorna os LOGS de movimentações do bebê.
-----------------------------------------------------------------------------------------------------------------------------------------------

## APP:

![APPtela1](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/5deef23c-e3fc-44aa-ace2-22f5165d7dc6)
![APPtela2](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/d6b30460-807d-4b62-985d-d827e8b6336e)
![APPtela3](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/a615fcf1-3892-4c21-84dd-40503ad0cdde)
![BraceleteBABA](https://github.com/NULLBYTE-RGH/Baba-Eletronica-Para-Pais-Deficientes-Auditivos/assets/79452652/39ea8ad5-48c0-46e9-9d35-85a3bf92d9b3)


