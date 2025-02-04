# Documentação do Endpoint GerarNovaVersao

O endpoint **GerarNovaVersao** é responsável por gerar uma nova versão de um documento associado a um armazenamento. Ele recebe informações sobre as edições a serem feitas no documento e retorna uma nova versão atualizada do mesmo.

## URL

GET /gerar_nova_versao


## Parâmetros da Solicitação

O endpoint espera receber uma solicitação com um corpo JSON contendo os seguintes parâmetros:

- `armazenamento_uid`: Uma string que representa o identificador único do armazenamento associado ao documento.
- `conteudo_arquivo`: Uma lista de objetos representando as edições a serem feitas no documento. Cada objeto tem as seguintes chaves:
  - `adicionado_apos` (opcional): Um número inteiro que indica a posição após a qual o parágrafo será adicionado. Se não fornecido, será usado o valor da chave `ordem`.
  - `ordem`: Um número inteiro que indica a posição do parágrafo a ser editado.
  - `tipo_texto`: Uma string que pode ser "tabela" ou "paragrafo", indicando o tipo de texto a ser editado.
  - `tipo_acao`: Uma string que pode ser "criado", "editado" ou "deletado", indicando a ação a ser realizada no parágrafo.
  - `texto`: Uma string que representa o conteúdo do parágrafo ou tabela a ser adicionado, editado ou deletado.

## Resposta

A resposta do endpoint será um JSON contendo as seguintes informações:

- `message`: Uma mensagem indicando o resultado da operação.
- `success`: Um valor booleano indicando se a operação foi bem-sucedida ou não.
- `data` (opcional): Uma lista contendo informações adicionais sobre a resposta, caso necessário.
- `url_api`: Uma string que representa a URL da API de armazenamento utilizada para carregar e salvar o arquivo modificado.

## Códigos de Resposta

O endpoint pode retornar os seguintes códigos de resposta HTTP:

- 200 OK: A solicitação foi bem-sucedida, e a nova versão do documento foi gerada e atualizada no armazenamento.
- 400 Bad Request: A solicitação não foi bem-sucedida devido a um erro nos parâmetros fornecidos.
- 500 Internal Server Error: Ocorreu um erro interno durante o processamento da solicitação.

## Exemplo de Solicitação

```json
GET /gerar_nova_versao

Corpo da Solicitação:
{
  "armazenamento_uid": "abcd1234",
  "conteudo_arquivo": [
    {
      "ordem": 3,
      "tipo_texto": "paragrafo",
      "tipo_acao": "editado",
      "texto": "Este é um novo parágrafo editado."
    },
    {
      "adicionado_apos": 5,
      "tipo_texto": "paragrafo",
      "tipo_acao": "criado",
      "texto": "Este é um novo parágrafo adicionado após a posição 5."
    },
    {
      "ordem": 2,
      "tipo_texto": "tabela",
      "tipo_acao": "editado",
      "texto": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Emissora: VALID SOLUÇÕES S.A.</td>\n      <td>Emissora: VALID SOLUÇÕES S.A.</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Ativo: Debênture</td>\n      <td>Ativo: Debênture</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Série: 2</td>\n      <td>Emissão: 8</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Volume na Data de Emissão: R$ 503.700.000,00</td>\n      <td>Quantidade de ativos: 503700</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Data de Vencimento: 10/05/2025</td>\n      <td>Data de Vencimento: 10/05/2025</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Taxa de Juros: 100% do CDI + 4,25% a.a. na base 252.</td>\n      <td>Taxa de Juros: 100% do CDI + 4,25% a.a. na base 252.</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Status: ATIVO</td>\n      <td>Status: ATIVO</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Inadimplementos no período: Não ocorreram inadimplementos no período.</td>\n      <td>Inadimplementos no período: Não ocorreram inadimplementos no período.</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Garantias: Cessão fiduciária sobre a conta nº 53.028-6, agência 8541 de titularidade da Emissora, mantida junto ao Itaú Unibanco S.A. de movimentação restrita pela Emissora (\"Conta Vinculada\"), na qual serão depositados em até 1 (um) Dia Útil contado da Data de Integralização de cada série, os recursos referentes a 25% (vinte e cinco por cento) do saldo devedor do principal das Debêntures (\"Cash Collateral\"), incluindo a Conta Vinculada e todos os recursos depositados ou que venham a ser depositados e mantidos, a qualquer tempo, incluindo quaisquer recursos eventualmente em trânsito para a Conta Vinculada, ou em compensação bancária, e todos os bens, atuais ou futuros, detidos e a serem detidos pela Cedente a qualquer tempo com relação aos investimentos permitidos vinculados à Conta Vinculada.</td>\n      <td>Garantias: Cessão fiduciária sobre a conta nº 53.028-6, agência 8541 de titularidade da Emissora, mantida junto ao Itaú Unibanco S.A. de movimentação restrita pela Emissora (\"Conta Vinculada\"), na qual serão depositados em até 1 (um) Dia Útil contado da Data de Integralização de cada série, os recursos referentes a 25% (vinte e cinco por cento) do saldo devedor do principal das Debêntures (\"Cash Collateral\"), incluindo a Conta Vinculada e todos os recursos depositados ou que venham a ser depositados e mantidos, a qualquer tempo, incluindo quaisquer recursos eventualmente em trânsito para a Conta Vinculada, ou em compensação bancária, e todos os bens, atuais ou futuros, detidos e a serem detidos pela Cedente a qualquer tempo com relação aos investimentos permitidos vinculados à Conta Vinculada.</td>\n    </tr>\n  </tbody>\n</table>"
    }
  ]
}
```

## Exemplo de Resposta
Código: 200 OK

Corpo da Resposta:
{
  "message": "Versão gerada com sucesso",
  "success": true,
  "url_api": "https://exemplo-api-armazenamento.com",
  "data": []
}

## Notas
Certifique-se de fornecer os parâmetros corretos no corpo da solicitação para evitar receber um código de resposta de erro.
A chave data na resposta é opcional e pode conter informações adicionais, caso necessário.
Em caso de erros ou exceções, o endpoint retornará uma mensagem de erro apropriada na resposta, juntamente com o código de status correspondente.