# Summariser Agent

An AI-powered website summarisation tool that leverages OpenAI's language models to extract and summarise content from any website. The project is built with a modular architecture that separates configuration, website scraping, and summarisation logic, making it easily extendable for future integrations (such as weather data, additional LLMs, etc.).

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Extending the Project](#extending-the-project)
- [License](#license)

## Overview

The Summariser Agent is designed to:

- **Scrape Websites**: Use BeautifulSoup to fetch and clean HTML content.
- **Generate Summaries**: Leverage OpenAI's language models to summarise website content.
- **Orchestrate Services**: Use an agent to route tasks between different business logic modules.

By isolating functionality into dedicated modules and packages, the project adheres to best practices in modularity, scalability, and maintainability.

## Project Structure

```bash
my_project/
├── ai_assistant/
│   ├── agent.py          # Orchestrator that delegates tasks (e.g., summarisation)
│   └── summariser_agent/ # Dedicated package for summarisation logic
│       ├── __init__.py
│       ├── config.py     # Loads env vars, validates API key, and creates shared objects
│       ├── website.py    # Website scraper using BeautifulSoup
│       ├── utils.py      # Utility functions (e.g., get_system_prompt)
│       └── summariser.py # Summariser that calls the LLM for generating summaries
├── src/
│   └── main.py           # Entry point for CLI usage of the agent
├── .env                  # Environment variables file (API keys, etc.)
└── requirements.txt      # Python dependencies
```
# Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/summariser-agent.git
cd summariser-agent
```
Create and activate a virtual environment:
```bash
git clone https://github.com/yourusername/summariser-agent.git
cd summariser-agent
```
