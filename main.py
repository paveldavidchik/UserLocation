import requests


def location():
    info = requests.get('https://freegeoip.app/json/').json()
    for key, value in info.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    location()
