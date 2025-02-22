# -*- coding: utf-8 -*-
"""
Coletor de dados da API Rick and Morty
Documentação: https://rickandmortyapi.com/documentation/

Objetivo:
- Coletar os seguintes itens:
    - ID
    - Nome do personagem
    - Status
    - Espécie
    - Gênero
    - Local de origem
    - Imagem do personagem
"""
import requests
import os
import pandas as pd

class DadosRickMorty:
    """Classe para coletar e processar dados da API Rick and Morty."""

    def __init__(self):
        self.url = 'https://rickandmortyapi.com/api/character'
        self.image_dir = 'dados/images'
        os.makedirs(self.image_dir, exist_ok=True)
        self.characters_data = []
        
        
    # Função para obter o número total de páginas
    def get_total_pages(self):
        """Obtém o número total de páginas da API."""
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json().get('info', {}).get('pages', 0)
        return 0
    

    # Função para obter os personagens de uma página específica
    def get_characters(self, page):
        """Obtém os personagens de uma página específica."""
        response = requests.get(self.url, params={'page': page})
        if response.status_code == 200:
            return response.json().get('results', [])
        return []
    
        # Funções para capturar os campos desejados
    def get_id(self, character):
        return character.get('id')

    def get_name(self, character):
        return character.get('name')

    def get_status(self, character):
        return character.get('status')

    def get_species(self, character):
        return character.get('species')

    def get_gender(self, character):
        return character.get('gender')

    def get_origin(self, character):
        return character.get('origin', {}).get('name')

    def get_image_url(self, character):
        return character.get('image')
    
    # Função para baixar a imagem do personagem
    def download_image(self, character):
        """Baixa e salva a imagem do personagem."""
        image_url = self.get_image_url(character)
        if image_url:
            image_name = f"{self.get_id(character)}_{self.get_name(character).replace(' ', '_')}.jpg"
            image_path = os.path.join(self.image_dir, image_name)

            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                with open(image_path, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                return image_path
        return None
    
    # Função para extrair os dados formatados de um personagem
    def extract_character_data(self, character):
        """Extrai os dados formatados de um personagem."""
        return {
            "id": self.get_id(character),
            "name": self.get_name(character),
            "status": self.get_status(character),
            "species": self.get_species(character),
            "gender": self.get_gender(character),
            "origin": self.get_origin(character),
            "image_path": self.download_image(character)  # Salva a imagem e retorna o caminho
        }
    
    def run(self):
        """Executa o processo de coleta de dados."""
        total_pages = self.get_total_pages()
        for page in range(1, total_pages + 1):
            characters = self.get_characters(page)
            for character in characters:
                character_data = self.extract_character_data(character)
                self.characters_data.append(character_data)
        
        print(f"Coleta concluída! {len(self.characters_data)} personagens coletados.")

    def save_to_csv(self):
        """Salva os dados coletados em um arquivo CSV."""
        df = pd.DataFrame(self.characters_data)
        df.to_csv('dados/rick_morty.csv', index=False)
        print("Dados salvos em 'dados/rick_morty.csv'.")



if __name__ == "__main__":
    rick_morty = DadosRickMorty()
    rick_morty.run()
    rick_morty.save_to_csv()
