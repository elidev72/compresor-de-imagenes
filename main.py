import os
from PIL import Image
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    
    downloadFolder: str = os.getenv('DOWNLOAD_FOLDER')
    
    print(downloadFolder)