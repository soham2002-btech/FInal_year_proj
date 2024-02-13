from flask import Flask, request, jsonify
from Speech_to_text import speech_to_text
from Text_to_speech import text_to_speech
from Answer_generation_by_mistralai import question
from Language_translation import translate_to_hindi

app = Flask(__name__)



@app.route("/translate", methods=["POST"])
def translate_text_speech(text):
    Translated_text = translate_to_hindi(text)
    speech = text_to_speech(Translated_text)
    return speech

@app.route("/answer_question", methods=["POST"])
def answer_question(audio):
    # Get question text from user
    audio = request.form["audio"]
    text = speech_to_text(audio)
    answer = question(text)
    speech = text_to_speech(answer)
    return speech

def answer_question_with_mistral(question):
    # Placeholder function to simulate answering questions using Mistral model
    return "This is a placeholder answer."

if __name__ == "__main__":
    app.run(debug=True)
