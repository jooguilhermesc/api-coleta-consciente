# api-coleta-consciente
API utilizada no webapp "Coleta Consciente" que visa disponibilizar uma plataforma onde as pessoas possam consultar os pontos de descarte de resíduos no intuito de contribuir para o desenvolvimento de cidades mais sustentáveis.

# Como utilizar a API

A API pode ser acessada a partir do seguinte endereço: https://coleta-consciente.herokuapp.com/recycle/

A API é estruturada da seguinte forma:

"id_recycle_point": Identificado unitário gerado automaticamente de maneira aleatória,
"category_recycle_point": Tipo do ponto de entrega (Ponto de Entrega Voluntário, Cooperativa, ONG, Empresa Especializada, etc, etc...),
"name_recycle_point": Nome do local de entrega (ou apelido no caso dos PEVs),
"end_recycle_point": Endereço completo do local onde fica o ponto de coleta,
"latitude": Coordenada geográfica da latitude referente ao ponto de coleta, no Brasil a latitude varia de +05° 16'19" (ponto mais ao norte) a -60° 12'45" (ponto mais ao sul),
"longitude": Coordenada geográfica da longitude referente ao ponto de coleta, no Brasil a longitude varia de -34° 47'34" (ponto mais oriental) a -73° 59'26" (ponto mais ocidental),
"category_recycle_procedure": Tipo de resíduo que o local recebe (Todo tipo de lixo seco, lixo eletrônico, papelão, plástico, remédios, óleos, etc...),
"contact_recycle_point": Informações de contato sobre o local,
"info_recycle_point": Informações gerais sobre o local,
"created_at": Data de registro desse ponto na API
