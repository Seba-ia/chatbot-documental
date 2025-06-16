import os

# Rutas
input_path = "data/texto_extraido.txt"
output_path = "data/fragments.txt"

print("📁 Verificando existencia del archivo...")

# Verificar si el archivo existe
if not os.path.exists(input_path):
    print(f"⚠️ No se encontró el archivo: {input_path}")
    exit()

print("📖 Leyendo texto completo...")

# Leer el texto completo
with open(input_path, "r", encoding="utf-8") as f:
    full_text = f.read()

print(f"🔠 Longitud del texto leído: {len(full_text)} caracteres")

# Dividir en fragmentos por saltos de línea dobles (párrafos)
fragmentos_raw = full_text.split("\n")
fragments = [frag.strip() for frag in fragmentos_raw if len(frag.strip()) > 40]

print(f"✂️ Bloques crudos detectados: {len(fragmentos_raw)}")
print(f"✅ Fragmentos útiles (más de 40 caracteres): {len(fragments)}")

# Guardar los fragmentos
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n---\n".join(fragments))

print(f"📄 Fragmentos guardados en: {output_path}")
