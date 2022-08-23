# Librairie(s)
import re
import requests

# Module(s)
from configuration import APP_CONFIG


def dprint(str_to_print, priority_level=1, preprint="", hashtag_display=True) -> None:
    from configuration import APP_CONFIG
    if APP_CONFIG.DEBUG and APP_CONFIG.PRIORITY_DEBUG_LEVEL >= priority_level:
        str_ident = "".join("-" for _ in range(priority_level))
        if hashtag_display:
            print(f"{preprint}#{str_ident} {str_to_print}")
        else:
            print(f"{preprint}{str_to_print}")


def get_my_ip() -> str:
    ip = None
    while True:
        try:
            # ip = urllib.request.urlopen(APP_CONFIG.GET_IP_URL).read().decode('utf8')
            response = requests.get(APP_CONFIG.GET_IP_URL).json()["Answer"]
            ip = re.search("is(.+?)in", response).group(1)
            break
        except:
            print("ERROR -> get current ip failed")

    return ip


def update_ip(ip_to_update: str) -> None:
    while True:
        try:
            requests.get(
                f"http://ipv4.dynv6.com/api/update?ipv4={ip_to_update}&token={APP_CONFIG.TOKEN}&zone={APP_CONFIG.ZONE}")
            break
        except:
            print("ERROR -> update ip")
