# import json
# import re

# def fix_json_error(data: str, return_str=True):
#     data = data.strip().strip('"').strip(",").strip("`")

#     try:
#         json.loads(data)
#         return data
#     except json.decoder.JSONDecodeError:
#         data = data.split("\n")
#         data = [line.strip() for line in data]

#         if not data[-1][-1] == '"':
#             data[-1] += '"'

#         # Add checks for balanced curly braces
#         open_braces = 0
#         close_braces = 0
#         for line in data:
#             open_braces += line.count('{')
#             close_braces += line.count('}')
        
#         if open_braces > close_braces:
#             data.append('}' * (open_braces - close_braces))
#         elif close_braces > open_braces:
#             data.insert(0, '{' * (close_braces - open_braces))

#         # Add checks for trailing characters
#         for i in range(len(data)):
#             line = data[i]
#             if line in ['[', ']', '{', '}']:
#                 continue
#             if line.endswith(('[', ']', '{', '}')):
#                 continue

#             if i + 1 < len(data): #edge case added
#                 if not line.endswith(',') and data[i + 1] not in [']', '}', '],', '},']:
#                     data[i] += ','
#                 if data[i + 1] in [']', '}', '],', '},'] and line.endswith(','):
#                     data[i] = line[:-1]

#         data = " ".join(data)

#         if not return_str:
#             data = json.loads(data)
#         return data

# data = """
# { 
#     "url": "https://api.spotify.com/v1/artists/2FKWNmZWDBZR4dE5KX4plR/albums", 
#     "description": "Get the list of albums by Diljit Dosanjh.", 
#     "output_instructions": "What is the title and release date of his newest album?" 
# }
# """

# api_url = "https://api"
# # data = fix_json_error(data)
# # print(data)
# #data = json.loads(data)
# data = json.loads(data)['url'].replace(api_url, '')
# print(data)


# import requests

# def test_spotify_api(access_token):
#     url = 'https://api.spotify.com/v1/me'
#     headers = {
#         'Authorization': f'Bearer {access_token}'
#     }

#     try:
#         response = requests.get(url, headers=headers)

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             print("GET request to Spotify API successful.")
#             print("Response:")
#             print(response.json())  # Print the JSON response
#         else:
#             print(f"Error: Status code {response.status_code}")
#             print("Response:")
#             print(response.text)  # Print the error response
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")

# if __name__ == '__main__':
#     # Replace 'YOUR_ACCESS_TOKEN_HERE' with your actual Spotify API access token
#     access_token = 'BQC6T0jqUHoKnJ5ZT9zkrOgR0L401YWY5zczWsNOCSasuR9PEv9zZyNk1aL8Aj5B5rnOzm-Bejq4jOhYmwR4ycPYEY1WTQrCcj8jOpzlCpXDpKHb4_Um-BjVQFtHhVE0rOHaWjNTNe9erptpzWF82kp_SzVN01Cqk8VLPnKasp1aAMUQF2CesW3Q2C2BnDG_S0L2942ndhRmznoB_UPN1a9BSq5xitisQjp_Mxb3b95vZef6qc4A16SUmTZ79rHAQZVbzItA9thr2jnVZDwIr3YPAP7UsijpqMuIQM3Pga0MZJatEB-Fusw2cIWLiT1U-IDJbiI_1bMm4gTGewG1LONK'
#     test_spotify_api(access_token)

from typing import Dict, Any

#from requests_wrapper import TextRequestsWrapper  # Import your wrapper class here
from langchain.requests import RequestsWrapper
import requests
from langchain_community.utilities import Requests


class SpotifyAPI:
    def __init__(self, requests_wrapper: RequestsWrapper):
        self.requests_wrapper = requests_wrapper

    def get_user_profile(self):
        url = 'https://api.notion.com/v1/users'
        headers={}
        spotify_access_token = "BQDqJX9iUcTkOCQfs2a32rvFCeBka4AyUjg3SSfLChMJ7MuvzF5ZPDARQPZvl0Dd0sL8-2vSiRY-_V6Q4YsXwFQBM2oBnLxVjdwOLOHuMNOazR3lJAomesW7nkBZAh4DcaO-im0kHoRPfmHned408ECLPM8Er6n9anko3UDos_uLjYqGQW9TOUOucEMWfzE7SyOQa4IwgyZKWajMnxWvH0321DWpWN8xpDq4Qc3C1CX3LRuOzbIpsul-IOIpjB-fZcvyRX2eL3BeQ1pfAdLWurhbtxJxBny2jsThno-jWwaSx0Mkr5LRh86V0ifKPHIG7vOgtVtLsl6XIMkI-uQdl2eh"
        Notion_token = "secret_vu6u516RRHpU5BABNV49Y3JTZHagwmzAtrMVmtDhcjd"
        headers['Authorization'] = f'Bearer {Notion_token}'
        headers['Notion-Version'] = "2022-06-28"
        headers['Content-Type'] = "application/json"
        requests_wrapper = Requests(headers=headers)

        response = requests_wrapper.get(url)

        
        return response.json()
    

    # def get_spotify_auth_headers(self) -> Dict[str, str]:
    #     spotify_access_token = "BQDqJX9iUcTkOCQfs2a32rvFCeBka4AyUjg3SSfLChMJ7MuvzF5ZPDARQPZvl0Dd0sL8-2vSiRY-_V6Q4YsXwFQBM2oBnLxVjdwOLOHuMNOazR3lJAomesW7nkBZAh4DcaO-im0kHoRPfmHned408ECLPM8Er6n9anko3UDos_uLjYqGQW9TOUOucEMWfzE7SyOQa4IwgyZKWajMnxWvH0321DWpWN8xpDq4Qc3C1CX3LRuOzbIpsul-IOIpjB-fZcvyRX2eL3BeQ1pfAdLWurhbtxJxBny2jsThno-jWwaSx0Mkr5LRh86V0ifKPHIG7vOgtVtLsl6XIMkI-uQdl2eh"
    #     return {'Authorization': f'Bearer {spotify_access_token}'}

if __name__ == "__main__":
    requests_wrapper = RequestsWrapper()  # Initialize your requests wrapper
    spotify_api = SpotifyAPI(requests_wrapper)

    # Example: Get user profile details
    user_profile = spotify_api.get_user_profile()
    print("User Profile:")
    import json
    print(user_profile)
    print(type(user_profile))
