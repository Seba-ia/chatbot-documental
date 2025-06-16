import fitz  # PyMuPDF
import os

# Ruta al PDF
pdf_path = "data/pdf/Paperchatbot-Revisionliteraria.pdf"
output_path = "data/texto_extraido.txt"

# Verifica si el archivo existe
if not os.path.exists(pdf_path):
    print("⚠️ Archivo no encontrado:", pdf_path)
    raise FileNotFoundError(f"No se encontró el archivo: {pdf_path}")

# Abrir y extraer texto
print("Extrayendo texto del PDF...")
doc = fitz.open(pdf_path)
all_text = ""

for page in doc:
    all_text += page.get_text()

doc.close()

# Guardar texto extraído
with open(output_path, "w", encoding="utf-8") as f:
    f.write(all_text)
print("📂 Guardando texto extraído...")

print(f"✅ Texto extraído y guardado en: {output_path}")
