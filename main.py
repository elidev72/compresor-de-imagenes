import os
from PIL import Image as i
import pikepdf
from dotenv import load_dotenv

QUALITY: int = 60

if __name__ == '__main__':
    load_dotenv()
    originFolder: str | None = os.getenv('ORIGIN_FOLDER')
    imageFolder: str | None = os.getenv('IMAGE_FOLDER')
    pdfFolder: str | None = os.getenv('PDF_FOLDER')
    
    for filename in os.listdir(originFolder):
        name, extension = os.path.splitext(originFolder + filename)
        
        if extension in ('.jpg', '.png', '.jpeg'):
            image = i.open(originFolder + filename)
            image.save(imageFolder + "compressed_"+filename, optimize=True, quality=QUALITY)
            os.remove(originFolder + filename)
        elif extension == '.pdf':
            with pikepdf.open(originFolder + filename) as pdf:
                pdf.save(pdfFolder + "compressed_"+filename, compress_streams=True)
                os.remove(originFolder + filename)