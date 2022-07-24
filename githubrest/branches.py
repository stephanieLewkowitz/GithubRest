import requests
from .authentication import Auth

# create Branch class
class Branches(Auth):
    def __init__(self, token, user):
       super().__init__(token,user)
       
# get branches for a given user repository
    def get_branches(self, repo):
        try:

            response = requests.get(f'https://api.github.com/repos/{self.user}/{repo}/branches', 
                        headers={'Accept': 'application/vnd.github+json',
                            'Authorization': f'token {self.token}'})        
        
            return response, response.text
    	    
        except Exception as e:
    	    print(f"Error getting branches, {e}")
    	    
# rename a repository branch    	    
    def rename_branch(self, repo, branch_name, new_branch_name):
    

        try:
            data = {"new_name":new_branch_name}
            strdat = str(data) 
            strdat = strdat.replace("\'","\"") 
        
            response = requests.post(f'https://api.github.com/repos/{self.user}/{repo}/branches/{branch_name}/rename', 
                        headers={'Accept': 'application/vnd.github+json',
                            'Authorization': f'token {self.token}'}, 
                         data = strdat)
    	
            return response, response.text
    	
        except Exception as e:
    	    print(f"Error renaming branch, {e}")
