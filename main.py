import requests


VK_API_URL = 'https://api.vk.com/method/'
VERSION = '5.131'
ACCESS_TOKEN = 'ddfd588addfd588addfd588a88decf18bbdddfdddfd588ab5c9338b69c6f9e7ad06c166'


def get_user_info(user_id):
    method_url = f'{VK_API_URL}users.get'
    params = {
        'access_token': ACCESS_TOKEN,
        'v': VERSION,
        'user_ids': user_id,
        'fields': 'first_name,last_name,city,country,bdate,photo_200_orig',
    }
    
    response = requests.get(method_url, params=params)
    data = response.json()
    
    if 'response' in data and len(data['response']) > 0:
        return data['response'][0]
    else:
        raise ValueError('Невозможно получить информацию о пользователе')


def display_user_info(user_data):
    fields_to_display = ['id', 'first_name', 'last_name', 'city', 'country', 'bdate', 'photo_200_orig']
    for field in fields_to_display:
        value = user_data.get(field)
        if value is not None:
            print(f"{field}: {value}")


if __name__ == '__main__':
    USER_ID = input("Введите логин: ")
    try:
        user_info = get_user_info(USER_ID)
        display_user_info(user_info)
    except Exception as e:
        print(e)