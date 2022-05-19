import streamlit as st
import logging
import boto3
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError
import requests
import mimetypes
import s3fs
import os
from PIL import Image 

def load_image(image_file):
	img = Image.open(image_file)
	return img


os.environ["AWS_DEFAULT_REGION"] = 'us-east-2'
os.environ["AWS_ACCESS_KEY_ID"] = 'AKIARLFEN3ZYTWBVYNX7'
os.environ["AWS_SECRET_ACCESS_KEY"] = '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'


s3 = boto3.client('s3')
s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='AKIARLFEN3ZYTWBVYNX7',
    aws_secret_access_key='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'
)

def save_uploadedfile(uploadedfile):
     with open(os.path.join(os.getcwd(),uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))



st.title('Abo5 Product Collection Portal')
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:

      # To See details
      file_details = {"filename":image_file.name, "filetype":image_file.type,
                      "filesize":image_file.size}
      st.write(file_details)
      st.write(image_file)

      # To View Uploaded Image
      st.image(load_image(image_file),width=250) 
      st.write(os.getcwd())
      save_uploadedfile(image_file)
      s3.Bucket('abo5').upload_file(Filename=image_file.name, Key='TEST')
 
       
