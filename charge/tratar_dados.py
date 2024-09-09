import pandas as pd
import unicodedata
import re

DEFAULT = 'https://raw.githubusercontent.com/kelvins/municipios-brasileiros/main/csv/municipios.csv'

class TratarCidadesBrasil:

    def __init__(self, path_cidades_info=DEFAULT):
        self.cidades_info = pd.read_csv(path_cidades_info)
        """
        DataFrame contendo 'nome', 'latitude' e 'longitude'
        das cidades do Brasil.
        """        

    def listar_cidades(self):
        """
        Lista o nome de todos os municípios do Brasil
        com a primeira letra do nome em maiúsculo.

        Returns:
            list: Nome dos municípios do Brasil
        """        
        self.cidades_info['nome'] = self.cidades_info['nome'].apply(lambda city: str(city).capitalize())
        self.cidades_info['nome'] = self.cidades_info['nome'].apply(lambda city: self.remover_acentuacao(str(city)))

        cidades_do_brasil = self.cidades_info['nome'].to_list()
        return cidades_do_brasil
    
    def remover_acentuacao(self, texto):
        """
        Normaliza um texto de entrada para uma versão
        sem acentuação.

        Args:
            texto (string): Texto com acentuação

        Returns:
            string: Texto sem acentuação
        """        
        texto_normalizado = unicodedata.normalize('NFD', texto)
        texto_sem_acento = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
        return texto_sem_acento

    def tratar_cidade(self, nome_cidades_do_brasil, cidade):
        """
        Verifica e padroniza o nome de uma cidade
        para o mesmo padrão da base DEFAULT.

        Args:
            nome_cidades_do_brasil (list): Lista com os municípios do Brasil
            cidade (string): Nome de uma possível cidade do Brasil

        Returns:
            string: Nome padronizado
        """
        cidade = cidade.split('-')[0]
        cidade = re.sub(r'\d+|\|', '', cidade)
        cidade = self.remover_acentuacao(cidade)

        # Converte toda a cidade para minúsculas e depois capitaliza a primeira letra
        cidade = cidade.lower().strip().capitalize()
        
        if ("/" in cidade) or ("," in cidade):
            cidade_split = cidade.split("/")
            if len(cidade_split) < 2:
                cidade_split = cidade.split(",")
            
            cidade = cidade_split[1].strip().capitalize()
            
            if cidade not in nome_cidades_do_brasil:
                cidade = cidade_split[0].strip().capitalize()
                
        return cidade.strip()

    def pesquisar_latitude(self, cidade):
        """
        Pesquisa a latitude de uma cidade na base DEFAULT.
        """
        nomes_cidades_do_brasil = self.cidades_info['nome'].apply(lambda city: str(city).capitalize()).to_list()
        
        if cidade in nomes_cidades_do_brasil:
            latitude = self.cidades_info[self.cidades_info['nome'] == cidade].iloc[0]['latitude']
            return latitude
        return None  # ou outro valor padrão caso a cidade não seja encontrada

    def pesquisar_longitude(self, cidade):
        """
        Pesquisa a longitude de uma cidade na base DEFAULT.
        """
        nomes_cidades_do_brasil = self.cidades_info['nome'].apply(lambda city: str(city).capitalize()).to_list()
        
        if cidade in nomes_cidades_do_brasil:
            longitude = self.cidades_info[self.cidades_info['nome'] == cidade].iloc[0]['longitude']
            return longitude
        return None  # ou outro valor padrão caso a cidade não seja encontrada
