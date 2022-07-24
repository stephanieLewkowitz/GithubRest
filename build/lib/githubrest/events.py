import requests
from .authentication import Auth

# Events Class
class Events(Auth):
    def __init__(self, token, user):
       super().__init__(token,user)
  
# List user events       
    def list_events(self):
        try:
        
    	    response = requests.get(f'https://api.github.com/users/{self.user}/events')
    	
    	    return response, response.text
    	
        except Exception as e:
    	    print(f"Error listing events, {e}")
    	    
#List reposiory events    	    
    def list_repo_events(self, repo):
        try:
        
    	    response = requests.get(f'https://api.github.com/repos/{self.user}/{repo}/events', 
                        headers={'Accept': 'application/vnd.github+json',
                            'Authorization': f'token {self.token}'})
                                                              
    	
    	    return response, response.text
    	
        except Exception as e:
    	    print(f"Error listing repos, {e}")

# curl -I https://api.github.com/users/tater/events
