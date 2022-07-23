import subprocess
from .authentication import Auth

# This class allows interaction with user repositories
class Repos(Auth):
    def __init__(self, token, user):
       super().__init__(token,user)
        
    # List user repositories
    def list_repos(self):
        try:
    	    out = subprocess.check_output([
    	    "curl", 
    	    "-H",
    	    "Accept: application/vnd.github+json", 
    	    "-H", 
    	    f"Authorization: token {self.token}", 
    	    f"https://api.github.com/users/{self.user}/repos"])
    	
    	    return out
    	
        except Exception as e:
    	    print(f"Error listing repos, {e}")


    # create repository
    def create_repo(self, repo_name):
    
        data = {"name":repo_name}
        strdat = str(data) 
        strdat = strdat.replace("\'","\"") 
        try: 
    	    out = subprocess.check_output([
    	    "curl",
    	    "-X", 
    	    "POST", 
    	    "-H",
    	    "Accept: application/vnd.github+json", 
    	    "-H", 
    	    f"Authorization: token {self.token}", 
    	    f"https://api.github.com/{self.user}/repos",
    	    "-d",
    	    strdat])
    	
    	    return out

        except Exception as e:
    	    print(f"Error creating repos, {e}")





