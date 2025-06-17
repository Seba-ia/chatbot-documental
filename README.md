# chatbot-documental
Este proyecto es parte de una actividad práctica para el ramo de Inteligencia Artificial.  
Consiste en la construcción de un chatbot que responde preguntas basadas en el contenido de un documento PDF vectorizado localmente.
## ✅ Fases del proyecto

### Fase 1 – Configuración del entorno
- Instalación de GitHub, Cursor, Python y Ollama.
- Creación del repositorio y estructura del proyecto.

### Fase 2 – Obtención de información
- Selección de un documento PDF académico sobre chatbots en educación.
- Instalación del modelo de lenguaje local `tinyllama` usando Ollama.

### Fase 3 – Procesamiento del documento
- Extracción del texto desde el PDF (`01_extract_text.py`)
- División del texto en fragmentos útiles (`02_split_fragments.py`)
- Generación de vectores (embeddings) con `sentence-transformers` (`03_generate_vectors.py`)
- Guardado de los vectores en `data/vectors/`

---

## 🧠 Fase 4 – Construcción del chatbot (en desarrollo)
- Conexión del modelo LLM con los vectores
- Implementación de búsqueda semántica (KNN)
- Interfaz de conversación local

---

## 📁 Estructura del proyecto
hey
