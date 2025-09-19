import os
from PIL import Image

# Path to your static image folder
IMAGE_DIR = os.path.join("static", "image")
OUTPUT_DIR = os.path.join("static", "image", "compressed")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def compress_image(input_path, output_path, quality=65, max_width=1600):
    """Resize & compress image while keeping sharpness."""
    img = Image.open(input_path)

    # Resize if too wide
    if img.width > max_width:
        ratio = max_width / img.width
        new_size = (max_width, int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)

    # Convert PNGs with transparency to RGB
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img.save(output_path, "JPEG", optimize=True, quality=quality)

# Loop through all images
for filename in os.listdir(IMAGE_DIR):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(IMAGE_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename.replace(".png", ".jpg"))

        compress_image(input_path, output_path)
        print(f"Compressed: {filename} → {output_path}")
