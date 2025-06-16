import os
import numpy as np
from sentence_transformers import SentenceTransformer

# Rutas
input_path = "data/fragments.txt"
output_dir = "data/vectors"
os.makedirs(output_dir, exist_ok=True)

# Leer fragmentos
print("📄 Leyendo fragmentos...")
with open(input_path, "r", encoding="utf-8") as f:
    fragments = [frag.strip() for frag in f.read().split("\n---\n") if frag.strip()]

print(f"🧩 Cantidad de fragmentos: {len(fragments)}")

# Cargar modelo
print("📦 Cargando modelo de embeddings (all-MiniLM-L6-v2)...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generar vectores
print("🔢 Generando vectores...")
embeddings = model.encode(fragments, show_progress_bar=True)

# Guardar resultados
np.save(os.path.join(output_dir, "embeddings.npy"), embeddings)

with open(os.path.join(output_dir, "fragments.txt"), "w", encoding="utf-8") as f:
    f.write("\n---\n".join(fragments))

print(f"✅ Embeddings guardados en: {os.path.join(output_dir, 'embeddings.npy')}")
print(f"📝 Fragmentos guardados en: {os.path.join(output_dir, 'fragments.txt')}")
