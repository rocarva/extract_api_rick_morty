flowchart TD
    A[Início] -->|Instala dependências| B[Instalar requisitos]
    B -->|Obter total de páginas| C[Get Total Pages]
    C -->|Iterar sobre páginas| D{Página disponível?}
    D -->|Sim| E[Obter personagens da página]
    E -->|Iterar sobre personagens| F[Extrair dados do personagem]
    F -->|Baixar imagem| G[Salvar imagem]
    G -->|Adicionar dados ao DataFrame| H[Atualizar lista de personagens]
    H --> D
    D -->|Não| I[Salvar dados no CSV]
    I --> J[Fim]