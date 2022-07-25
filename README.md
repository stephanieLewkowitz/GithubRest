
<p>
This is a demo python library wrapper for the github rest api 
https://docs.github.com/en/rest/
</p>


## <div align="center">User Guide</div>

<summary>Install</summary>

<p>
Clone repo and install [requirements.txt](https://github.com/stephanielewkowitz/githubrest)
</p>

```bash
python3 setup.py bdist_wheel
cd dist
python3 -m pip install githubrest-0.0.1-py3-none-any.whl.whl  # install
```
<p>
If the install directory is on the python path, the library should now be installed.
</p>
<p>
We are using the python "requests" library to make rest calls to the github api. We also need to provide a github user account and personal access token.

</p>
<summary>Examples</summary>

```bash

import githubrest

repo = githubrest.Repos(TOKEN, USER)

status, response = repo.list_repos()
status, response  = repo.create_repo(repo_name)

event = githubrest.Events(TOKEN, USER)
status, response  = event.list_events()
status, response  = event.list_repo_events(repo_name)

branch = githubrest.Branches(TOKEN, USER)
status, response  = branch.get_branches(repo_name)
status, response  = branch.rename_branch(repo_name, branch_name, new_branch_name)

```
<p>
a 200 or 201 status indicates a successful response from the server. A 400 status indicates an error. 
</p>

<p>
The input patch_data for Repos.patch_repo(repo_name, patch_data) should be in this dictionary format:
</p>
```
patch_data = {
"name":"Hello-World",
"description":"This is your first repository",
"homepage":"https://github.com",
"private":True,
"has_issues":True,
"has_projects":True,
"has_wiki":True}

```



