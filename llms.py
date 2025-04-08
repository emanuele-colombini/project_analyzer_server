from crewai import LLM

openrouter__qwen = LLM(
    model='openrouter/qwen/qwen-2.5-coder-32b-instruct:free',
    api_key='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',
    temperature=0.1
)

geai__openai_assistant = LLM(
    model='openai/saia:assistant:ec_crewai_agents',
    api_base='https://api.beta.saia.ai/chat',
    api_key='coder_assistant_8TUnVI_h6Az_BxSa2NqSsXr4Udo35OQwOqc0fLyey9yHebo1XEkQwNFODPct0K9MXZ3GEa1uOiKJHdmY-xmqhg',
    temperature=0.1
)

ollama__gemma = LLM(
    model='ollama/deepseek-r1:8b',
    base_url="http://localhost:11434",
    temperature=0.1
)

ollama__memory_embedder = {
    "provider": "ollama",
    "config": {
        "model": "nomic-embed-text"
    }
}

global_llm = geai__openai_assistant
