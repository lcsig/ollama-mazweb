"""
Configuration module for Ollama-MazWeb System
"""

from .models import MODELS
from .prompt_modes import PROMPT_MODES, SYSTEM_PROMPTS
from .app_config import APP_CONFIG
from .utils import get_system_prompt, get_default_model, get_default_prompt_mode, is_valid_model

__all__ = [
    'MODELS',
    'PROMPT_MODES',
    'SYSTEM_PROMPTS',
    'APP_CONFIG',
    'get_system_prompt',
    'get_default_model',
    'get_default_prompt_mode',
    'is_valid_model'
]

# Complete configuration object for backwards compatibility
CONFIG = {
    "models": MODELS,
    "prompt_modes": PROMPT_MODES,
    "system_prompts": SYSTEM_PROMPTS,
    **APP_CONFIG
}
