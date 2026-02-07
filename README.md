# POML Instructions

Projeto educacional sobre **Prompt Engineering** estruturado usando **POML (Prompt Orchestration Markup Language)**.

## O que é POML?

POML é uma linguagem de marcação open-source projetada para trazer estrutura, manutenibilidade e versatilidade à engenharia de prompt. Ele substitui "strings de texto plano" por código estruturado.

Funciona para LLMs assim como o HTML funciona para navegadores: define a estrutura, a semântica e os dados de forma padronizada, independentemente do modelo que irá renderizá-lo (GPT-4, Llama, Claude).

## Propósito do Projeto

Este projeto demonstra como:
- Estruturar prompts complexos usando POML
- Versionar e manter prompts como código
- Criar templates reutilizáveis com interpolação de variáveis
- Gerar prompts dinamicamente para diferentes contextos

## Setup

Instale a ferramenta de gerenciamento de dependências Python:
- [UV](https://github.com/astral-sh/uv)

## Como Executar

O projeto possui um entrypoint único que lista todos os scripts disponíveis:

```bash
uv run main.py
```

## Fluxo de Trabalho

1. Execute `uv run main.py` e escolha o script desejado
2. O script carrega o template POML correspondente
3. POML processa e interpola as variáveis definidas
4. Prompt formatado é copiado automaticamente para o clipboard
5. Cole o prompt em seu LLM/agente preferido

## Recursos Adicionais

- [Documentação POML](https://github.com/poml-lang/poml)
- Ver `docs/roadmap.md` para tópicos pendentes
- Ver `docs/glossary.md` para terminologia

## Prompts úteis para começar

- Analise este projeto e me diga o que você entendeu
- Crie um novo template POML para [seu caso de uso]
- Explique a diferença entre POML e prompts de texto plano
