
<p>
This is a demo python library wrapper for the github rest api 
https://docs.github.com/en/rest/
</p>


## <div align="center">User Guide</div>

<summary>Install</summary>

Clone repo and install [requirements.txt](https://github.com/stephanielewkowitz/githubrest)

```bash
cd bdist
python3 pip install githubrest*.whl  # install
```

<summary>Examples</summary>

```bash

import githubrest

repo = githubrest.Repos(TOKEN, USER)
output = repo.list_repos()
output2 = repo.create_repo()

event = githubrest.Events(TOKEN, USER)
output3 = event.list_events()
output4 = event.list_repo_events(repo_name)

branch = githubrest.Branches(TOKEN, USER)
output5 = branch.get_branches(repo_name)
output6 = branch.rename_branch(repo_name, branch_name, new_branch_name)

```
