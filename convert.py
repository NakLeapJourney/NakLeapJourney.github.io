import os
from PIL import Image
import pillow_heif

# Register HEIF format with Pillow
pillow_heif.register_heif_opener()

# Root folder containing HEIC images
PHOTO_DIR = 'photo'

# Counter for sequential file naming across all subfolders
counter = 1

# Walk through all subfolders and files
for root, dirs, files in os.walk(PHOTO_DIR):
    for file in files:
        if file.lower().endswith('.heic'):
            heic_path = os.path.join(root, file)

            try:
                # Open HEIC image and convert to RGB
                image = Image.open(heic_path).convert("RGB")

                # New JPG filename with sequential numbering
                new_filename = f"{counter}.jpg"

                # Save JPG in the SAME folder as the original HEIC
                jpg_path = os.path.join(root, new_filename)

                # Save as high quality JPEG
                image.save(jpg_path, "JPEG", quality=100, subsampling=0)

                # # Delete the original HEIC file
                # os.remove(heic_path)

                print(f"Converted and saved: {jpg_path}")
                counter += 1

            except Exception as e:
                print(f"Error converting {heic_path}: {e}")
