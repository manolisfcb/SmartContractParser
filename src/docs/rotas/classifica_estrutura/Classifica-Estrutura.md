# Documentação do Endpoint ClasificaEstruturaParagrafos

O endpoint **ClasificaEstruturaParagrafos** é responsável por classificar a estrutura de parágrafos fornecidos em um JSON através do método HTTP GET. Ele utiliza um modelo de classificação previamente treinado para realizar as previsões.

## URL

GET /clasifica_estrutura_paragrafos


## Parâmetros da Solicitação

O endpoint espera receber uma solicitação com um corpo JSON contendo o seguinte parâmetro:

- `paragrafos`: Uma lista de strings representando os parágrafos cuja estrutura será classificada.

## Resposta

A resposta do endpoint será um JSON contendo as seguintes informações:

- `message`: Uma mensagem indicando o resultado da operação.
- `data`: Uma lista contendo informações sobre a classificação da estrutura de cada parágrafo. Cada item da lista será um dicionário com as seguintes chaves:
  - `estrutura_pred`: Uma string que representa a estrutura prevista para o parágrafo.
  - `paragrafo`: A string do parágrafo classificado.
- `success`: Um valor booleano indicando se a operação foi bem-sucedida ou não.

## Códigos de Resposta

O endpoint pode retornar os seguintes códigos de resposta HTTP:

- 200 OK: A solicitação foi bem-sucedida, e a resposta contém as informações de classificação da estrutura dos parágrafos.
- 400 Bad Request: A solicitação não foi bem-sucedida devido a um erro nos parâmetros fornecidos.
- 500 Internal Server Error: Ocorreu um erro interno durante o processamento da solicitação.

## Exemplo de Solicitação

```json
GET /clasifica_estrutura_paragrafos

Corpo da Solicitação:
{
  "paragrafos": [
    "Este é o primeiro parágrafo.",
    "Aqui está o segundo parágrafo.",
    "E finalmente, o terceiro parágrafo."
  ]
}
```

## Exemplo de Resposta

Código: 200 OK

Corpo da Resposta:
``` json {
  "message": "Estrutura dos parágrafos classificada com sucesso",
  "data": [
    {
      "estrutura_pred": "Tipo_A",
      "paragrafo": "Este é o primeiro parágrafo."
    },
    {
      "estrutura_pred": "Tipo_B",
      "paragrafo": "Aqui está o segundo parágrafo."
    },
    {
      "estrutura_pred": "Tipo_A",
      "paragrafo": "E finalmente, o terceiro parágrafo."
    }
  ],
  "success": true
}
```

# Notas
Certifique-se de fornecer os parâmetros corretos no corpo da solicitação para evitar receber um código de resposta de erro.
A resposta pode variar dependendo do modelo de classificação utilizado para prever as estruturas dos parágrafos.
Em caso de erros ou exceções, o endpoint retornará uma mensagem de erro apropriada na resposta, juntamente com o código de status correspondente.