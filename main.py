# Librairie(s)
import time
from datetime import datetime

# Module(s)
from configuration import APP_CONFIG
from safe_actions import dprint, get_my_ip, update_ip

ip = get_my_ip()

dprint(f"Run {APP_CONFIG.APPLICATION_NAME}", priority_level=1)
dprint(f"Token: {APP_CONFIG.TOKEN}", priority_level=2)
dprint(f"Zone: {APP_CONFIG.ZONE}", priority_level=2)
dprint(f"Actual IP: {ip}", priority_level=2)
dprint(f"Update delay: {APP_CONFIG.REFRESH_DELAY}", priority_level=2)
dprint("\n", hashtag_display=False)

while True:
    try:
        new_ip = get_my_ip()

        dprint(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, Check IP update: New = {new_ip}, Old = {ip}",
               priority_level=2)
        if new_ip != ip:
            dprint(f"{new_ip} != {ip} => IP update request send ...", priority_level=3)
            update_ip()
            ip = new_ip
        else:
            dprint(f"{new_ip} == {ip} => no update.", priority_level=3)
    except:
        dprint(f"Script crash !", priority_level=2)
        print("#-- Error request crash")

    time.sleep(APP_CONFIG.REFRESH_DELAY)
