from flask import Flask, request, jsonify, render_template
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from googletrans import Translator
import torch

app = Flask(__name__)

# Inicjalizacja tłumacza
translator = Translator()

# Wybór modelu GPT-2 Large
model_name = "gpt2-large"

# Ładowanie modelu i tokenizer'a
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Dodanie tokenu padding, aby uniknąć ostrzeżeń
model.config.pad_token_id = model.config.eos_token_id

def generate_response(prompt, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones_like(inputs)  # Tworzenie maski uwagi

    outputs = model.generate(
        inputs,
        attention_mask=attention_mask,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        no_repeat_ngram_size=no_repeat_ngram_size,
        top_k=top_k,
        top_p=top_p,
        temperature=temperature,
        do_sample=True
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

@app.route('/')
def index():
    return render_template('Page.html')

@app.route('/chat')
def chat_page():
    return render_template('Chatbot.html')

@app.route('/game')
def gra():
    return render_template('Game.html')

@app.route('/page')
def strona():
    return render_template('Page.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get("message")
        if user_input:
            translated_input = translator.translate(user_input, src='pl', dest='en').text
            response = generate_response(translated_input)
            translated_response = translator.translate(response, src='en', dest='pl').text
            return jsonify({"response": translated_response})
        return jsonify({"response": "Proszę podać pytanie."})
    except Exception as e:
        return jsonify({"response": f"Wystąpił błąd: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)