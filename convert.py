# # import os
# # from PIL import Image
# # import pillow_heif

# # # Register HEIF format with Pillow
# # pillow_heif.register_heif_opener()

# # # Root folder containing HEIC images
# # PHOTO_DIR = 'photo'

# # # Counter for sequential file naming across all subfolders
# # counter = 1

# # # Walk through all subfolders and files
# # for root, dirs, files in os.walk(PHOTO_DIR):
# #     for file in files:
# #         if file.lower().endswith('.heic'):
# #             heic_path = os.path.join(root, file)

# #             try:
# #                 # Open HEIC image and convert to RGB
# #                 image = Image.open(heic_path).convert("RGB")

# #                 # New JPG filename with sequential numbering
# #                 new_filename = f"{counter}.jpg"

# #                 # Save JPG in the SAME folder as the original HEIC
# #                 jpg_path = os.path.join(root, new_filename)

# #                 # Save as high quality JPEG
# #                 image.save(jpg_path, "JPEG", quality=100, subsampling=0)

# #                 # Delete the original HEIC file
# #                 os.remove(heic_path)

# #                 print(f"Converted and saved: {jpg_path}")
# #                 counter += 1

# #             except Exception as e:
# #                 print(f"Error converting {heic_path}: {e}")



# import os

# # Root folder containing subfolders with images
# PHOTO_DIR = 'photo'

# # File extensions to consider (you can add more if needed)
# VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.heic', '.webp')

# # Loop through each subfolder
# for root, dirs, files in os.walk(PHOTO_DIR):
#     # Skip the root folder itself, process only subdirectories
#     if root == PHOTO_DIR:
#         continue

#     # Filter and sort files (optional: sort by name or time)
#     image_files = sorted([f for f in files if f.lower().endswith(VALID_EXTENSIONS)])

#     # Rename each image in the subfolder
#     for idx, filename in enumerate(image_files, start=1):
#         ext = os.path.splitext(filename)[1].lower()
#         new_name = f"{idx}{ext}"
#         old_path = os.path.join(root, filename)
#         new_path = os.path.join(root, new_name)

#         # Avoid overwriting if the name already matches
#         if old_path != new_path:
#             try:
#                 os.rename(old_path, new_path)
#                 print(f"Renamed: {old_path} → {new_path}")
#             except Exception as e:
#                 print(f"Error renaming {old_path}: {e}")


import os
from PIL import Image

PHOTO_DIR = 'photo'
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp')
TARGET_QUALITY = 85
MAX_WIDTH = 1920
MAX_HEIGHT = 1080

def compress_image(image_path):
    try:
        ext = os.path.splitext(image_path)[1].lower()
        with Image.open(image_path) as img:
            img = img.convert('RGB')
            img.thumbnail((MAX_WIDTH, MAX_HEIGHT))  # Resize while keeping aspect ratio

            # Temp save path to overwrite safely
            temp_path = image_path + ".tmp"

            if ext in ['.jpg', '.jpeg']:
                img.save(temp_path, format='JPEG', quality=TARGET_QUALITY, optimize=True)
            elif ext == '.png':
                img.save(temp_path, format='PNG', optimize=True)
            elif ext == '.webp':
                img.save(temp_path, format='WEBP', quality=TARGET_QUALITY, method=6)
            else:
                print(f"Skipped (unsupported format): {image_path}")
                return

            os.replace(temp_path, image_path)
            print(f"Compressed: {image_path}")

    except Exception as e:
        print(f"Error compressing {image_path}: {e}")

for root, dirs, files in os.walk(PHOTO_DIR):
    for filename in files:
        if filename.lower().endswith(VALID_EXTENSIONS):
            compress_image(os.path.join(root, filename))
