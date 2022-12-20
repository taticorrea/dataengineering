import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.options.pipeline_options import PipelineOptions


# pipeline_options = PipelineOptions(argv=None)
# pipeline = beam.Pipeline(options=pipeline_options)
with beam.Pipeline() as pipeline:
    colunas_denge = ['id',
                    'data_iniSE',
                    'casos',
                    'ibge_code',
                    'cidade',
                    'uf',
                    'cep',
                    'latitude',
                    'longitude']
    
    delimiter = '|'

    # def text_to_dict(text, cols, delimiter=delimiter):
    #     '''
    #     Recebe um texto, um delimitador e uma lista de colunas. Retorna um dicionario
    #     '''
    #     lista=text.split(delimiter)
    #     return dict(zip(cols,lista))

    def data_transform(element):
        """Recebe um dicionario e cria uma nova chave ano-mes
        Retorna o mesmo dicionario com um novo campo"""        

        element['ano_mes'] = '-'.join(element['data_iniSE'].split('-')[:2])
        return element

    def chave_uf(element):
        '''
        Recebe um dicionario
        Retorna uma tupla () com o estado (UF) e o element (UF,element)
        '''
        chave=element['uf']
        return (chave,element)

    dengue = (
        pipeline
        | "Leitura do dataset de dengue" >> 
            ReadFromText('casos_dengue.txt',skip_header_lines=1)
        | "De texto para dicionario" >>
            beam.Map(lambda x: dict(zip(colunas_denge,x.split(delimiter))))
            # beam.Map(text_to_dict, colunas_denge)        
        | "Criar campo ano-mes" >>
            beam.Map(data_transform)
        | "Criar chave pelo estado" >>
            beam.Map(chave_uf)
        | "Agrupa por chave" >>
            beam.GroupByKey()
        | "Mostrar resultados" >>
            beam.Map(print)            
    )

    pipeline.run()