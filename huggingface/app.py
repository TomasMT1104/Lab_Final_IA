import gradio as gr
from transformers import pipeline

# Cargar modelo de sentimiento
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    if not text.strip():
        return "Por favor ingresa un texto."
    result = classifier(text)[0]
    label = result["label"]
    score = round(result["score"], 4)
    return f"Sentimiento: {label} (confianza: {score})"

# Interfaz Gradio
demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=3, label="Texto de entrada"),
    outputs=gr.Textbox(label="Resultado"),
    title="Análisis de Sentimiento - ia-prof",
    description="Modelo de análisis de sentimiento basado en DistilBERT."
)

demo.launch()
