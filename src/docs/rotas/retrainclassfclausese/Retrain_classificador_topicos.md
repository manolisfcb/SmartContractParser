# Classifica estrutura do documento 
Este endpoint da API permite retreinar o classificador de tópicos e atualizar o conjunto de dados.


Endpoint URL
GET: https://api-ia-contratos.dev.otfin.tools/treinar_classificador_topicos

POST: https://api-ia-contratos.dev.otfin.tools/treinar_classificador_topicos

PUT: https://api-ia-contratos.dev.otfin.tools/treinar_classificador_topicos

## Descripção
Existem 3 casos para retreinar o classificador:

1: Quando o classificador não consiguiu identificar algum paragrafo

2: Quando acaba a operação e temos a ultima versão do contrato (sign-off)

3: Quando o classificador errou e o usuario muda a classificação


1: Quando o classificador não consegue identificar um paragrafo, ele retorna uma flag Falando que
    tem que ser retreinado o classificador. nesse momento já ele tem os dados necessários para
    realizar a operação só precisa ativar o endpoint (http://127.0.0.1:5000/treinar_classificador_topicos)

    Request
    Não é requerido nenhum parametro.
    Status Code: 200 OK
    Content Type: application/json


## Curl
curl --location --request GET 'https://api-ia-contratos.dev.otfin.tools/treinar_classificador_topicos' \
--data-raw ''

### Response:

Corpo da resposta: A resposta será um objeto JSON com a seguinte estrutura:
{
    "message": "Modelo de tópicos retreinado com sucess",
    "success": true,
}


--------------------------------------------------------------------------------------------------------------------

POST: https://api-ia-contratos.dev.otfin.tools/treinar_classificador_topicos

2: Quando acaba a operação, é necessário passar para o classificador os parágrafos aceitos que não foram
    validados automaticamente pelo sistema.

    Atualiza o conjunto de dados para o classificador de tópicos.

## curl --location --request POST 'http://127.0.0.1:5000/treinar_classificador_topicos' \
--header 'Content-Type: application/json' \
--data-raw '{
    "data": [
        {
            "nome_paragrafo_pred": "inscricao_desta_escritura_de_emissao_e_seus_eventuais_aditamentos",
            "paragrafo": "2.2.1 Esta Escritura de Emissão e seus eventuais aditamentos serão inscritos na JUCESP de acordo com o inciso II e o parágrafo 3º do artigo 62 da Lei das Sociedades por Ações, devendo ser levados a protocolo na JUCESP, pela Emissora, no prazo de até 10 (dez) Dias Úteis contados da data da respectiva assinatura. "
        },
        {
            "nome_paragrafo_pred": "inscricao_desta_escritura_de_emissao_e_seus_eventuais_aditamentos",
            "paragrafo": "2.2.2 Nos termos da Cláusula 7.1.7 abaixo, esta Escritura de Emissão será objeto de aditamento para refletir o resultado do Procedimento de Bookbuilding (conforme abaixo definido), o qual irá definir a taxa final de Remuneração das Debêntures, nos termos e condições aprovados na RCA, e, portanto, sem a necessidade de nova aprovação societária pela Emissora."
        },
        {
            "nome_paragrafo_pred": "inscricao_desta_escritura_de_emissao_e_seus_eventuais_aditamentos",
            "paragrafo": "A Emissora deverá entregar ao Agente Fiduciário, no prazo de até 5 (cinco) Dias Úteis contados da data do efetivo registro, 1 (uma) cópia eletrônica (PDF), contendo a chancela de registro da JUCESP, do respectivo documento e eventuais aditamentos inscritos na JUCESP.2.3 Dispensa de Registro na CV"
        }
    ]
}'

    Requisição
    Tipo de conteúdo: application/json
    Corpo da requisição: A carga útil da requisição deve ser um objeto JSON com a seguinte estrutura:

Parâmetros:
paragrafo (string): O valor da coluna "paragrafo" a ser treinado.
nome_paragrafo_pred (string): tag de classificação do paragrafo

## payload entrada post:
    {
        "data": [
            {
                "nome_paragrafo_pred": "destinacao_dos_recursos",
                "paragrafo": "Os recursos obtidos pela Emissora por meio da Emissão serão destinados prioritariamente à aquisição dos Direitos Creditórios Vinculados, quais sejam, as CCBs listadas no Anexo II desta Escritura, bem como de outras CCBs emitidas nos termos da Lei nº 10.931, e que posteriormente integrarão a lista do Anexo II através das devidas atualizações, sendo que, nesta última hipótese, (i) o valor de aquisição será calculado, pelo Agente de Cobrança conforme disposto no Instrumento de Endosso e (ii) deverão ser atendidos os Critérios de Elegibilidade previstos nesta Escritura. "
            }
                    {
                "nome_paragrafo_pred": "inscricao_desta_escritura_de_emissao_e_seus_eventuais_aditamentos",
                "paragrafo": "2.2.1 Esta Escritura de Emissão e seus eventuais aditamentos serão inscritos na JUCESP de acordo com o inciso II e o parágrafo 3º do artigo 62 da Lei das Sociedades por Ações, devendo ser levados a protocolo na JUCESP, pela Emissora, no prazo de até 10 (dez) Dias Úteis contados da data da respectiva assinatura. "
            },
            {
                "nome_paragrafo_pred": "inscricao_desta_escritura_de_emissao_e_seus_eventuais_aditamentos",
                "paragrafo": "2.2.2 Nos termos da Cláusula 7.1.7 abaixo, esta Escritura de Emissão será objeto de aditamento para refletir o resultado do Procedimento de Bookbuilding (conforme abaixo definido), o qual irá definir a taxa final de Remuneração das Debêntures, nos termos e condições aprovados na RCA, e, portanto, sem a necessidade de nova aprovação societária pela Emissora."
            },
            {
                "nome_paragrafo_pred": "inscricao_desta_escritura_de_emissao_e_seus_eventuais_aditamentos",
                "paragrafo": "A Emissora deverá entregar ao Agente Fiduciário, no prazo de até 5 (cinco) Dias Úteis contados da data do efetivo registro, 1 (uma) cópia eletrônica (PDF), contendo a chancela de registro da JUCESP, do respectivo documento e eventuais aditamentos inscritos na JUCESP.2.3 Dispensa de Registro na CV"
            }
                ]
    }

## Resposta
         Código de status: 200 OK
         Tipo de conteúdo: application/json
         Corpo da resposta: A resposta será um objeto JSON com a seguinte estrutura:



3: Quando o classificador erra e o usuario muda a classificação 
POST: https://api-ia-contratos.dev.otfin.tools/treinar_classificador_topicos

## payload entrada pontos 2 e 3:
{
    "data": [
        {
            "nome_paragrafo_pred": "destinacao_dos_recursos",
            "paragrafo": "Os recursos obtidos pela Emissora por meio da Emissão serão destinados prioritariamente à aquisição dos Direitos Creditórios Vinculados, quais sejam, as CCBs listadas no Anexo II desta Escritura, bem como de outras CCBs emitidas nos termos da Lei nº 10.931, e que posteriormente integrarão a lista do Anexo II através das devidas atualizações, sendo que, nesta última hipótese, (i) o valor de aquisição será calculado, pelo Agente de Cobrança conforme disposto no Instrumento de Endosso e (ii) deverão ser atendidos os Critérios de Elegibilidade previstos nesta Escritura. "
        }
                {
            "nome_paragrafo_pred": "inscricao_desta_escritura_de_emissao_e_seus_eventuais_aditamentos",
            "paragrafo": "2.2.1 Esta Escritura de Emissão e seus eventuais aditamentos serão inscritos na JUCESP de acordo com o inciso II e o parágrafo 3º do artigo 62 da Lei das Sociedades por Ações, devendo ser levados a protocolo na JUCESP, pela Emissora, no prazo de até 10 (dez) Dias Úteis contados da data da respectiva assinatura. "
        },
        {
            "nome_paragrafo_pred": "inscricao_desta_escritura_de_emissao_e_seus_eventuais_aditamentos",
            "paragrafo": "2.2.2 Nos termos da Cláusula 7.1.7 abaixo, esta Escritura de Emissão será objeto de aditamento para refletir o resultado do Procedimento de Bookbuilding (conforme abaixo definido), o qual irá definir a taxa final de Remuneração das Debêntures, nos termos e condições aprovados na RCA, e, portanto, sem a necessidade de nova aprovação societária pela Emissora."
        },
        {
            "nome_paragrafo_pred": "inscricao_desta_escritura_de_emissao_e_seus_eventuais_aditamentos",
            "paragrafo": "A Emissora deverá entregar ao Agente Fiduciário, no prazo de até 5 (cinco) Dias Úteis contados da data do efetivo registro, 1 (uma) cópia eletrônica (PDF), contendo a chancela de registro da JUCESP, do respectivo documento e eventuais aditamentos inscritos na JUCESP.2.3 Dispensa de Registro na CV"
        }
            ]
}

## Resposta
        Código de status: 200 OK
        Tipo de conteúdo: application/json
        Corpo da resposta: A resposta será um objeto JSON com a seguinte estrutura:

        {
            "message": "Dados atualizados com sucesso",
        }
