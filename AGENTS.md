# AGENTS.md

Este documento contém informações e diretrizes para LLMs (Large Language Models) trabalharem com este projeto.

## Sobre o Projeto

Este é um projeto educacional focado em **Prompt Engineering** usando **POML (Prompt Orchestration Markup Language)**. O objetivo é ensinar como estruturar, versionar e manter prompts complexos de forma organizada.

### Estrutura de Diretórios

- `main.py` - Entrypoint único para execução de scripts
- `poml/` - Templates de prompts em formato .poml
- `src/` - Scripts Python que processam os templates
- `docs/` - Documentação (progress.md, glossary.md)
- `static/` - Arquivos de configuração auxiliares

## Como Executar

O projeto possui um entrypoint único que lista todos os scripts disponíveis:

```bash
uv run main.py
```

## O que é POML?

POML é uma linguagem de marcação (similar a XML/HTML) para estruturar prompts. Principais características:

- **Estruturado**: Usa tags XML para organizar o prompt
- **Versionável**: Pode ser tratado como código (git, diffs, etc)
- **Reutilizável**: Suporta variáveis e interpolação
- **Independente**: Funciona com qualquer modelo LLM

## Tags POML Principais

### Tags Básicas

- `<poml>` - Tag raiz obrigatória
- `<role>` - Define o papel/persona do agente
- `<task>` - Define a tarefa a ser executada
- `<output-format>` - Especifica o formato esperado da resposta

### Variáveis

- `<let name="var">valor</let>` - Define variável local (dentro do .poml)
- `{{ variable }}` - Interpolação de variável (pode vir do Python ou `<let>`)

### Estruturação

- `<list listStyle="decimal">` - Lista numerada
- `<list listStyle="dash">` - Lista com traços (-)
- `<list listStyle="star">` - Lista com asteriscos (*)
- `<list listStyle="plus">` - Lista com plus (+)
- `<list listStyle="latin">` - Lista com letras (a, b, c...)
- `<item>` - Item de lista
- `<p>` - Parágrafo
- `<b>` - Texto em negrito
- `<!-- comentário -->` - Comentários XML

## Regras para Criar Novos Arquivos POML

### 1. Estrutura Obrigatória

Todo arquivo .poml DEVE:
- Começar e terminar com tag `<poml>`
- Ter pelo menos uma das tags: `<role>` ou `<task>`
- Usar indentação de 2 espaços
- Ter encoding UTF-8

### 2. Convenções de Nomenclatura

- **Arquivo**: snake_case, descritivo do propósito (ex: `kindle.poml`, `github_issue.poml`)
- **Variáveis**: snake_case (ex: `target_url`, `item_count`)

### 3. Estrutura Recomendada

```xml
<poml>
  <!-- 1. Definição de variáveis locais (opcional) -->
  <let name="variable">valor padrão</let>
  
  <!-- 2. Definição do papel do agente -->
  <role>
    Descrição clara do papel, responsabilidades e prioridades do agente.
  </role>
  
  <!-- 3. Definição da tarefa -->
  <task>
    <list listStyle="decimal">
      <item>Passo 1 com {{ variables }} interpoladas</item>
      <item>Passo 2</item>
      <item>Passo N</item>
    </list>
  </task>
  
  <!-- 4. Formato de saída (opcional mas recomendado) -->
  <output-format>
    Especificação clara de como a resposta deve ser formatada.
  </output-format>
</poml>
```

### 4. Boas Práticas

#### Variáveis
- Use `<let>` para valores padrão que podem ser sobrescritos
- Comente variáveis que devem vir obrigatoriamente do Python:
  ```xml
  <!-- <let name="item_count">3</let> -->
  ```
- Use nomes descritivos e autoexplicativos

#### Role (Papel)
- Seja específico sobre o domínio (ex: "agente de automação web", "assistente de código")
- Defina prioridades claras (ex: "Sua prioridade é precisão")
- Mencione restrições se houver

#### Task (Tarefa)
- Use listas numeradas para sequências de passos
- Seja específico e objetivo em cada passo
- Interpole variáveis claramente com `{{ variavel }}`
- Evite ambiguidade

#### Output Format
- Especifique formato exato esperado
- Use exemplos quando possível
- Seja explícito sobre o que NÃO incluir (ex: "apenas a lista, sem explicações")

### 5. Exemplos de Casos de Uso

#### Prompt Simples (Interativo)
Quando o prompt precisa de input do usuário via CLI:
```xml
<poml>
  <role>You are a helpful assistant.</role>
  <task>Greet {{name}} warmly.</task>
</poml>
```

#### Prompt de Automação
Quando o prompt instrui um agente a realizar ações:
```xml
<poml>
  <let name="url">https://example.com</let>
  
  <role>
    Você é um agente de automação web especializado em extração de dados.
  </role>
  
  <task>
    <list listStyle="decimal">
      <item>Navegue até {{ url }}</item>
      <item>Extraia dados específicos</item>
      <item>Valide os dados extraídos</item>
    </list>
  </task>
  
  <output-format>
    JSON com estrutura:
    {"data": [...], "status": "success"}
  </output-format>
</poml>
```

#### Prompt de Análise
Quando o prompt pede análise de dados/código:
```xml
<poml>
  <role>Você é um especialista em análise de código.</role>
  
  <task>
    Analise o código em {{ file_path }} e identifique:
    <list listStyle="bullet">
      <item>Problemas de performance</item>
      <item>Vulnerabilidades de segurança</item>
      <item>Oportunidades de refatoração</item>
    </list>
  </task>
  
  <output-format>
    Relatório estruturado com seções para cada categoria de problema.
  </output-format>
</poml>
```

## Fluxo de Criação de Novo Template

Quando um usuário pedir para criar um novo template POML:

1. **Entender o caso de uso**
   - Qual é o objetivo do prompt?
   - Quais variáveis são necessárias?
   - Qual agente/modelo vai consumir isso?

2. **Criar o arquivo .poml**
   - Nome descritivo em snake_case
   - Seguir estrutura recomendada acima
   - Incluir todas as tags necessárias

3. **Criar o script Python correspondente**
   - Arquivo em `src/` com mesmo nome base
   - Definir contexto (variáveis)
   - Carregar template com `utils.load()`
   - Copiar para clipboard com `utils.copy()`

4. **Testar o fluxo completo**
   - Executar com `uv run main.py` e escolher o script no menu
   - OU executar diretamente com `uv run src/nome_do_script.py`
   - Verificar se o output no clipboard está correto
   - Testar com um LLM se possível

## Script Python Template

```python
import utils

# input obtido (se necessário)
# utils.clear()
# name = input("Prompt: ").strip()

# context definition
context = {
    "variable1": "valor1",
    "variable2": "valor2"
}

# output captured
output = utils.load("nome_do_arquivo.poml", context)

# output copied to clipboard
utils.copy(output)
```

## Validação de Qualidade

Um bom arquivo POML deve:
- ✅ Ter estrutura XML válida
- ✅ Ter role E/OU task definidos
- ✅ Usar variáveis de forma consistente
- ✅ Ter output-format quando a resposta é estruturada
- ✅ Ser autoexplicativo (comentários quando necessário)
- ✅ Seguir convenções de nomenclatura
- ✅ Ter indentação consistente (2 espaços)

## Recursos

- [Documentação oficial POML](https://github.com/poml-lang/poml)
