# Setup

## Pré-requisitos

- Python 3.10+
- Uma API key da OpenAI

## Instalação

```bash
# 1. Criar e ativar o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar a API key
cp .env.example .env
# Edite o .env e substitua sk-your-key-here pela sua key
```

## Executar

```bash
source venv/bin/activate
uvicorn main:app --reload
```

Acesse http://localhost:8000 (porta padrão do uvicorn)

Para usar outra porta:

```bash
uvicorn main:app --reload --port 3000
```

## Estrutura do projeto

```
main.py          → Setup do app FastAPI e routers
llm.py           → Cliente OpenAI e helper call_llm
techniques.py    → Engines reutilizáveis (ToT, ReAct, execução de código)
prompts.py       → Todos os prompts organizados por técnica
routes/
  review.py      → Endpoints de code review (/api/review/*)
  logic.py       → Endpoints de lógica (/api/logic/*)
frontend.html    → Interface web (HTML único)
```

## Técnicas demonstradas

| Técnica | O que faz | Chamadas LLM |
|---|---|---|
| **Prompt Simples** | Envia o problema sem instrução específica | 1 |
| **Chain of Thought** | Pede para o modelo pensar passo a passo | 1 |
| **ReAct** | Modelo alterna raciocínio e execução de código | Múltiplas (loop autônomo) |
