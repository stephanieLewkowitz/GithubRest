#Setup authentication class

class Auth:
    def __init__(self, token, user):
        self.token = token
        self.user = user
        if (type(self.token) != str) or (type(self.user) != str):
            raise Exception ('token and user inputs must be strings.')
       
        


