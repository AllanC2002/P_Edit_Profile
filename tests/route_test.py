import requests

#BASE_URL = "http://44.214.216.202:8080"
BASE_URL = "http://44.194.87.132:8080"#prod
login_data = {
    "User_mail": "allanprod2",  
    "password": "1234"                
}

#login_response = requests.post(f"http://52.203.72.116:8080/login", json=login_data)
login_response = requests.post(f"http://100.25.74.174:8080/login", json=login_data)#prod

if login_response.status_code != 200:
    print("Error:", login_response.status_code, login_response.json())
    exit()

token = login_response.json().get("token")
print("Token :", token)

# endpoint edit
update_data = {
    "Description": "Changed description by prod in te video",
    #"Id_preferences": 2,
    #"Id_type": 1
}

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

update_response = requests.patch(f"{BASE_URL}/update-profile", json=update_data, headers=headers)

print("Response:", update_response.status_code)
print("Response JSON:", update_response.json())
