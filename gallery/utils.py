# gallery/utils.py
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def compress_image(image, quality=85, max_width=1200):
    """Compress uploaded images to optimize loading times"""
    img = Image.open(image)
    
    # Resize if too large
    if img.width > max_width:
        ratio = max_width / float(img.width)
        height = int(float(img.height) * ratio)
        img = img.resize((max_width, height), Image.Resampling.LANCZOS)
    
    # Convert to RGB if necessary
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Compress
    output = BytesIO()
    img.save(output, format='JPEG', quality=quality, optimize=True)
    output.seek(0)
    
    return InMemoryUploadedFile(
        output, 'ImageField', f"{image.name.split('.')[0]}.jpg",
        'image/jpeg', output.getbuffer().nbytes, None
    )