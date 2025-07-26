"""
Utility functions for configuration management
"""

from .models import MODELS
from .prompt_modes import PROMPT_MODES, SYSTEM_PROMPTS


def get_system_prompt(mode, custom_prompt=None, model_properties=None):
    """Get system prompt based on mode and model properties"""
    if mode == "custom":
        return custom_prompt or "You are a helpful AI assistant."

    # If model has thinking capability, automatically use thinking mode
    if model_properties and "Thinking" in model_properties:
        return SYSTEM_PROMPTS["thinking_mode"]

    return SYSTEM_PROMPTS.get(mode, SYSTEM_PROMPTS["general_assistant"])


def get_default_model():
    """Get the default model value"""
    for model in MODELS:
        if model.get("default", False):
            return model["value"]
    return MODELS[0]["value"] if MODELS else "llama3"


def get_default_prompt_mode():
    """Get the default prompt mode value"""
    for mode in PROMPT_MODES:
        if mode.get("default", False):
            return mode["value"]
    return PROMPT_MODES[0]["value"] if PROMPT_MODES else "general_assistant"


def is_valid_model(model):
    """Check if model exists in available models"""
    return any(m["value"] == model for m in MODELS)
