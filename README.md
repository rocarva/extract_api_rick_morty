# 📌 Coletor de Dados da API Rick and Morty

## 📖 Descrição
Este projeto coleta dados da API [Rick and Morty](https://rickandmortyapi.com/documentation/) e armazena as informações dos personagens, incluindo:
- ID
- Nome
- Status
- Espécie
- Gênero
- Local de origem
- Caminho da imagem baixada

Os dados são salvos em um arquivo CSV e as imagens são baixadas para uma pasta específica.

---

## 📂 Estrutura do Projeto
```
📦 projeto_rick_morty
 ├── 📂 dados
 │   ├── rick_morty.csv  # Arquivo CSV com os personagens coletados
 │   ├── 📂 images       # Pasta onde as imagens são salvas
 │       ├── 1_Rick_Sanchez.jpg
 │       ├── 2_Morty_Smith.jpg
 │       ├── ...
 ├── dados_rick_morty.py # Script principal com a classe DadosRickMorty
 ├── README.md           # Documentação do projeto
 ├── fluxograma.md       # Fluxograma Mermaid
```

---

## 🚀 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/rocarva/extract_api_rick_morty.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd projeto_rick_morty
   ```
3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Como Executar
1. Execute o script principal para coletar os dados:
   ```bash
   python main.py
   ```
2. O CSV será salvo em `dados/rick_morty.csv` e as imagens em `dados/images/`.

---

## 📊 Fluxograma
O fluxo do código está representado no arquivo `fluxograma.md` usando Mermaid.js.

Para visualizar, abra o arquivo em um editor compatível como VSCode com a extensão **Markdown Preview Mermaid Support**.

---

## 📜 Licença
Este projeto é de código aberto e pode ser utilizado livremente.

