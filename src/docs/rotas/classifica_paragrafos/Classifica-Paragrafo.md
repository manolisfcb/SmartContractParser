# Documentação do Endpoint ClasificaParagrafos

O endpoint **ClasificaParagrafos** é responsável por classificar parágrafos fornecidos em um JSON através do método HTTP GET. Ele retorna uma resposta JSON com informações sobre a classificação de cada parágrafo e pode atualizar o modelo de classificação, se necessário.

## URL

GET /clasifica_paragrafos


## Parâmetros da Solicitação

O endpoint espera receber uma solicitação com um corpo JSON contendo os seguintes parâmetros:

- `paragrafos`: Uma lista de strings representando os parágrafos que serão classificados.
- `clausula`: Uma string que representa o nome da cláusula à qual os parágrafos pertencem.
- `subclausula` (opcional): Uma string que representa o nome da subcláusula à qual os parágrafos pertencem, caso seja aplicável.

## Resposta

A resposta do endpoint será um JSON contendo as seguintes informações:

- `message`: Uma mensagem indicando o resultado da operação.
- `data`: Uma lista contendo informações sobre a classificação de cada parágrafo. Cada item da lista será um dicionário com as seguintes chaves:
  - `nome_paragrafo_pred`: Uma string que representa o nome da classe prevista para o parágrafo. Caso o parágrafo não possa ser classificado, será retornado o valor 'nao_classificado'.
  - `indice_certeza`: Um valor numérico representando o índice de certeza da classificação.
  - `paragrafo`: A string do parágrafo classificado.
- `success`: Um valor booleano indicando se a operação foi bem-sucedida ou não.
- `tem_que_retreinar`: Um valor booleano que indica se é necessário retreinar o modelo de classificação. Este valor será alterado para `True` caso algum parágrafo seja classificado como 'nao_classificado', e o modelo precisa ser atualizado.

## Códigos de Resposta

O endpoint pode retornar os seguintes códigos de resposta HTTP:

- 200 OK: A solicitação foi bem-sucedida, e a resposta contém as informações de classificação dos parágrafos.
- 400 Bad Request: A solicitação não foi bem-sucedida devido a um erro nos parâmetros fornecidos.
- 500 Internal Server Error: Ocorreu um erro interno durante o processamento da solicitação.

## Exemplo de Solicitação

```json
GET /clasifica_paragrafos

Corpo da Solicitação:
{
  "paragrafos": [
    "Lorem ipsum dolor sit amet.",
    "Nullam nec ex eu ligula consectetur rhoncus.",
    "Praesent lacinia nisi sed nibh volutpat, in faucibus purus venenatis."
  ],
  "clausula": "Lorem Ipsum",
  "subclausula": "Nullam Nec Ex"
}
```


##  Exemplo de Solicitação

Código: 200 OK

Corpo da Resposta:

``` json{
  "message": "Parágrafos classificados com sucesso",
  "data": [
    {
      "nome_paragrafo_pred": "Classe_A",
      "indice_certeza": 0.85,
      "paragrafo": "Lorem ipsum dolor sit amet."
    },
    {
      "nome_paragrafo_pred": "Classe_B",
      "indice_certeza": 0.78,
      "paragrafo": "Nullam nec ex eu ligula consectetur rhoncus."
    },
    {
      "nome_paragrafo_pred": "Classe_A",
      "indice_certeza": 0.91,
      "paragrafo": "Praesent lacinia nisi sed nibh volutpat, in faucibus purus venenatis."
    }
  ],
  "success": true,
  "tem_que_retreinar": false
}

```
## Notas
Certifique-se de fornecer os parâmetros corretos no corpo da solicitação para evitar receber um código de resposta de erro.
Se algum parágrafo for classificado como 'nao_classificado', o valor de tem_que_retreinar será alterado para True, indicando a necessidade de retrainar o modelo de classificação.
Caso ocorra um erro interno no servidor durante o processamento da solicitação, será retornada uma mensagem de erro genérica. Em caso de erros, é recomendado verificar o corpo da resposta para detalhes adicionais.