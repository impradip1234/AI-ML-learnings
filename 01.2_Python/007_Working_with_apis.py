import requests

def api_request():
    url='https://api.freeapi.app/api/v1/public/randomusers/user/random'
    result=requests.get(url)
    data=result.json()
    if data['success'] and 'data' in data:
        user_data=data['data']
        user_name=user_data['login']['username']
        user_country=user_data['location']['country']
        return user_name,user_country
    else:
        raise Exception("Failed to fetch user data!")

def main():
    try:
        user_name,user_country = api_request()
        print(f"user name is: {user_name} \ncountry name is:{user_country}")
    except Exception as e:
        print(str(e))
    

if __name__=="__main__":
    main()

