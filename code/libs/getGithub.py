from github import Github


# Last time
import datetime
import pytz

utc=pytz.UTC
today = datetime.datetime.now(utc)
backmonth = today - datetime.timedelta(days=180)
print(backmonth)

def getUserData():
    # Authentication is defined via github.Auth
    from github import Auth

    # using an access token
    auth = Auth.Token("")

    # First create a Github instance:

    # Public Web Github
    g = Github(auth=auth)

    # Github Enterprise with custom hostname
    g = Github( auth=auth)
    githubData = {}
    githubRepos=[]
    githubTopics=[]
    #print(g.get_user().get_events())
    #for repo in g.get_user().get_events():
    #    print(repo)
    ##
    # Then play with your Github objects:
    numberOfRepos=0
    numberOfStars=0

    for repo in g.get_user().get_repos():
        if repo.pushed_at > backmonth:
            topics = repo.get_topics()
            repoData ={
                "name": repo.full_name,
                "date": repo.pushed_at,
                "url": repo.url,
                "description": repo.description,
                "topics": topics
            }
    
            githubTopics.append(topics)
            githubRepos.append(repoData)
        print(repo.subscribers_count)
    
        #repo = g.get_repo(repo.full_name)
        
    
        numberOfRepos= numberOfRepos + 1
        numberOfStars= numberOfStars + int(repo.stargazers_count)


    orgs = g.get_user().get_orgs()
    for org in orgs:
        print(org)


    # To close connections after use
    githubData['reposcount']=numberOfRepos
    githubData['repos']=githubRepos
    githubData['topics']=githubTopics
    g.close()


    #result
    return githubData