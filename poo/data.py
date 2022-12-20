class Data:
    def __init__(self,dia,mes,ano) -> None:
        self.dia=dia
        self.mes=mes
        self.ano=ano
    
    def format_data(self):
        data_formated = "{}/{}/{}".format(self.dia,self.mes,self.ano)
        return data_formated