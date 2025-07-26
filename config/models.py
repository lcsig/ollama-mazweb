"""
Model configurations for Ollama-MazWeb System
"""

MODELS = [
    {
        "value": "dolphin-llama3:8b",
        "name": "Dolphin Llama3 8B",
        "default": True,
        "properties": [],
        "ollama_url": "https://ollama.com/library/dolphin-llama3"
    },
    {
        "value": "aqualaguna/gemma-3-27b-it-abliterated-GGUF:q2_k",
        "name": "Gemma 3 27B Abliterated",
        "default": False,
        "properties": [],
        "ollama_url": "https://ollama.com/aqualaguna/gemma-3-27b-it-abliterated-GGUF"
    },
    {
        "value": "goekdenizguelmez/JOSIEFIED-Qwen3:8b",
        "name": "JOSIEFIED Qwen3 8B",
        "default": False,
        "properties": ["Thinking", "Tools"],
        "ollama_url": "https://ollama.com/goekdenizguelmez/JOSIEFIED-Qwen3"
    },
    {
        "value": "huihui_ai/jan-nano-abliterated:4b",
        "name": "Jan Nano Abliterated 4B",
        "default": False,
        "properties": ["Thinking", "Tools"],
        "ollama_url": "https://ollama.com/huihui_ai/jan-nano-abliterated"
    },
    {
        "value": "dolphin-mixtral:8x7b",
        "name": "Dolphin Mixtral 8x7B",
        "default": False,
        "properties": [],
        "ollama_url": "https://ollama.com/library/dolphin-mixtral"
    }
]
