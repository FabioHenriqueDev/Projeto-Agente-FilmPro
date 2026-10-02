# FilmPro

O FilmPro é uma aplicação de recomendação personalizada de filmes. Descreva o que você está com vontade de assistir e o agente usa inteligência artificial para sugerir títulos que combinam com suas preferências.

O projeto reúne uma interface web em português e uma API construída com FastAPI. Para pesquisar e organizar as recomendações, o agente utiliza o modelo GPT-4o, busca na web e consulta informações de filmes na OMDb.

## Funcionalidades

- Recomenda filmes com base em gênero, clima, temas e títulos de referência informados pelo usuário.
- Apresenta informações como sinopse, ano, direção, gêneros, duração, avaliação e motivo da recomendação.
- Inclui uma interface web para enviar preferências e visualizar os resultados.
- Expõe documentação interativa da API com Swagger UI e ReDoc.
- Disponibiliza uma rota simples para verificar se a API está online.

## Tecnologias

- Python 3
- FastAPI e Uvicorn
- Agno e OpenAI GPT-4o
- OMDb API
- HTML, CSS e JavaScript

## Requisitos

- Python 3 instalado.
- Uma chave de API da OpenAI.
- Uma chave de API da OMDb.

## Como executar

1. Clone o repositório e acesse a pasta do projeto:

   ```powershell
   git clone <URL_DO_REPOSITORIO>
   cd <PASTA_DO_REPOSITORIO>
   ```

2. Crie e ative um ambiente virtual:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   No macOS ou Linux, use:

   ```bash
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto:

   ```env
   OPENAI_API_KEY=sua_chave_openai
   API_KEY_OMDB=sua_chave_omdb
   ```

   Obtenha as chaves nos sites da [OpenAI](https://platform.openai.com/api-keys) e da [OMDb API](https://www.omdbapi.com/apikey.aspx). Não publique o arquivo `.env` nem inclua chaves em commits.

5. Inicie a aplicação:

   ```bash
   python main.py
   ```

6. Acesse:

   - Aplicação web: [http://localhost:8000](http://localhost:8000)
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API

### `GET /health`

Verifica a disponibilidade da API.

```bash
curl http://localhost:8000/health
```

### `POST /recomendations`

Gera recomendações a partir das preferências enviadas. O campo `preferences` deve conter entre 10 e 500 caracteres.

```bash
curl -X POST http://localhost:8000/recomendations \
  -H "Content-Type: application/json" \
  -d "{\"preferences\":\"Quero um suspense inteligente, com reviravoltas\"}"
```

A resposta contém `data.movies`, uma lista de filmes com dados estruturados, e `data.total_recommendations`. O campo de sucesso da resposta chama-se `sucess` no formato atual da API.

## Estrutura do projeto

```text
.
├── agent/                 # Agente, prompts, modelos, configuração e ferramenta OMDb
├── api/                   # Aplicação FastAPI e endpoints
├── design/                # Referência visual do projeto
├── site/                  # Interface web estática
├── main.py                # Inicialização do servidor
└── requirements.txt       # Dependências Python
```

## Desenvolvimento e observações

- O servidor de desenvolvimento inicia com recarga automática.
- As chamadas de recomendação dependem da disponibilidade e das credenciais dos serviços externos OpenAI e OMDb.
- O CORS está configurado para aceitar qualquer origem no código atual; revise essa configuração antes de publicar a API em produção.
- Este checkout não inclui uma suíte de testes automatizados configurada.
