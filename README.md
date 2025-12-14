# SDW2023 - Pipeline ETL com Python e GPT-4

Este projeto demonstra um pipeline ETL simples utilizando Python e a API da OpenAI (GPT-4).

## Estrutura
- SDW2023.csv → Dataset de entrada
- etl_pipeline.py → Pipeline ETL
- requirements.txt → Dependências
- SDW2023_output.json → Saída gerada

## Como executar
```bash
pip install -r requirements.txt
python etl_pipeline.py
```

## Variáveis de ambiente
Crie um arquivo `.env` com:
```
OPENAI_API_KEY=sua_chave_aqui
```

## Fluxo
Extract → CSV  
Transform → GPT-4  
Load → JSON  

Projeto pronto para uso educacional e portfólio.
