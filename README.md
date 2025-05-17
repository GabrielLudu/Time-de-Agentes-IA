# 🚀 Time de Agentes IA: Automação Completa de MVP

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-AI-orange)
![Rich](https://img.shields.io/badge/terminal-rich-green)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)

## Sumário

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Uso](#uso)
- [Exemplo de Saída](#exemplo-de-saída)
- [Contribuição](#contribuição)
- [FAQ](#faq)
- [Licença](#licença)

---

## Sobre

O **Time de Agentes IA** é um projeto que simula uma equipe completa de desenvolvimento de software para criar seu MVP, automatizando cada etapa com agentes especializados do Google Gemini:

> "Do planejamento à documentação, acelere seu ciclo de desenvolvimento com IA."

---

## Funcionalidades

- 🔍 **Análise de Viabilidade**: avalia mercado, riscos, custos e prazos.
- 📋 **Requisitos**: gera requisitos funcionais, não-funcionais e critérios de aceitação.
- 🎨 **Arquitetura & UX/UI**: cria design de alto nível e wireframes textuais.
- 🗂 **Backlog & Roadmap**: organiza user stories e define entregas do MVP.
- 💻 **Implementação Front-end**: esboça componentes e estilo (React/Vue/HTML-CSS).
- 🖥 **Implementação Back-end**: define APIs, modelos de dados e integrações (Flask/Node/Django).
- ✅ **Testes & QA**: elabora casos de teste unitários, de integração e manuais.
- 🚀 **DevOps (CI/CD & Deploy)**: configura pipeline, containerização e deploy.
- 📚 **Documentação**: gera arquivos JSON, Markdown e guias de uso.

---

## Instalação

1. **Clone** o repositório:

   ```bash
   git clone https://github.com/GabrielLudu/Time-de-Agentes-IA.git
   cd Time-de-Agentes-IA
   ```

2. **Ambiente Virtual**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .\.venv\Scripts\activate # Windows
   ```

3. **Instale** dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure** variáveis de ambiente:

   ```bash
   cp .env.example .env
   # Edite .env e defina GOOGLE_API_KEY
   ```

---

## Uso

Execute o script principal e siga as instruções no terminal:

```bash
python main.py
```

1. Insira a **Visão Geral** do produto.
2. Acompanhe painéis Rich exibindo cada etapa.
3. Encontre os relatórios em `outputs/relatorio.json` e `outputs/relatorio.md`.

---

## ⚠️ Aviso Importante

> Os resultados são gerados automaticamente por inteligência artificial e podem conter imprecisões ou erros. Sempre revise manualmente antes de usar em produção.

## Exemplo de Saída

### JSON

```json
{
  "viabilidade": "– Mercado: alta demanda\n– Custo: R$120k\n…",
  "requisitos": "- RF1: …\n- RNF1: …",
  "frontend": "import React...",
  "backend": "from flask import Flask..."
}
```

### Terminal (Rich)

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 🔍 Análise de Viabilidade             ┃
┃ – Mercado: alta demanda               ┃
┃ – Riscos: integração de APIs          ┃
┃ – Cronograma: 3 meses                ┃
┃ – Recomendação: avançar com MVP      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

## FAQ

**Como mudar o modelo Gemini?**
Atualize o valor de `MODEL_ID` em `main.py` e reinicie o script.

**Posso usar outro framework front-end?**
Sim! Modifique a instrução em `agente_desenvolvimento_frontend` para seu framework preferido.

**Onde encontro os resultados?**
Em `outputs/relatorio.json` e `outputs/relatorio.md`, após a execução.

---

<p align="center">Feito por: Gabriel Luduvice</p>
