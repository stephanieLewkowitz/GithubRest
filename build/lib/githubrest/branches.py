import subprocess
from .authentication import Auth

# create Branch class
class Branches(Auth):
    def __init__(self, token, user):
       super().__init__(token,user)
       
# get branches for a given user repository
    def get_branches(self, repo):
        try:
    	    out = subprocess.check_output([
    	    "curl", 
    	    "-H",
    	    "Accept: application/vnd.github+json", 
    	    "-H", 
    	    f"Authorization: token {self.token}", 
    	    f"https://api.github.com/repos/{self.user}/{repo}/branches"])
    	
    	    return out
    	
        except Exception as e:
    	    print(f"Error getting branches, {e}")
    	    
# rename a repository branch    	    
    def rename_branch(self, repo, branch_name, new_branch_name):
    
        data = {"name":rename_branch}
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
    	    f"https://api.github.com/repos/{self.user}/{repo}/branches/{branch_name}/rename",
    	    "-d",
    	    strdat])
    	
    	    return out
    	
        except Exception as e:
    	    print(f"Error renaming branch, {e}")
