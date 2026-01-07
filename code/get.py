import requests
import os
import json
from jinja2 import Environment, FileSystemLoader




from getGithub import   getUserData
from getStrapi import   pushStrapiData
import podcast


from minio import Minio

API_URL = os.environ.get('API_ENDPOINT')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')



client = Minio("minio.server.robots.beer",
    access_key=AWS_ACCESS_KEY_ID,
    secret_key=AWS_SECRET_ACCESS_KEY,
)


## First 100
api_url = 'https://lifeandshell.apps.elino.se/wp-json/wp/v2/posts?_embed&per_page=100'
posts_json = []
response = requests.get(api_url)
print(response.status_code)

if response.status_code == 200:
    posts_json = response.json()



#print(posts_json)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

  
for post in posts_json:
    print("#######################")
    #print(post["_embedded"]["wp:term"])
    # Get catergory
    category=[]
    for cat in post["_embedded"]["wp:term"][0]:
        #catJson = json.dumps(cat)
        print(cat['name'])
        print("##")
        category.append(str(cat['name']))
    #print(category)
    post['category'] = category


    dest = "/code/public/blog/"+post['slug']
    if not os.path.exists(dest):
        os.makedirs(dest)
    template = env.get_template('blog.tpl')
    output = template.render(post=post)
    fileName = dest+ "/index.html"
    f = open(fileName, "w")
    f.write(output)
    f.close()


    dest = "/code/hugo/content/posts/"+post['slug']
    template = env.get_template('hugo/post.tpl')
    output = template.render(post=post)
    fileName = dest+ ".html"
    f = open(fileName, "w")
    f.write(output)
    f.close()

    #Push to strapi
    pushStrapiData(post)

### 100-200
api_url = 'https://lifeandshell.apps.elino.se/wp-json/wp/v2/posts?_embed&per_page=100&offset=100'
posts_json = []
response = requests.get(api_url)
posts_json = response.json()
#print(posts_json)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

  
for post in posts_json:
    print("#######################")
    #print(post["_embedded"]["wp:term"])
    # Get catergory
    category=[]
    for cat in post["_embedded"]["wp:term"][0]:
        #catJson = json.dumps(cat)
        print(cat['name'])
        print("##")
        category.append(str(cat['name']))
    #print(category)
    post['category'] = category


    dest = "/code/public/blog/"+post['slug']
    if not os.path.exists(dest):
        os.makedirs(dest)
    template = env.get_template('blog.tpl')
    output = template.render(post=post)
    fileName = dest+ "/index.html"
    f = open(fileName, "w")
    f.write(output)
    f.close()


    dest = "/code/hugo/content/posts/"+post['slug']
    template = env.get_template('hugo/post.tpl')
    output = template.render(post=post)
    fileName = dest+ ".html"
    f = open(fileName, "w")
    f.write(output)
    f.close()
    #Push to strapi
    pushStrapiData(post)

#
##Get Github data
githubData = getUserData()
print(githubData)



f = open("/code/hugo/data/github.json", "w")
f.write(json.dumps(githubData))
f.close()
