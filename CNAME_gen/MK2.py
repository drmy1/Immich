import secrets
import os


class AlreadyInDB(Exception):
    pass


def generator(digit=6) -> None:
    # TODO if secret in db, call generator() again and check again.
    sam = ["a", "e", "i", "o", "u", "y"]
    sou = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "z",
    ]
    cname: str = ""

    for i in range(3):
        sam_ch = secrets.choice(sam)
        sou_ch = secrets.choice(sou)
        sam.remove(sam_ch)
        sou.remove(sou_ch)
        cname += sam_ch + sou_ch

    print(cname)

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
    # TODO connect to proxy somehow or sand some API request somewhere with cname, WG-IP and wg_pubkey.
    # TODO Proxyserverer already has a automatic script for updating NGINX and WG config

    # TODO send cname to DB (can be done in the same step as above)

    pass


if __name__ == "__main__":
    # TODO change path to the location of CNAME.txt
    if not os.path.exists("CNAME.txt"):
        generator()
    # generator()
