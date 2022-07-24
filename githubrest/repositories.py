import requests
from .authentication import Auth

# This class allows interaction with user repositories
class Repos(Auth):
    def __init__(self, token, user):
       super().__init__(token,user)
        
    # List user repositories
    def list_repos(self):
        try:
    	    response = requests.get(f'https://api.github.com/users/{self.user}/repos', 
                        headers={'Accept': 'application/vnd.github+json',
                            'Authorization': f'token {self.token}'})
    	
    	    return response, response.text
    	
        except Exception as e:
    	    print(f"Error listing repos, {e}")


    # create repository for authenticated user
    def create_repo(self, repo_name):
    
        try:         
            data = {"name":repo_name}
            strdat = str(data) 
            strdat = strdat.replace("\'","\"") 
        
            response = requests.post(f'https://api.github.com/{self.user}/repos', 
                        headers={'Accept': 'application/vnd.github+json',
                            'Authorization': f'token {self.token}'}, 
                         data = strdat)
            
            return response, response.text         
                         
        except Exception as e:
     	    print(f"Error creating repos, {e}")

#           commented attempt with subprocess.check_output()                         
#     	    out = subprocess.check_output([
#     	    "curl",
#     	    "-X", 
#     	    "POST", 
#     	    "-H",
#     	    "Accept: application/vnd.github+json", 
#     	    "-H", 
#     	    f"Authorization: token {self.token}", 
#     	    f"https://api.github.com/{self.user}/repos",
#     	    "-d",
#     	    strdat])
    	
#     	    return out






