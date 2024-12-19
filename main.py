import os
from PIL import Image
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    
    originFolder: str | None = os.getenv('ORIGIN_FOLDER')
    
    print(originFolder)