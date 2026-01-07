import asyncio
import json
import os



url = os.environ.get('STRAPI_URL')
#url = 'http://192.168.1.70:1337/api'
token = os.environ.get('STRAPI_TOKEN')








import requests

# Login and get JWT

# Use JWT for authenticated requests
headers = {"Content-Type": "application/json","Authorization": f"Bearer {token}"}
#response = requests.get(f"{url}/articles", headers=headers)
#print(response.json())







def pushStrapiData(post):
    sendData = {
    "data": {
    "title": post['title']['rendered'],
    "slug": post['slug'],
    "category":str(post['category']),
    "articel": post['content']['rendered'],
    "tags": str(post['tags']),
    "date": post['date'],
    }}
    #print(sendData)
    urlToUse= url+"/Articles"
    data = json.dumps(sendData)
    resp = requests.post(
        urlToUse,
        headers=headers,
        data=data)
    print(resp.text)





#post_json = {'data': {'title': 'How to Automate LinkedIn Posts with Python 2025', 'slug': 'how-to-automate-linkedin-posts-with-python-the-2025-guide', 'category': "['Code', 'Life', 'Python']", 'articel': '\n<p></p>\n\n\n\n<p></p>\n\n\n\n<p>I have a simple workflow: I write my posts in WordPress, and once they&#8217;re ready, a workflow kicks off to get them published. A key part of this process is announcing the new post on LinkedIn to let my network know it&#8217;s live.</p>\n\n\n\n<p>Sounds easy, right? Well, I quickly discovered that most Python libraries for the LinkedIn API are outdated. LinkedIn has deprecated large parts of its old API, leaving many tools broken.</p>\n\n\n\n<p>After a bit of digging, I found a solid solution using just Python and the <code>requests</code> library. With this method, I can successfully post to my personal profile and into groups I manage. While I couldn&#8217;t get it to work for a company page, this covers most of my needs. Here&#8217;s how you can do it too.</p>\n\n\n\n<hr class="wp-block-separator has-alpha-channel-opacity"/>\n\n\n\n<h2 class="wp-block-heading">Step 1: Getting the Bloody Access Token</h2>\n\n\n\n<p>Before we can do anything, we need an <strong>access token</strong>. Be warned, this is the most painful part of the process.</p>\n\n\n\n<h3 class="wp-block-heading">Create a LinkedIn App</h3>\n\n\n\n<p>First, you need to head over to the <a target="_blank" rel="noreferrer noopener" href="https://www.linkedin.com/developers/">LinkedIn Developer Portal</a> and create an app. Fill out all the necessary details, give it a logo, and make sure you verify it if needed.</p>\n\n\n\n<p>Inside your app settings, you&#8217;ll find your <strong>Client ID</strong> and <strong>Client Secret</strong>. You&#8217;ll also need to add a <strong>Redirect URI</strong>. For this guide, we&#8217;ll use a dummy URL: <code>https://localhost:3000/callback</code>. Just make sure the URL you add here is the <em>exact same one</em> you use in the next step.</p>\n\n\n\n<h3 class="wp-block-heading">Authorize Your App</h3>\n\n\n\n<p>Now, you need to grant your newly created app permission to access your LinkedIn account. To do this, construct the following URL, replacing <code>YOUR_CLIENT_ID</code> with your app&#8217;s Client ID.</p>\n\n\n\n<pre class="wp-block-code"><code>https:&#47;&#47;www.linkedin.com/oauth/v2/authorization?response_type=code&amp;client_id=YOUR_CLIENT_ID&amp;redirect_uri=https://localhost:3000/callback&amp;state=foobar&amp;scope=openid,profile,w_member_social,w_organization_social\n</code></pre>\n\n\n\n<p>Paste this URL into your browser. You&#8217;ll be asked to log in to LinkedIn and authorize the app. After you approve it, you&#8217;ll be redirected to the dummy URL we set up. Since <code>localhost:3000</code> isn&#8217;t running anything, you&#8217;ll see an error page. <strong>This is expected!</strong></p>\n\n\n\n<p>Look at the URL in your browser&#8217;s address bar. It will look something like this:</p>\n\n\n\n<figure class="wp-block-embed"><div class="wp-block-embed__wrapper">\nhttps://localhost:3000/callback?code=Axxxxxxxxxxxxx&#8230;..&#038;state=foobar\n</div></figure>\n\n\n\n<p>See that long string of characters after <code>code=</code>? That&#8217;s your <strong>authorization code</strong>. Copy it!</p>\n\n\n\n<h3 class="wp-block-heading">Exchange the Code for an Access Token</h3>\n\n\n\n<p>Now we trade that code for our final access token. Open your terminal and use the following <code>cURL</code> command. Replace the placeholders with your <strong>Client ID</strong>, <strong>Client Secret</strong>, and the <strong>authorization code</strong> you just copied.</p>\n\n\n\n<p>Bash</p>\n\n\n\n<pre class="wp-block-code"><code>curl --location --request POST \'https://www.linkedin.com/oauth/v2/accessToken\' \\\n--header \'Content-Type: application/x-www-form-urlencoded\' \\\n--data-urlencode \'grant_type=authorization_code\' \\\n--data-urlencode \'code=PASTE_YOUR_AUTHORIZATION_CODE_HERE\' \\\n--data-urlencode \'client_id=PASTE_YOUR_CLIENT_ID_HERE\' \\\n--data-urlencode \'client_secret=PASTE_YOUR_CLIENT_SECRET_HERE\' \\\n--data-urlencode \'redirect_uri=https://localhost:3000/callback\'\n</code></pre>\n\n\n\n<p>When you run this, the response will be a JSON object containing your <code>access_token</code>. Save it securely—this is the key to making API calls. </p>\n\n\n\n<hr class="wp-block-separator has-alpha-channel-opacity"/>\n\n\n\n<h2 class="wp-block-heading">Step 2: Finding Your User and Group IDs</h2>\n\n\n\n<p>To post, you need to know <em>who</em> is posting and <em>where</em> they are posting. In the LinkedIn API, these are identified by URNs (Uniform Resource Names).</p>\n\n\n\n<h3 class="wp-block-heading">Get Your Personal URN</h3>\n\n\n\n<p>You can find your personal URN by making a simple API call. Run the following Python script, making sure to add your new access token.</p>\n\n\n\n<p>Python</p>\n\n\n\n<pre class="wp-block-code"><code>import requests\n\n# Paste the access token you received\nACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"\n\nheaders = {\n    "Authorization": f"Bearer {ACCESS_TOKEN}"\n}\n\napi_url = "https://api.linkedin.com/v2/userinfo"\n\ntry:\n    response = requests.get(api_url, headers=headers)\n    response.raise_for_status()\n    user_info = response.json()\n    print(f"Success! Your URN is: {user_info&#91;\'sub\']}")\nexcept requests.exceptions.RequestException as e:\n    print(f"An error occurred: {e}")\n</code></pre>\n\n\n\n<p>The output will contain your URN in the <code>sub</code> field. It will look like <code>urn:li:person:xxxxxxxx</code>.</p>\n\n\n\n<h3 class="wp-block-heading">Get a Group URN</h3>\n\n\n\n<p>To find a group&#8217;s ID, navigate to the group on LinkedIn and click to manage or edit it. The group ID is the number in the URL. Your Group URN will be <code>urn:li:group:GROUP_ID</code>.</p>\n\n\n\n<hr class="wp-block-separator has-alpha-channel-opacity"/>\n\n\n\n<h2 class="wp-block-heading">Step 3: Let&#8217;s Post to LinkedIn!</h2>\n\n\n\n<p>With the access token and URNs in hand, we can finally post. The script below sends a simple text post.</p>\n\n\n\n<ul class="wp-block-list">\n<li>Set the <code>ACCESS_TOKEN</code>.</li>\n\n\n\n<li>Set the <code>author</code> to your personal URN.</li>\n\n\n\n<li>To post to a <strong>group</strong>, set the <code>containerEntity</code> to the group&#8217;s URN. To post to your <strong>personal profile</strong>, comment out or remove the <code>"containerEntity"</code> line entirely.</li>\n\n\n\n<li>Change the <code>text</code> inside <code>shareCommentary</code> to whatever you want to post.</li>\n</ul>\n\n\n\n<p>Python</p>\n\n\n\n<pre class="wp-block-code"><code>import requests\nimport json\n\n# Your access token\nACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"\n# Your personal URN (from the previous step)\nYOUR_PERSON_URN = "urn:li:person:xxxxxxxx"\n# The URN of the group you want to post to\nGROUP_URN = "urn:li:group:1234567"\n\ndef post_to_linkedin(post_text):\n    """Posts a message to a LinkedIn group or personal profile."""\n\n    api_url = "https://api.linkedin.com/v2/ugcPosts"\n    \n    headers = {\n        "Authorization": f"Bearer {ACCESS_TOKEN}",\n        "Content-Type": "application/json",\n        "X-Restli-Protocol-Version": "2.0.0"\n    }\n\n    post_data = {\n        "author": YOUR_PERSON_URN,\n        "lifecycleState": "PUBLISHED",\n        # To post to a group, include the line below.\n        # To post to your personal feed, remove it.\n        "containerEntity": GROUP_URN,\n        "specificContent": {\n            "com.linkedin.ugc.ShareContent": {\n                "shareCommentary": {\n                    "text": post_text\n                },\n                "shareMediaCategory": "NONE"\n            }\n        },\n        "visibility": {\n            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"\n        }\n    }\n\n    try:\n        response = requests.post(api_url, headers=headers, data=json.dumps(post_data))\n        response.raise_for_status()  # Raise an exception for bad status codes\n        print("Post successful! ")\n        print(response.json())\n    except requests.exceptions.RequestException as e:\n        print(f"An error occurred: {e}")\n        if e.response:\n            print(f"Response status code: {e.response.status_code}")\n            print(f"Response content: {e.response.text}")\n\n# Example usage:\nmy_new_blog_post_announcement = "I just published a new blog post about automating LinkedIn with Python! Check it out. #python #automation #linkedinapi"\npost_to_linkedin(my_new_blog_post_announcement)\n\n</code></pre>\n\n\n\n<p>And that&#8217;s it! While the initial setup with OAuth 2.0 is a bit of a marathon, once you have the token, automating your posts from any Python script is straightforward. Happy automating! </p>\n', 'tags': '[66, 92, 4, 49]', 'date': '2025-09-16T09:59:24'}}
#urlToUse= url+"/Articles"
#data = json.dumps(post_json)
#resp = requests.post(
#    urlToUse,
#    headers=headers,
#    data=data)
#print(resp.text)



