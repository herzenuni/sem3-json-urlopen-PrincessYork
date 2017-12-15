import requests
from pprint import pprint


def get_vk_user(user_id, fields):

    req = "https://api.vk.com/method/users.get?user_ids={}&fields={}&v=5.69".format(user_id, fields)
    print('Generated request :', req)

    try:
        answer = requests.get(req)
    except requests.ConnectionError:
        print("Server connection error. Check your internet connection...")
    except Exception as exc:
        print(str(exc.__class__), " exception cached...")

    return answer.json()


if __name__ == "__main__":
    user_id = input("vk id : ")
    fields = input("fields : ")
    pprint(get_vk_user(user_id, fields))
