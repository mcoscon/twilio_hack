# Cloudinary settings using python code. Run before pycloudinary is used.
import cloudinary
import uuid
from dotenv import load_dotenv
import cloudinary.uploader
import os
load_dotenv()
cloudinary.config(
  cloud_name = os.getenv("CLOUDINARY_NAME"),  
  api_key = os.getenv("CLOUDINARY_KEY"),  
  api_secret = os.getenv("CLOUDINARY_SECRET")  
)

def upload_cloudinary(image_name):
    #We'll need an identifier to upload different intruders
    image_id = uuid.uuid1().int
    image_id = str(image_id)
    cloudinary.uploader.upload(image_name, public_id = image_id) #upload the captured image "detected"
    return (cloudinary.utils.cloudinary_url(image_id)) #access the uploaded image url via its public_id
