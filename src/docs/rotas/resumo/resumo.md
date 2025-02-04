# Documentação do Endpoint "Resumo"
## Descrição
O endpoint "Resumo" é utilizado para obter um resumo das informações contidas em um documento no formato .docx. O resumo é gerado com base na frequência das palavras em cada sentença do documento, selecionando as 20 sentenças com maior pontuação para formar o resumo final.

## Método HTTP
- Método: GET
- Parâmetros da Requisição:  O endpoint espera receber um objeto JSON contendo a chave armazenamento_uid, que é o identificador único do documento a ser processado. 
- Exemplo:
``` json
{
  "armazenamento_uid": "7c24e1e6-7dbf-43b2-84f9-2cc2f9065ef9"
}
```
## Resposta da Requisição
A resposta da requisição será um objeto JSON contendo as seguintes informações:

- data: Objeto JSON com o conteúdo do resumo gerado:
- conteudo_resumo: Objeto JSON contendo os seguintes campos:
- numero_da_emissao: Número da emissão do documento (caso exista).
- especie: Espécie do documento (caso exista).
- produto: Tipo do produto do documento (neste caso, sempre será "debênture").
- data_de_emissao: Data de emissão do documento (caso exista).
- data_de_vencimento: Data de vencimento do documento (caso exista).
- valor_nominal_unitario: Valor nominal unitário do documento (caso exista).
- valor_total_da_emissao: Valor total da emissão do documento (caso exista).
- jornal_de_publicacao: Jornal de publicação do documento (caso exista).
- repactuacao: Informações sobre repactuação do documento (caso exista).
- numero_de_serie: Número de série do documento (caso exista).
- quantidade_de_papeis: Quantidade de papéis do documento (caso exista).
- garantias: Informações sobre garantias do documento (caso exista).
- resumo: Texto do resumo gerado a partir do conteúdo do documento.
- success: Booleano indicando se a requisição foi bem sucedida ou não.
- message: Mensagem de sucesso ou erro, informando o resultado da requisição.

## Exemplo de Resposta

``` json
 {
  "data": {
    "conteudo_resumo": {
      "numero_da_emissao": "12345",
      "especie": "Ordinária",
      "produto": "debênture",
      "data_de_emissao": "2023-07-15",
      "data_de_vencimento": "2028-07-15",
      "valor_nominal_unitario": "100.00",
      "valor_total_da_emissao": "1000000.00",
      "jornal_de_publicacao": "Diário Oficial",
      "repactuacao": "Sim",
      "numero_de_serie": "A123",
      "quantidade_de_papeis": "10000",
      "garantias": "Hipoteca de Imóveis",
      "resumo": "Este é um resumo gerado a partir do documento. Contém informações relevantes sobre a emissão de debêntures, incluindo número da emissão, espécie, data de emissão, data de vencimento, valor nominal unitário, valor total da emissão, jornal de publicação, repactuação, número de série, quantidade de papéis e informações sobre as garantias. O resumo é gerado com base na frequência das palavras em cada sentença do documento, selecionando as 20 sentenças com maior pontuação para formar o resumo final."
    }
  },
  "success": true,
  "message": "Resumo gerado com sucesso"
}
```

Em caso de erro na requisição, a chave success será false e a chave message conterá a mensagem de erro. Exemplo:

``` json 
{
  "message": "Ocorreu um erro ao processar o documento",
  "success": false
}

```