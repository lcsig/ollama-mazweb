# 🧠 Ollama-MazWeb System

A modern, responsive web-based chat interface for interacting with local LLMs via Ollama. Features multiple model support, customizable system prompts, and real-time streaming responses with markdown rendering.

![Chat Interface](https://img.shields.io/badge/Interface-Modern_Web_UI-blue)
![Models](https://img.shields.io/badge/Models-Multiple_LLM_Support-green)
![Streaming](https://img.shields.io/badge/Responses-Real--time_Streaming-orange)

## 📸 Interface Preview

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="img/chat-interface-screenshot.png" alt="Ollama-MazWeb Chat Interface" width="400">
        <br>
        <em>Modern chat interface with dark sidebar</em>
      </td>
      <td align="center">
        <img src="img/thinking-mode.png" alt="Thinking Mode Feature" width="400">
        <br>
        <em>Thinking mode with step-by-step reasoning</em>
      </td>
    </tr>
  </table>
</div>

## ✨ Features

- 🤖 **Multiple Model Support** - Switch between different LLM models seamlessly
- 🎨 **Modern UI** - Clean, responsive chat interface with dark sidebar
- ⚡ **Real-time Streaming** - See responses as they're generated
- 📝 **Markdown Rendering** - Properly formatted code blocks, lists, and text styling
- 🛠️ **Customizable Prompts** - Built-in assistant modes + custom system prompts
- 💾 **Chat History** - Persistent conversations per model/prompt combination
- 🔄 **Easy Model Switching** - Change models without losing context

## 📋 Prerequisites

Before getting started, ensure you have:

- **Python 3.10+** installed on your system
- **Ollama** installed and running

## 🚀 Installation & Setup

### 1. Install Ollama

**On Linux (Ubuntu/Debian with Snap):**
```bash
sudo snap install ollama
```

**On macOS:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**On Windows:**
Download and install from [ollama.ai](https://ollama.ai/download)

### 2. Start Ollama Service

```bash
ollama serve
```

*Keep this terminal open - Ollama needs to be running for the chat system to work.*

### 3. Install Required Models

The chat system is pre-configured with multiple models. Install the recommended ones using these commands:

**Dolphin Llama3 8B (Default - Recommended):** [📋 Model Page](https://ollama.com/library/dolphin-llama3)
```bash
ollama pull dolphin-llama3:8b
```

**Gemma 3 27B Abliterated (More Capable - Slower):** [📋 Model Page](https://ollama.com/aqualaguna/gemma-3-27b-it-abliterated-GGUF)
```bash
ollama pull aqualaguna/gemma-3-27b-it-abliterated-GGUF:q2_k
```

**JOSIEFIED Qwen3 8B (Thinking & Tools Support):** [📋 Model Page](https://ollama.com/goekdenizguelmez/JOSIEFIED-Qwen3)
```bash
ollama pull goekdenizguelmez/JOSIEFIED-Qwen3:8b
```

**Jan Nano Abliterated 4B (Lightweight with Thinking & Tools):** [📋 Model Page](https://ollama.com/huihui_ai/jan-nano-abliterated)
```bash
ollama pull huihui_ai/jan-nano-abliterated:4b
```

**Dolphin Mixtral 8x7B (Large Multi-Expert Model):** [📋 Model Page](https://ollama.com/library/dolphin-mixtral)
```bash
ollama pull dolphin-mixtral:8x7b
```

*Note: You can install any combination of these models. The system will automatically detect available models. Models with "Thinking" and "Tools" properties offer enhanced reasoning capabilities.*

### 4. Clone & Setup Chat System

```bash
git clone <your-repo-url>
cd llm
```

### 5. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

Open your browser and navigate to: **http://localhost:7700**

## 🎯 Usage

### Model Selection
- Use the **Model** dropdown in the sidebar to switch between installed models
- The system will maintain separate chat histories for each model

### Assistant Modes

#### 🤖 General Assistant (Default)
- Helpful, knowledgeable, and unrestricted AI assistant
- Great for general questions and conversations

#### 👨‍💻 Senior Software Engineer  
- Technical expert with 10+ years of experience
- Provides detailed technical explanations and code examples
- Focuses on best practices, architecture, and clean code

#### 🤔 Thinking Mode
- **Step-by-step reasoning display** - Shows the AI's thought process before providing answers
- **Special visual styling** - Thinking blocks are highlighted with a distinctive purple border and "🤔 Thinking..." header
- **Real-time streaming** - Watch the AI's reasoning unfold in real-time as it types
- **Structured format** - Uses `<thinking>` tags to separate reasoning from final answers
- **Enhanced transparency** - Perfect for complex problems where you want to see the logic behind the solution
- **Visual indicators** - Thinking content appears in italicized, bordered blocks for easy identification

#### ✏️ Custom Prompt
- Define your own system prompt
- Perfect for specialized use cases or specific personas

### Chat Features

- **Send Messages**: Type your message and press Enter or click Send
- **Clear History**: Use "New Chat" or "Clear History" to start fresh
- **Markdown Support**: Responses support **bold**, *italic*, `code`, and lists
- **Code Blocks**: Multi-line code is properly formatted and syntax highlighted

## ⚙️ Configuration

### Adding New Models

1. **Install the model via Ollama:**
   ```bash
   ollama pull model-name:tag
   ```

2. **Add to config/models.py:**
   ```python
   MODELS = [
       # ...existing models...
       {
           "value": "model-name:tag",
           "name": "Display Name",
           "default": False,  # Set to True to make it default
           "properties": [],
           "ollama_url": "https://ollama.com/library/model-name"
       }
   ]
   ```

### Custom System Prompts

Add new prompt modes by editing the configuration files:

**1. Add the mode to config/prompt_modes.py:**
```python
PROMPT_MODES = [
    # ...existing modes...
    {
        "value": "your_mode",
        "name": "Your Custom Mode",
        "default": False
    }
]

SYSTEM_PROMPTS = {
    # ...existing prompts...
    "your_mode": "Your custom system prompt here..."
}
```

**2. The system will automatically load your new configurations on restart.**

## 🔧 Troubleshooting

### Common Issues

**"Connection refused" errors:**
- Ensure Ollama is running: `ollama serve`
- Check if Ollama is accessible: `curl http://localhost:11434/api/tags`

**Model not found:**
- Verify model is installed: `ollama list`
- Install missing models: `ollama pull model-name`

**Slow responses:**
- Larger models (27B) require more RAM and are slower
- Consider using smaller models (8B) for faster responses
- Close other applications to free up system resources

**Chat history not clearing:**
- Refresh the page if clear history doesn't work
- Check browser console for errors

### System Requirements

**Minimum:**
- 8GB RAM (for 8B models)
- 4GB free disk space

**Recommended:**
- 16GB+ RAM (for 27B models)  
- 8GB+ free disk space
- SSD for better performance

## 🗂️ Project Structure

```
llm/
├── app.py                      # Flask backend application
├── requirements.txt            # Python dependencies
├── LICENSE                     # MIT License file
├── README.md                   # This documentation
├── config/                     # Configuration modules
│   ├── __init__.py            # Package initialization
│   ├── app_config.py          # Application settings
│   ├── models.py              # Model configurations
│   ├── prompt_modes.py        # System prompts and modes
│   └── utils.py               # Utility functions
├── img/                       # Interface screenshots
│   ├── chat-interface-screenshot.png
│   └── thinking-mode.png
└── templates/
    └── chat.html              # Frontend chat interface
```

## 📝 API Endpoints

- `GET /` - Chat interface
- `GET /config` - Get application configuration
- `POST /send` - Send message and receive streaming response
- `POST /clear_history` - Clear chat history

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Verify Ollama is running and models are installed
3. Check the browser console for JavaScript errors
4. Open an issue with error details and system information

---

**Happy chatting! 🚀**
