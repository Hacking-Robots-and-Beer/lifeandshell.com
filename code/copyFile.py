import requests
import os
import json
from jinja2 import Environment, FileSystemLoader




from getGithub import   getUserData

from minio import Minio

API_URL = os.environ.get('API_ENDPOINT')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')



client = Minio("minio.server.robots.beer",
    access_key=AWS_ACCESS_KEY_ID,
    secret_key=AWS_SECRET_ACCESS_KEY,
)
for path, subdirs, files in os.walk("/code/hugo/public"):
    path = path.replace("\\","/")
    directory_name = path.replace("/code/hugo/public","")
    for file in files:
        print(os.path.join(path, file))
        client.fput_object(os.environ.get('AWS_BUCKET'), directory_name+'/'+file, os.path.join(path, file),)
