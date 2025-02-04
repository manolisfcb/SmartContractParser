# Documentação da Classe Docx

## Descrição

A classe `Docx` é utilizada para manipular documentos no formato `.docx`. Essa classe possui métodos para obter informações sobre o documento, editar o texto de parágrafos e tabelas, além de estruturar os dados do documento em uma árvore hierárquica.

## Construtor

```python
def __init__(self, path):
    """
    Construtor da classe Docx.

    Args:
        path (str): Caminho do arquivo .docx a ser lido.
    """
```
Atributos
- path: Caminho do arquivo .docx que foi lido.
- doc: Objeto docx.Document que representa o documento do Word.
- tags_body: Lista de tags que representam a estrutura do documento.
- tables: Lista de objetos da classe Table, que representam as tabelas do documento.
- paragrafos: Lista de objetos da classe Paragrafo, que representam os parágrafos do documento.

# Métodos

`get_tags_body()`

def get_tags_body(self):
    """
    Obtém as tags que representam a estrutura do corpo do documento.

    Returns:
        list: Lista de tags que representam a estrutura do corpo do documento.
    """
`get_all_paragraphs_text()`

def get_all_paragraphs_text(self):
    """
    Obtém o texto de todos os parágrafos do documento.

    Returns:
        list: Lista com o texto de todos os parágrafos do documento.
    """

`get_table(table_index) `

def get_table(self, table_index):
    """
    Obtém uma tabela específica do documento.

    Args:
        table_index (int): Índice da tabela a ser obtida.

    Returns:
        Table or None: Objeto da classe Table que representa a tabela encontrada.
            Retorna None se a tabela não for encontrada.
    """
` get_paragrafo(paragrafo_index) `

def get_paragrafo(self, paragrafo_index):
    """
    Obtém um parágrafo específico do documento.

    Args:
        paragrafo_index (int): Índice do parágrafo a ser obtido.

    Returns:
        Paragrafo or None: Objeto da classe Paragrafo que representa o parágrafo encontrado.
            Retorna None se o parágrafo não for encontrado.
    """
`edit_paragrafo(paragrafo_index, text) `

def edit_paragrafo(self, paragrafo_index, text):
    """
    Edita o texto de um parágrafo específico no documento.

    Args:
        paragrafo_index (int): Índice do parágrafo a ser editado.
        text (str): Novo texto a ser inserido no parágrafo.

    Returns:
        Docx: A própria instância do objeto após a edição.
    """

` edit_table(table_index, text) `

def edit_table(self, table_index, text):
    """
    Edita o conteúdo de uma tabela específica no documento.

    Args:
        table_index (int): Índice da tabela a ser editada.
        text (str): Novo conteúdo da tabela em formato HTML.

    Returns:
        Docx: A própria instância do objeto após a edição.
    """

