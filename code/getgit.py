import requests
import os
import json
from jinja2 import Environment, FileSystemLoader




from getGithub import   getUserData

from minio import Minio

API_URL = os.environ.get('API_ENDPOINT')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')




#
#
#
#
#
##Making Blog Post page 
#template = env.get_template('blog_page.tpl')
#output = template.render(posts=posts_json)
#fileName = "/code/public/blog/index.html"
#f = open(fileName, "w")
#f.write(output)
#f.close()
#
#
#api_url = 'https://lifeandshell.apps.elino.se/wp-json/wp/v2/posts?_embed&per_page=10'
#posts_json = []
#response = requests.get(api_url)
#posts_json = response.json()
#
#
#api_url = 'https://lifeandshell.apps.elino.se/wp-json/wp/v2/tags?_embed&per_page=100'
#response = requests.get(api_url)
#tags_json = response.json()
#
#
#api_url = 'https://lifeandshell.apps.elino.se/wp-json/wp/v2/categories?_embed&per_page=100'
#response = requests.get(api_url)
#categoris_json = response.json()
#
#
#
##Get Github data
githubData = getUserData()
print(githubData)


tags = []
for topics in githubData['topics']:
    for topic in topics:
        tags.append(topic)




print("tags"+str(tags))



##Making index page 
#template = env.get_template('index.tpl')
#output = template.render(posts=posts_json, githubData=githubData, tags=tags)
#fileName = "/code/public/index.html"
#f = open(fileName, "w")
#f.write(output)
#f.close()
#
#for path, subdirs, files in os.walk("/code/public"):
#    path = path.replace("\\","/")
#    directory_name = path.replace("/code/public","")
#    for file in files:
#        print(os.path.join(path, file))
#        client.fput_object(os.environ.get('AWS_BUCKET'), directory_name+'/'+file, os.path.join(path, file),)


