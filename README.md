# Fake News Detection Crew

A multi-agent AI system for detecting and fact-checking fake news, powered by [crewAI](https://crewai.com). Given a claim or news statement, a team of specialized AI agents searches the internet for evidence, analyzes its credibility, and produces a structured verdict report.

## How It Works

The crew runs three agents in a sequential pipeline:

| Agent | Role | Responsibility |
|---|---|---|
| `jurnalist` | Senior Investigative Journalist | Searches the internet for credible sources, studies, and official statements related to the claim |
| `fact_checker` | Truth Judge & Logic Analyst | Evaluates the gathered evidence and delivers a verdict (True / False / Partially False) with a confidence score (1–100) |
| `redactor` | Editor-in-Chief | Compiles the verdict into a clean, professionally formatted Markdown report |

### Tasks

1. **`research_task`** — The journalist searches the web for evidence (pro and con) and produces a research report with source links.
2. **`fact_check_task`** — The fact-checker analyzes the research report and outputs a verdict with a confidence score and main argument.
3. **`reporting_task`** — The editor assembles the final report saved to `raport_final.md`.

### Tools

- **Internet Search** (`Cautare pe Internet`) — A DuckDuckGo-powered search tool used by the journalist agent to retrieve live web results.

### LLM

The crew uses **Groq's `llama-3.3-70b-versatile`** model via [LiteLLM](https://docs.litellm.ai/) routing.

## Project Structure

```
agentic-ai-fake-news-crew/
├── knowledge/
│   └── user_preference.txt        # Optional user context injected into the crew
├── src/fake_news_crew/
│   ├── config/
│   │   ├── agents.yaml            # Agent definitions (role, goal, backstory)
│   │   └── tasks.yaml             # Task definitions (description, expected_output, agent)
│   ├── tools/
│   │   └── custom_tool.py         # Scaffold for additional custom tools
│   ├── crew.py                    # Crew orchestration (agents, tasks, LLM, tools)
│   └── main.py                    # Entry point — defines the input claim and runs the crew
├── raport_final.md                # Generated output report (created after each run)
├── pyproject.toml
└── .env                           # API keys
```

## Installation

Ensure you have Python >=3.10, <3.14 installed. This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Install uv if you haven't already
pip install uv

# Install project dependencies
crewai install
```

## Configuration

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

To change the claim being fact-checked, edit the `subiect` input in `src/fake_news_crew/main.py`:

```python
input_date = {
    'subiect': 'Your claim or news statement here.'
}
```

You can also customize agents and tasks:

- `src/fake_news_crew/config/agents.yaml` — agent roles, goals, and backstories
- `src/fake_news_crew/config/tasks.yaml` — task descriptions and expected outputs
- `src/fake_news_crew/crew.py` — LLM settings, tool assignments, crew process

## Running the Project

```bash
crewai run
```

The crew will research the claim, analyze the evidence, and write the verdict to `raport_final.md` in the project root.

### Example Output

The generated report (`raport_final.md`) includes:

1. The original claim
2. Verdict — **True / False / Partially False**
3. Confidence score (1–100)
4. Detailed explanation
5. List of sources with links

See [`raport_final.md`](raport_final.md) for an example output from a run on the claim:
> *"A miraculous and secret cancer treatment using warm water with lemon on an empty stomach has been discovered."*

## Support

- [crewAI Documentation](https://docs.crewai.com)
- [crewAI GitHub](https://github.com/joaomdmoura/crewai)
- [Join the Discord](https://discord.com/invite/X4JWnZnxPb)
