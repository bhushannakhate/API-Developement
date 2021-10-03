import requests

def get_token():
    url = "http://127.0.0.1:8000/api-token-auth/"
    response = requests.post(url, data={'username': 'superuser', 'password': 'superuser'})
    # print(response.json())
    return response.json()['token']

def get_data():
    url = "http://127.0.0.1:8000/api/users_list/"
    #token = get_token()
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.get(url, headers=header)
    print(response.json())
    
#get_data()

def delete_data():
    url = "http://127.0.0.1:8000/api/users_list/1"
    header = {'Authorization': f'Token {get_token()}'}
    requests.delete(url, headers=header)


delete_data()
