# Paulo Nuin Nov 2020

import os
import requests


query = """
{
  repository(owner: "spinnaker", name: "spinnaker") {
   forkCount
    issues{
      totalCount
    }
    pullRequests{
      totalCount
    }
    releases{
      totalCount
    }
    stargazers{
      totalCount
    }
    watchers{
      totalCount
    }    
  }
}
"""

token = os.getenv('GITHUB_TOKEN')
headers = {"Authorization": f'token {token}'}
print(headers)
request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
print(request.text)