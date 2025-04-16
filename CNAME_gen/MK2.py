# Project: CNAME-Generator
# File Updated: 16-04-2025
# Credits: Adam Drmota

import secrets
import os


class AlreadyInDB(Exception):
    """
    Exception raised when attempting to add an entry that already exists in the database.

    This exception is used to signal that a duplicate entry was detected, and the operation
    cannot proceed as it would violate the uniqueness constraint of the database.

    Attributes:
        None
    """

    pass


def generator(digit=6) -> None:
    """
    Generates a unique CNAME string consisting of alternating vowels and consonants.
    The function creates a string by randomly selecting three vowels and three consonants
    from predefined lists. Each selected character is removed from its respective list
    to ensure uniqueness within the generated string. The resulting string is then checked
    for collisions in the database. If a collision is detected, the function recursively
    calls itself to generate a new string.
    Args:
        digit (int, optional): Placeholder argument. Defaults to 6. (Currently unused in the function.)
    Raises:
        AlreadyInDB: If the generated CNAME already exists in the database.
    Notes:
        - The function assumes the existence of `check_for_collision` and `save_secret` functions.
        - The `check_for_collision` function checks if the generated CNAME exists in the database.
        - The `save_secret` function saves the generated CNAME to the database.
    """
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

    for _ in range(digit // 2):
        sam_ch = secrets.choice(sam)
        sou_ch = secrets.choice(sou)
        sam.remove(sam_ch)
        sou.remove(sou_ch)
        cname += sam_ch + sou_ch

    try:
        check_for_collision(cname)
        save_secret(cname)

    except AlreadyInDB:
        generator()


def check_for_collision(cname) -> None:
    """
    Checks if the given cname already exists in the database.

    This function is intended to connect to a database and verify if the
    provided cname is a duplicate. If a duplicate is found, an exception
    (e.g., AlreadyInDB) should be raised. Currently, the implementation
    is a placeholder.

    Args:
        cname (str): The cname to check for duplicates in the database.

    Raises:
        AlreadyInDB: If the cname is found in the database (to be implemented).
    """
    # TODO connect to db and check for dublicates
    # try:
    # if cname in db:
    #     raise AlreadyInDB
    pass


# TODO change saving location
def save_secret(cname) -> None:
    """
    Saves the provided CNAME string to a file named 'CNAME.txt'.

    Args:
        cname (str): The CNAME string to be saved.

    Raises:
        Exception: If an error occurs while writing to the file, it will be caught and printed.

    Note:
        The function currently does not call the `send()` function, as it is commented out.
    """
    try:
        with open("CNAME.txt", "w") as f:
            f.write(cname)
    except Exception as e:
        print(f"Error saving cname: {e}")
    # finally:
    #     send()


def send():
    """
    Placeholder function for sending data to a proxy server and updating configurations.
    This function is intended to:
    1. Connect to a proxy server or send an API request containing the following information:
       - CNAME (Canonical Name)
       - WireGuard IP (WG-IP)
       - WireGuard public key (wg_pubkey)
       - Ping the WireGuard Gateway (WG GW)
    2. Update the proxy server's NGINX and WireGuard configurations using an automatic script.
    3. Send the CNAME to a database, potentially in the same step as the above operations.
    Note:
    - The implementation details for connecting to the proxy server, sending the API request,
      and updating configurations are yet to be completed.
    - Ensure proper error handling and logging when implementing this function.
    """
    # TODO connect to proxy somehow or sand some API request somewhere with cname, WG-IP and wg_pubkey + ping WG GW.
    # TODO Proxyserverer already has a automatic script for updating NGINX and WG config

    # TODO send cname to DB (can be done in the same step as above)

    pass


if __name__ == "__main__":
    # TODO change path to the location of CNAME.txt
    # if not os.path.exists("CNAME.txt"):
    #    generator()
    generator()
