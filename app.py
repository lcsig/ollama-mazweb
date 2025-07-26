from flask import Flask, render_template, request, jsonify, Response, stream_with_context
import requests
import json
import hashlib
from config import CONFIG, get_system_prompt, get_default_model, get_default_prompt_mode, is_valid_model

app = Flask(__name__)
chat_histories = {}
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"

def cleanup_old_histories():
    """Basic cleanup - remove histories if we have too many"""
    MAX_HISTORIES = 50  # Adjust as needed
    if len(chat_histories) > MAX_HISTORIES:
        # Remove oldest entries (this is basic - could be improved with LRU)
        oldest_keys = list(chat_histories.keys())[:len(chat_histories) - MAX_HISTORIES]
        for key in oldest_keys:
            del chat_histories[key]

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/config", methods=["GET"])
def get_config():
    """Serve configuration to frontend"""
    return jsonify(CONFIG)

@app.route("/send", methods=["POST"])
def send():
    # Validate content type
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400
    
    data = request.json
    user_message = data.get("message")
    model = data.get("model", get_default_model()).strip()
    prompt_mode = data.get("prompt_mode", get_default_prompt_mode())
    custom_prompt = data.get("custom_prompt", "")

    if not user_message or not model:
        return jsonify({"error": "Missing message or model"}), 400
    
    # Validate model exists
    if not is_valid_model(model):
        return jsonify({"error": f"Invalid model: {model}"}), 400

    # Clean up old histories periodically
    cleanup_old_histories()

    # Create unique key for chat history based on model and prompt mode
    history_key = f"{model}_{prompt_mode}"
    if prompt_mode == "custom":
        # Add hash of custom prompt to make unique histories for different custom prompts
        custom_hash = hashlib.md5(custom_prompt.encode()).hexdigest()[:8]
        history_key = f"{model}_custom_{custom_hash}"

    if history_key not in chat_histories:
        # Get model properties for thinking capability check
        model_config = next((m for m in CONFIG["models"] if m["value"] == model), None)
        model_properties = model_config.get("properties", []) if model_config else []

        system_prompt = get_system_prompt(prompt_mode, custom_prompt, model_properties)
        chat_histories[history_key] = [
            {"role": "system", "content": system_prompt}
        ]

    chat_histories[history_key].append({"role": "user", "content": user_message})

    def generate_stream():
        try:
            response = requests.post(
                OLLAMA_URL,
                json={"model": model, "messages": chat_histories[history_key], "stream": True},
                stream=True,
                timeout=300,
            )
            
            # Check if request was successful
            response.raise_for_status()
            
            full_response = ""
            for line in response.iter_lines():
                if line:
                    try:
                        part = json.loads(line.decode("utf-8"))
                        chunk = part.get("message", {}).get("content", "")
                        full_response += chunk
                        yield chunk
                    except json.JSONDecodeError:
                        yield "[ERROR PARSING CHUNK]"
            chat_histories[history_key].append({"role": "assistant", "content": full_response})

        except requests.exceptions.RequestException as e:
            yield f"[API CONNECTION ERROR: {e}]"
        except Exception as e:
            yield f"[STREAMING ERROR: {e}]"

    return Response(stream_with_context(generate_stream()), mimetype="text/plain")

@app.route("/clear_history", methods=["POST"])
def clear_history():
    """Clear chat history for a specific model and prompt mode"""
    # Validate content type
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400
    
    data = request.json
    model = data.get("model", get_default_model()).strip()
    prompt_mode = data.get("prompt_mode", get_default_prompt_mode())
    custom_prompt = data.get("custom_prompt", "")
    
    # Create same key as in send route
    history_key = f"{model}_{prompt_mode}"
    if prompt_mode == "custom":
        custom_hash = hashlib.md5(custom_prompt.encode()).hexdigest()[:8]
        history_key = f"{model}_custom_{custom_hash}"
    
    if history_key in chat_histories:
        del chat_histories[history_key]
    
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True, port=7700)
