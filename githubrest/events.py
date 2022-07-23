import subprocess
from .authentication import Auth

# Events Class
class Events(Auth):
    def __init__(self, token, user):
       super().__init__(token,user)
  
# List user events       
    def list_events(self):
        try:
    	    out = subprocess.check_output([
    	    "curl", 
    	    "-I",
    	    f"https://api.github.com/users/{self.user}/events"])
    	
    	    return out
    	
        except Exception as e:
    	    print(f"Error listing events, {e}")
    	    
#List reposiory events    	    
    def list_repo_events(self, repo):
        try:
    	    out = subprocess.check_output([
    	    "curl", 
    	    "-H",
    	    "Accept: application/vnd.github+json", 
    	    "-H", 
    	    f"Authorization: token {self.token}", 
    	    f"https://api.github.com/repos/{self.user}/{repo}/events"])
    	
    	    return out
    	
        except Exception as e:
    	    print(f"Error listing repos, {e}")

# curl -I https://api.github.com/users/tater/events
