# Prompt Engineering — MBA Engenharia de Software com IA

Aplicação web interativa que demonstra como **diferentes técnicas de prompt engineering** produzem resultados drasticamente diferentes usando o **mesmo modelo** (GPT-4o-mini).

## O que faz

A aplicação compara lado a lado 3 técnicas de prompt em dois cenários:

### Cenário 1: Code Review
Analisa uma função Python (`aplicar_desconto`) com problemas sutis usando:

- **Prompt Simples** — instrução direta sem estrutura (zero-shot)
- **Chain of Thought (CoT)** — força o modelo a raciocinar passo a passo
- **ReAct** — combina raciocínio com execução real de código Python para validar hipóteses

### Cenário 2: Pegadinha Lógica (Strawberry)
Testa a pergunta clássica *"Quantas vezes a letra 'r' aparece em 'strawberry'?"* com as mesmas técnicas, mostrando como LLMs erram contagem sem técnicas adequadas.

## Arquitetura

```
main.py           → FastAPI app + serve do frontend
llm.py            → Client OpenAI e helper call_llm()
prompts.py        → Todos os prompts organizados por técnica
techniques.py     → Engines genéricos: Tree of Thought, ReAct loop, execução de código
routes/review.py  → Endpoints /api/review/{simple,cot,tot,react}
routes/logic.py   → Endpoints /api/logic/{simple,cot,tot,react}
frontend.html     → Interface single-page com grid comparativo
```

## Pré-requisitos

- Python 3.10+
- Chave de API da OpenAI

## Como executar

1. **Clone e entre no diretório:**
   ```bash
   cd prompts
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # venv\Scripts\activate   # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure a chave da OpenAI:**
   ```bash
   echo "OPENAI_API_KEY=sk-..." > .env
   ```

5. **Inicie o servidor:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Acesse no navegador:**
   ```
   http://localhost:8000
   ```

Clique em **"EXECUTAR CODE REVIEW"** ou **"EXECUTAR CONTAGEM"** para rodar todas as técnicas em paralelo e comparar os resultados.

## Licença

Este projeto é parte do material educacional da [Full Cycle](https://fullcycle.com.br).
