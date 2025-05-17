from dotenv import load_dotenv
import os
import json
from rich.console import Console
from rich.panel import Panel
from google import genai
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("Defina a variável de ambiente GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key

console = Console()

client = genai.Client()
MODEL_ID = "gemini-2.0-flash"

def call_agent(agent: Agent, prompt: str) -> str:
    session_service = InMemorySessionService()
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    content = types.Content(role="user", parts=[types.Part(text=prompt)])
    response = ""
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
            for part in event.content.parts:
                if part.text:
                    response += part.text.strip() + "\n"
    return response

def agente_viabilidade(visao_geral: str) -> str:
    agent = Agent(
        name="agente_viabilidade",
        model=MODEL_ID,
        instruction="""
Você é um Analista de Viabilidade de Projetos de Software. Deve usar a ferramenta de buscad do Google (google_search) para pesquisar e avaliar viabilidade técnica, mercado, risco, custos e prazos.
Forneça sumário executivo e recomendação se prosseguir.
""",
        description="Avalia viabilidade do projeto",
        tools=[google_search]
    )
    prompt = f"Visão geral do produto: {visao_geral}"
    return call_agent(agent, prompt)

def agente_requisitos(visao_geral: str, analise_viabilidade: str) -> str:
    agent = Agent(
        name="agente_requisitos",
        model=MODEL_ID,
        instruction="""
Você é um Engenheiro de Requisitos. Gere lista de requisitos funcionais e não funcionais e critérios de aceitação.
""",
        description="Define requisitos do produto"
    )
    prompt = f"Visão geral: {visao_geral}\nAnálise de Viabilidade: {analise_viabilidade}"
    return call_agent(agent, prompt)

def agente_design(requisitos: str) -> str:
    agent = Agent(
        name="agente_design",
        model=MODEL_ID,
        instruction="""
Você é um Arquiteto de Software e Designer de UX/UI. Crie arquitetura de alto nível, componentes e wireframes textuais.
""",
        description="Design de arquitetura e UX/UI"
    )
    prompt = f"Requisitos: {requisitos}"
    return call_agent(agent, prompt)

def agente_planejamento(design: str) -> str:
    agent = Agent(
        name="agente_planejamento",
        model=MODEL_ID,
        instruction="""
Você é um Gerente de Projetos Ágil. Converta design em backlog de user stories e defina release plan para MVP.
""",
        description="Planejamento Ágil"
    )
    prompt = f"Design: {design}"
    return call_agent(agent, prompt)

def agente_desenvolvimento_frontend(stories: str) -> str:
    agent = Agent(
        name="agente_desenvolvimento_frontend",
        model=MODEL_ID,
        instruction="""
Você é um Desenvolvedor Front-end Sênior. Para cada user story, forneça esboço de código React/HTML-CSS, estrutura de componentes, estado e estilo.
""",
        description="Gera código front-end"
    )
    prompt = f"Backlog de Stories: {stories}"
    return call_agent(agent, prompt)

def agente_desenvolvimento_backend(stories: str) -> str:
    agent = Agent(
        name="agente_desenvolvimento_backend",
        model=MODEL_ID,
        instruction="""
Você é um Desenvolvedor Back-end Sênior. Para cada user story, forneça esboço de código em Flask/Node.js/Django, definições de rotas, modelos de dados e integrações.
""",
        description="Gera código back-end"
    )
    prompt = f"Backlog de Stories: {stories}"
    return call_agent(agent, prompt)


def agente_teste(impl_front: str, impl_back: str) -> str:
    agent = Agent(
        name="agente_teste",
        model=MODEL_ID,
        instruction="""
Você é um Engenheiro de QA. Baseado na implementação front-end e back-end, crie casos de teste unitários, integração e manuais.
""",
        description="Define testes do MVP"
    )
    prompt = f"Implementação front-end: {impl_front}\nImplementação back-end: {impl_back}"
    return call_agent(agent, prompt)


def agente_devops(impl_back: str) -> str:
    agent = Agent(
        name="agente_devops",
        model=MODEL_ID,
        instruction="""
Você é um Engenheiro DevOps. Defina configuração de CI/CD, containerização, scripts de deploy e infra para API e serviços.
""",
        description="CI/CD e Deploy"
    )
    prompt = f"Código back-end: {impl_back}"
    return call_agent(agent, prompt)


def agente_documentacao(all_info: str) -> str:
    agent = Agent(
        name="agente_documentacao",
        model=MODEL_ID,
        instruction="""
Você é um Redator Técnico. Produza README completo, guia de instalação e uso do front-end e back-end do MVP.
""",
        description="Documentação do produto"
    )
    prompt = f"Informações do projeto: {all_info}"
    return call_agent(agent, prompt)

if __name__ == "__main__":
    visao = console.input("[bold cyan]Descreva brevemente a visão geral do produto[/]: ")
    responses = {}

    vfm = agente_viabilidade(visao)
    responses["viabilidade"] = vfm
    console.print(Panel(vfm, title="🔍 Análise de Viabilidade", expand=False))

    reqs = agente_requisitos(visao, vfm)
    responses["requisitos"] = reqs
    console.print(Panel(reqs, title="📋 Requisitos", expand=False))

    design = agente_design(reqs)
    responses["design"] = design
    console.print(Panel(design, title="🎨 Arquitetura & UX/UI", expand=False))

    backlog = agente_planejamento(design)
    responses["backlog"] = backlog
    console.print(Panel(backlog, title="🗂 Backlog & Roadmap", expand=False))

    impl_front = agente_desenvolvimento_frontend(backlog)
    responses["frontend"] = impl_front
    console.print(Panel(impl_front, title="💻 Implementação Front-end", expand=False))

    impl_back = agente_desenvolvimento_backend(backlog)
    responses["backend"] = impl_back
    console.print(Panel(impl_back, title="🖥 Implementação Back-end", expand=False))

    tests = agente_teste(impl_front, impl_back)
    responses["testes"] = tests
    console.print(Panel(tests, title="✅ Casos de Teste & QA", expand=False))

    devops = agente_devops(impl_back)
    responses["devops"] = devops
    console.print(Panel(devops, title="🚀 DevOps (CI/CD & Deploy)", expand=False))

    docs = agente_documentacao("\n".join(responses.values()))
    responses["documentacao"] = docs
    console.print(Panel(docs, title="📚 Documentação Completa", expand=False))

    out_dir = "outputs"
    os.makedirs(out_dir, exist_ok=True)
    json_path = os.path.join(out_dir, "relatorio.json")
    md_path = os.path.join(out_dir, "relatorio.md")

    with open(json_path, "w", encoding="utf-8") as f_json:
        json.dump(responses, f_json, ensure_ascii=False, indent=2)

    md_content = []
    titles = {
        "viabilidade": "Análise de Viabilidade",
        "requisitos": "Requisitos",
        "design": "Arquitetura & UX/UI",
        "backlog": "Backlog & Roadmap",
        "frontend": "Implementação Front-end",
        "backend": "Implementação Back-end",
        "testes": "Casos de Teste & QA",
        "devops": "DevOps (CI/CD & Deploy)",
        "documentacao": "Documentação Completa"
    }
    for key, text in responses.items():
        md_content.append(f"## {titles[key]}\n\n{text}\n")
    with open(md_path, "w", encoding="utf-8") as f_md:
        f_md.write("# Relatório de MVP\n\n" + "\n".join(md_content))

    console.print(f"\n[green]✅ Relatório salvo em:[/] {json_path} e {md_path}")