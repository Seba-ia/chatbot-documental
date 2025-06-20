import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Cargar embeddings y fragmentos
print("📦 Cargando embeddings y fragmentos...")
embeddings = np.load("data/vectors/embeddings.npy")

with open("data/vectors/fragments.txt", "r", encoding="utf-8") as f:
    fragments = f.read().split("\n---\n")

# Cargar modelo de embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

print("✅ Chatbot listo. Escribe tu pregunta (o 'salir' para terminar)")

while True:
    modo = input("🎛️ ¿Modo de respuesta? (tutor/resumen/definir): ").strip().lower()
    pregunta = input("🧠 Tu pregunta: ").strip()

    if pregunta.lower() in ["salir", "exit", "quit"]:
        print("👋 Adiós")
        break

    # Elegir el tipo de rol según el modo
    if modo == "resumen":
        rol = "Responde en español. Resume el siguiente contenido en español, destacando ideas clave:"
    elif modo == "definir":
        rol = "Responde en español. Define de manera clara y concisa el concepto consultado usando este contenido:"
    else:
        rol = "Responde en español. Actúa como un experto académico. Responde con base en el siguiente contenido:"

    # Vectorizar la pregunta
    pregunta_vec = model.encode([pregunta])
    similarities = cosine_similarity(pregunta_vec, embeddings)[0]
    best_index = np.argmax(similarities)
    contexto = fragments[best_index]

    # Armar prompt para Ollama
    prompt = f"""{rol}

\"\"\"{contexto}\"\"\"

Pregunta del usuario: {pregunta}
"""

    print("\n⏳ Generando respuesta...\n")

    # Llamada a la API local de Ollama
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",
            "prompt": prompt,
            "temperature": 0.7,
            "stream": False
        }
    )

    if response.status_code == 200:
        data = response.json()
        print("🗨️ Respuesta de tinyllama:\n")
        print(data["response"])
    else:
        print("❌ Error al comunicarse con Ollama:", response.status_code)
