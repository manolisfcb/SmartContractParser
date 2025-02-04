# Documentação do Endpoint LeituraDocx

O endpoint **LeituraDocx** é responsável por ler um arquivo do tipo Docx enviado via método HTTP GET e extrair informações estruturadas a partir dele.

## URL

GET /leitura_docx


## Parâmetros da Solicitação

O endpoint espera receber um arquivo do tipo Docx enviado como parte do corpo da solicitação. O arquivo deve ser enviado como um formulário de dados multipartes, com o parâmetro 'file' representando o arquivo.

('file', type=FileStorage, default=None, location='files')

## Resposta

A resposta do endpoint será um JSON contendo as seguintes informações:

- `message`: Uma mensagem indicando o resultado da operação.
- `success`: Um valor booleano indicando se a operação foi bem-sucedida ou não.
- `data`: Um dicionário contendo as informações estruturadas extraídas do arquivo. Ele contém as seguintes chaves:
  - `conteudo_arquivo`: Uma estrutura de dados representando o conteúdo do arquivo, organizado em uma árvore de dados. Cada nó da árvore pode conter chaves diferentes, dependendo do tipo de elemento encontrado no arquivo Docx.
  - `data_autor`: Um dicionário contendo informações sobre o autor do documento, incluindo o agente fiduciário, o emissor, o autor, a data de criação, a data de modificação e o autor da última modificação.
- `tempo_de_processamento`: O tempo de processamento em segundos, indicando o tempo total que levou para executar a operação.

## Códigos de Resposta

O endpoint pode retornar os seguintes códigos de resposta HTTP:

- 200 OK: A solicitação foi bem-sucedida, e as informações estruturadas do arquivo foram extraídas com sucesso.
- 400 Bad Request: A solicitação não foi bem-sucedida devido a um erro nos parâmetros fornecidos ou na leitura do arquivo.
- 500 Internal Server Error: Ocorreu um erro interno durante o processamento da solicitação.

## Exemplo de Solicitação

A solicitação deve ser enviada como um formulário de dados multipartes, com o arquivo do tipo Docx anexado ao parâmetro 'file'.

## Exemplo de Resposta

```json
Código: 200 OK

Corpo da Resposta:
{
    "data": {
        "conteudo_arquivo": [
            {
                "clausula": "Preambulo",
                "ordem_no_texto": 0,
                "ordem_paragrafo": 0,
                "ordem_tabela": 0,
                "subclausulas": [
                    {
                        "ordem_no_texto": 0,
                        "ordem_paragrafo": 0,
                        "ordem_tabela": 0,
                        "paragrafos": [
                            {
                                "ordem_no_texto": 1,
                                "ordem_paragrafo": 1,
                                "ordem_tabela": null,
                                "texto": "INSTRUMENTO PARTICULAR DE ESCRITURA DA 9ª (NONA) EMISSÃO DE DEBÊNTURES SIMPLES, NÃO CONVERSÍVEIS EM AÇÕES, DA ESPÉCIE QUIROGRAFÁRIA, A SER CONVOLADA NA ESPÉCIE COM GARANTIA REAL, EM SÉRIE ÚNICA, PARA DISTRIBUIÇÃO PÚBLICA, COM ESFORÇOS RESTRITOS DE DISTRIBUIÇÃO, DA VALID SOLUÇÕES S.A.",
                                "tipo": "paragrafo"
                            },
                            
                            {
                                "ordem_no_texto": 34,
                                "ordem_paragrafo": 34,
                                "ordem_tabela": null,
                                "texto": "INSTRUMENTO PARTICULAR DE ESCRITURA DA 9ª (NONA) EMISSÃO DE DEBÊNTURES SIMPLES, NÃO CONVERSÍVEIS EM AÇÕES, DA ESPÉCIE QUIROGRAFÁRIA, A SER CONVOLADA NA ESPÉCIE COM GARANTIA REAL, EM SÉRIE ÚNICA, PARA DISTRIBUIÇÃO PÚBLICA, COM ESFORÇOS RESTRITOS DE DISTRIBUIÇÃO, DA VALID SOLUÇÕES S.A.",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 35,
                                "ordem_paragrafo": 35,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 36,
                                "ordem_paragrafo": 36,
                                "ordem_tabela": null,
                                "texto": "Pelo presente instrumento particular, de um lado,",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 37,
                                "ordem_paragrafo": 37,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 38,
                                "ordem_paragrafo": 38,
                                "ordem_tabela": null,
                                "texto": "VALID SOLUÇÕES S.A., sociedade por ações com registro de companhia aberta perante a Comissão de Valores Mobiliários (“CVM”), com sede na Cidade do Rio de Janeiro, Estado do Rio de Janeiro, na Rua Peter Lund, nº 146-202, São Cristóvão, CEP 20.930-390, e com filial na Alameda Rio Claro, 241 - Bela Vista, na Cidade de São Paulo, Estado de São Paulo, inscrita no Cadastro Nacional da Pessoa Jurídica do Ministério da Economia (“CNPJ/ME”) sob o nº 33.113.309/0001-47, com seus atos constitutivos registrados perante a Junta Comercial do Estado do Rio de Janeiro (“JUCERJA”) sob o NIRE 33.3.0027799-4, neste ato representada na forma de seu estatuto social (“Companhia” ou “Emissora”); ",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 39,
                                "ordem_paragrafo": 39,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 40,
                                "ordem_paragrafo": 40,
                                "ordem_tabela": null,
                                "texto": "e de outro lado, ",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 41,
                                "ordem_paragrafo": 41,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 42,
                                "ordem_paragrafo": 42,
                                "ordem_tabela": null,
                                "texto": "OLIVEIRA TRUST DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A., sociedade por ações, instituição financeira, com sede na cidade do Rio de Janeiro, Estado do Rio de Janeiro, na Avenida das Américas, nº 3.434, bloco 7, Barra da Tijuca, CEP 22640-102, com filial na Cidade de São Paulo, Estado de São Paulo, na Rua Joaquim Floriano, nº 1.502, 13º andar CEP 04534-004, inscrita no CNPJ/ME sob o nº 36.113.876/0004-34, neste ato representada na forma de seu estatuto social (“Agente Fiduciário”), na qualidade de representante dos titulares das Debêntures (conforme abaixo definido) (“Debenturistas”);\n",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 43,
                                "ordem_paragrafo": 43,
                                "ordem_tabela": null,
                                "texto": "Sendo a Emissora e o Agente Fiduciário doravante denominados, em conjunto, como “Partes” e, individual e indistintamente, como “Parte”;",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 44,
                                "ordem_paragrafo": 44,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 45,
                                "ordem_paragrafo": 45,
                                "ordem_tabela": null,
                                "texto": "vêm, por meio desta e na melhor forma de direito, firmar o presente “Instrumento Particular de Escritura da 9ª (nona) Emissão de Debêntures Simples, Não Conversíveis em Ações, da Espécie Quirografária, a ser convolada na Espécie com Garantia Real, em Série Única, para Distribuição Pública com Esforços Restritos de Distribuição, da Valid Soluções S.A.” (“Escritura de Emissão”), mediante as seguintes cláusulas e condições: ",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 46,
                                "ordem_paragrafo": 46,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            }
                        ],
                        "subclausula": "Preambulo"
                    }
                ],
                "tipo": "clausula"
            },
            {
                "clausula": "Cláusula I",
                "ordem_no_texto": 47,
                "ordem_paragrafo": 47,
                "ordem_tabela": null,
                "subclausulas": [
                    {
                        "ordem_no_texto": 47,
                        "ordem_paragrafo": 47,
                        "ordem_tabela": null,
                        "paragrafos": [],
                        "subclausula": "Cláusula I",
                        "tipo": "subclausula"
                    }
                ],
                "tipo": "clausula"
            },
            {
                "clausula": "AUTORIZAÇÃO",
                "ordem_no_texto": 48,
                "ordem_paragrafo": 48,
                "ordem_tabela": null,
                "subclausulas": [
                    {
                        "ordem_no_texto": 48,
                        "ordem_paragrafo": 48,
                        "ordem_tabela": null,
                        "paragrafos": [
                            {
                                "ordem_no_texto": 49,
                                "ordem_paragrafo": 49,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 50,
                                "ordem_paragrafo": 50,
                                "ordem_tabela": null,
                                "texto": "A presente 9ª (nona) emissão, nos termos da Lei nº 6.404, de 15 de dezembro de 1976, conforme alterada (“Lei das Sociedades por Ações” e “Emissão”, respectivamente), de debêntures simples, não conversíveis em ações, da espécie quirografária, a ser convolada na espécie com garantia real, em série única, da Emissora (“Debêntures”), para oferta pública de distribuição, com esforços restritos de distribuição das Debêntures, nos termos da Lei nº 6.385, de 7 de dezembro de 1976, conforme alterada (“Lei do Mercado de Valores Mobiliários”), da Instrução CVM nº 476, de 16 de janeiro de 2009, conforme alterada (“Instrução CVM 476”), e das demais disposições legais e regulamentares aplicáveis (“Oferta”), a celebração desta Escritura de Emissão, do Contrato de Distribuição (conforme definido abaixo) e dos demais documentos da Oferta, serão realizadas com base nas deliberações da Reunião do Conselho de Administração da Companhia realizada em 19 de abril de 2022 (“RCA da Emissora”), na forma do disposto do artigo 59 da Lei das Sociedades por Ações. A RCA da Emissora também autorizou a diretoria da Emissora, ou seus procuradores, para praticar todos os atos necessários à efetivação das deliberações consubstanciadas na RCA da Emissora, elaborar e celebrar todos os documentos necessários à Emissão e à Oferta, eventuais aditamentos aos referidos documentos, bem como a autorização para a contratação de todos os prestadores de serviços inerentes às obrigações previstas nesta Escritura de Emissão, bem como ratificou todos os demais atos já praticados pela diretoria, ou seus procuradores, relacionados nesta Cláusula. ",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 51,
                                "ordem_paragrafo": 51,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            }
                        ],
                        "subclausula": "AUTORIZAÇÃO",
                        "tipo": "subclausula"
                    }
                ],
                "tipo": "clausula"
            },
            {
                "clausula": "AGENTE FIDUCIÁRIO ",
                "ordem_no_texto": 518,
                "ordem_paragrafo": 516,
                "ordem_tabela": null,
                "subclausulas": [
                    {
                        "ordem_no_texto": 518,
                        "ordem_paragrafo": 516,
                        "ordem_tabela": null,
                        "paragrafos": [
                            {
                                "ordem_no_texto": 519,
                                "ordem_paragrafo": 517,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            },

                            {
                                "ordem_no_texto": 547,
                                "ordem_paragrafo": 545,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 548,
                                "ordem_paragrafo": 546,
                                "ordem_tabela": null,
                                "texto": "na data de celebração desta Escritura de Emissão, conforme organograma encaminhado pela Companhia, o Agente Fiduciário identificou que presta serviços de agente fiduciário nas seguintes emissões públicas de valores mobiliários, realizadas por sociedades integrantes do mesmo Grupo Econômico da Companhia: ",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 549,
                                "ordem_paragrafo": 547,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 550,
                                "ordem_paragrafo": null,
                                "ordem_tabela": 3,
                                "texto": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Emissora: VALID SOLUÇÕES S.A.</td>\n      <td>Emissora: VALID SOLUÇÕES S.A.</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Ativo: Debênture</td>\n      <td>Ativo: Debênture</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Série: 1</td>\n      <td>Emissão: 8</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Volume na Data de Emissão: R$ 27.000.000,00</td>\n      <td>Quantidade de ativos: 27000</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Data de Vencimento: 10/05/2024</td>\n      <td>Data de Vencimento: 10/05/2024</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Taxa de Juros: 100% do CDI + 3,85% a.a. na base 252.</td>\n      <td>Taxa de Juros: 100% do CDI + 3,85% a.a. na base 252.</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Status: ATIVO</td>\n      <td>Status: ATIVO</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Inadimplementos no período: Não ocorreram inadimplementos no período.</td>\n      <td>Inadimplementos no período: Não ocorreram inadimplementos no período.</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Garantias: Cessão fiduciária sobre a conta nº 53.028-6, agência 8541 de titularidade da Emissora, mantida junto ao Itaú Unibanco S.A. de movimentação restrita pela Emissora (\"Conta Vinculada\"), na qual serão depositados em até 1 (um) Dia Útil contado da Data de Integralização de cada série, os recursos referentes a 25% (vinte e cinco por cento) do saldo devedor do principal das Debêntures (\"Cash Collateral\"), incluindo a Conta Vinculada e todos os recursos depositados ou que venham a ser depositados e mantidos, a qualquer tempo, incluindo quaisquer recursos eventualmente em trânsito para a Conta Vinculada, ou em compensação bancária, e todos os bens, atuais ou futuros, detidos e a serem detidos pela Cedente a qualquer tempo com relação aos investimentos permitidos vinculados à Conta Vinculada.</td>\n      <td>Garantias: Cessão fiduciária sobre a conta nº 53.028-6, agência 8541 de titularidade da Emissora, mantida junto ao Itaú Unibanco S.A. de movimentação restrita pela Emissora (\"Conta Vinculada\"), na qual serão depositados em até 1 (um) Dia Útil contado da Data de Integralização de cada série, os recursos referentes a 25% (vinte e cinco por cento) do saldo devedor do principal das Debêntures (\"Cash Collateral\"), incluindo a Conta Vinculada e todos os recursos depositados ou que venham a ser depositados e mantidos, a qualquer tempo, incluindo quaisquer recursos eventualmente em trânsito para a Conta Vinculada, ou em compensação bancária, e todos os bens, atuais ou futuros, detidos e a serem detidos pela Cedente a qualquer tempo com relação aos investimentos permitidos vinculados à Conta Vinculada.</td>\n    </tr>\n  </tbody>\n</table>",
                                "tipo": "tabela"
                            },
                            {
                                "ordem_no_texto": 551,
                                "ordem_paragrafo": 548,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 552,
                                "ordem_paragrafo": null,
                                "ordem_tabela": 4,
                                "texto": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Emissora: VALID SOLUÇÕES S.A.</td>\n      <td>Emissora: VALID SOLUÇÕES S.A.</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Ativo: Debênture</td>\n      <td>Ativo: Debênture</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Série: 2</td>\n      <td>Emissão: 8</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Volume na Data de Emissão: R$ 503.700.000,00</td>\n      <td>Quantidade de ativos: 503700</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Data de Vencimento: 10/05/2025</td>\n      <td>Data de Vencimento: 10/05/2025</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Taxa de Juros: 100% do CDI + 4,25% a.a. na base 252.</td>\n      <td>Taxa de Juros: 100% do CDI + 4,25% a.a. na base 252.</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Status: ATIVO</td>\n      <td>Status: ATIVO</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Inadimplementos no período: Não ocorreram inadimplementos no período.</td>\n      <td>Inadimplementos no período: Não ocorreram inadimplementos no período.</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Garantias: Cessão fiduciária sobre a conta nº 53.028-6, agência 8541 de titularidade da Emissora, mantida junto ao Itaú Unibanco S.A. de movimentação restrita pela Emissora (\"Conta Vinculada\"), na qual serão depositados em até 1 (um) Dia Útil contado da Data de Integralização de cada série, os recursos referentes a 25% (vinte e cinco por cento) do saldo devedor do principal das Debêntures (\"Cash Collateral\"), incluindo a Conta Vinculada e todos os recursos depositados ou que venham a ser depositados e mantidos, a qualquer tempo, incluindo quaisquer recursos eventualmente em trânsito para a Conta Vinculada, ou em compensação bancária, e todos os bens, atuais ou futuros, detidos e a serem detidos pela Cedente a qualquer tempo com relação aos investimentos permitidos vinculados à Conta Vinculada.</td>\n      <td>Garantias: Cessão fiduciária sobre a conta nº 53.028-6, agência 8541 de titularidade da Emissora, mantida junto ao Itaú Unibanco S.A. de movimentação restrita pela Emissora (\"Conta Vinculada\"), na qual serão depositados em até 1 (um) Dia Útil contado da Data de Integralização de cada série, os recursos referentes a 25% (vinte e cinco por cento) do saldo devedor do principal das Debêntures (\"Cash Collateral\"), incluindo a Conta Vinculada e todos os recursos depositados ou que venham a ser depositados e mantidos, a qualquer tempo, incluindo quaisquer recursos eventualmente em trânsito para a Conta Vinculada, ou em compensação bancária, e todos os bens, atuais ou futuros, detidos e a serem detidos pela Cedente a qualquer tempo com relação aos investimentos permitidos vinculados à Conta Vinculada.</td>\n    </tr>\n  </tbody>\n</table>",
                                "tipo": "tabela"
                            },
                            {
                                "ordem_no_texto": 553,
                                "ordem_paragrafo": 549,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 554,
                                "ordem_paragrafo": null,
                                "ordem_tabela": 5,
                                "texto": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Emissora: VALID SOLUÇÕES S.A. (nova denominação de VALID SOLUÇÕES E SERV. DE SEG. EM MEIOS DE PAG. E IDENTIFICAÇÃO S.A.)</td>\n      <td>Emissora: VALID SOLUÇÕES S.A. (nova denominação de VALID SOLUÇÕES E SERV. DE SEG. EM MEIOS DE PAG. E IDENTIFICAÇÃO S.A.)</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Ativo: Debênture</td>\n      <td>Ativo: Debênture</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Série: 1</td>\n      <td>Emissão: 7</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Volume na Data de Emissão: R$ 360.000.000,00</td>\n      <td>Quantidade de ativos: 36000</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Data de Vencimento: 04/06/2023</td>\n      <td>Data de Vencimento: 04/06/2023</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Taxa de Juros: 115% do CDI.</td>\n      <td>Taxa de Juros: 115% do CDI.</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Status: ATIVO</td>\n      <td>Status: ATIVO</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Inadimplementos no período: Não ocorreram inadimplementos no período.</td>\n      <td>Inadimplementos no período: Não ocorreram inadimplementos no período.</td>\n    </tr>\n  </tbody>\n</table>",
                                "tipo": "tabela"
                            },

                            {
                                "ordem_no_texto": 666,
                                "ordem_paragrafo": 661,
                                "ordem_tabela": null,
                                "texto": "Sem prejuízo do dever de diligência do Agente Fiduciário, o Agente Fiduciário assumirá que os documentos originais ou cópias autenticadas de documentos encaminhados pela Emissora ou por terceiros a seu pedido não foram objeto de fraude ou adulteração. Não será ainda, sob qualquer hipótese, responsável pela elaboração de documentos societários da Emissora, que permanecerão sob obrigação legal e regulamentar da Emissora elaborá-los, nos termos da legislação aplicável.",
                                "tipo": "paragrafo"
                            },
                            {
                                "ordem_no_texto": 667,
                                "ordem_paragrafo": 662,
                                "ordem_tabela": null,
                                "texto": "",
                                "tipo": "paragrafo"
                            }
                        ],
                        "subclausula": "AGENTE FIDUCIÁRIO ",
                        "tipo": "subclausula"
                    }
                ],
                "tipo": "clausula"
            }
        ],
        "data_autor": {
            "agente_fiduciario": null,
            "author": "Vanessa Rodrigues Fernandes Martins;BBI",
            "autor_modificacao": "Mariana Ferreira Rodrigues | Machado Meyer Advogados",
            "data_criacao": "Wed, 18 May 2022 18:08:00 GMT",
            "data_modificacao": "Wed, 18 May 2022 18:08:00 GMT",
            "emissor": null
        }
    },
    "message": "Arquivo lido com sucesso",
    "success": true,
    "tempo_de_processamento": 15.312795639038086
}
```
## Notas
Certifique-se de enviar um arquivo válido do tipo Docx para que a extração de informações estruturadas seja bem-sucedida.
Em caso de erros ou exceções, o endpoint retornará uma mensagem de erro apropriada na resposta, juntamente com o código de status correspondente.
O conteúdo da estrutura de dados conteudo_arquivo e os campos data_autor podem variar dependendo do conteúdo e da estrutura do arquivo Docx enviado.
O tempo de processamento pode variar dependendo do tamanho e complexidade do arquivo Docx sendo processado.