# Crew Agents Projects

Welcome to the Crew Agents Projects repository, powered by [crewAI](https://crewai.com). This repository contains multiple projects designed to help you set up multi-agent AI systems with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
python -m venv .venv
./.venv/Scripts/activate
pip install -r requirements.txt
```

make sure to copy the `env.sample` as `.env` and add the env variables.  
Use [ollama](https://ollama.com/) for local models.

## Projects

### 01_test_ai

This sample boilerplate project for crewAI.

- [pyproject.toml](01_test_ai/pyproject.toml)

### 02_ai_news

This project focuses on AI agents that gather and summarize news.

- [pyproject.toml](02_ai_news/pyproject.toml)

### 03_poem_flow

This project involves AI agents that generate and analyze poems introduced flows.

- [pyproject.toml](03_poem_flow/pyproject.toml)

### meeting_minutes

This project is designed for AI agents that take and summarize meeting minutes.

- [pyproject.toml](04_meeting_minutes/pyproject.toml)

### 05_pdf_rag

This project is designed for AI agents to chat with a pdf.

- [pyproject.toml](05_pdf_rag/pyproject.toml)

### 06_business_development

This project is designed for generating a business development report.

- [pyproject.toml](06_business_development/pyproject.toml)

## Installation

Ensure you have Python 3.12 installed on your system.

Next, navigate to your project directory and install the dependencies:

## Running the Projects

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
python .\src\<project>\main.py
```

This command initializes the crew, assembling the agents and assigning them tasks as defined in your configuration.

## Support

For support, questions, or feedback regarding any of the projects or crewAI:

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
