# Project: CNAME-Generator
# File Updated: 16-04-2025
# Credits: Adam Drmota

import secrets
import string
import os


class AlreadyInDB(Exception):
    pass


def generator(digit=6) -> None:
    # TODO if secret in db, call generator() again and check again.

    cname = "".join(
        secrets.choice(string.digits + string.ascii_lowercase)
        for _ in range(digit)
    )
    try:
        check_for_collision(cname)
        save_secret(cname)

    except AlreadyInDB:
        generator()


def check_for_collision(cname) -> None:
    # TODO connect to db and check for dublicates
    # try:
    # if cname in db:
    #     raise AlreadyInDB
    pass


# TODO change saving location
def save_secret(cname) -> None:
    try:
        with open("CNAME.txt", "w") as f:
            f.write(cname)
    except Exception as e:
        print(f"Error saving cname: {e}")
    # finally:
    #     send()


def send():
    # TODO connect to proxy somehow or sand some API request somewhere with cname, WG-IP and wg_pubkey+ ping WG GW.
    # TODO Proxyserverer already has a automatic script for updating NGINX and WG config

    # TODO send cname to DB (can be done in the same step as above)

    pass


if __name__ == "__main__":
    # TODO change path to the location of CNAME.txt
    # if not os.path.exists("CNAME.txt"):
    #    generator()
    generator()
