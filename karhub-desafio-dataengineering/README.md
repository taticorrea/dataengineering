# desafio-de-karhub-TatianeCorrea

Repositório com os scripts de leitura, sanitizaçâo, analise e ingestao de dados no Google BigQuery, como parte do Desafio do processo seletivo para vaga da Data Engineer na startup KarHub.


### Tabela de Conteúdo
- [Consideraçôes](#resume)
- [Utilizaçâo](#uso)
    - [Jupyter Notebook](#jupyter)


## Consideracoes
O objetivo do notebook é coletar, tratar, ingerir e analisar dados mocados no contexto da venda de peças automotivas pela KarHub. No total foram utilizados 3 datasets: 
- produtos_alias
- produtos
- veiculos_compativeis

Estes datasets possuem respectivamente dados de mapeamento entre todos possíveis ids de produtos e seus ids originais (de fabrica), sobre as peças e os veículos compativeis com as peças. O objetivo de negócio é gerar uma visâo ampla das peças à venda e seus respectivos atributos, e dos automoveis compatíveis com essas peças, utilizando a chave de relacionamento id original dos produtos.

Em uma primeira etapa foi realizada a obtencao dos dados, que por sua vez vinham de 3 fontes distintas: um arquivo .csv, um arquivo .xlsx e uma lista de jsons oriunda do output da requisicao da API de dados de veículos compatíveis. Em uma segunda etapa foi realizada a sanitizaçâo dos dados, fazendo tipagem e aplicando remção de caracteres especiais, como underscore, acentos, etc. Posteriormente foi realizada a etapa de filtragem e enriquecimento dos dados, selecionando na tabela de produtos apenas registros que possuiam a coluna ValorAtributo correspondente a alguma dimensao física como Largura e Altura.

Por fim, foi realizada a ingestao da tabela com dados de produtos e automoveis compatíveis no Google BigQuery e feitas as queries pedidas via pandas-gbq.


## Utilizacao
### Juppyter Notebook
Via Jupyter Notebook é possível acompanhar o raciocínio seguido durante o implementaçâ o da soluçâo de dados. Para rodar, basta abrir o arquivo .ipynb localmente no Jupyter ou abrir o arquivo via Google Colab. No inicio do notebook existem alguns comandos shell para instalar bibliotecas que sâo utilizadas no desenvolvimento. Também é possível instalar as dependencias desse projeto via pip install -r requirements.txt