# Project: CNAME-Generator
# File Updated: 16-04-2025
# Credits: Adam Drmota

import secrets
import string
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
    Generates a random alphanumeric string (CNAME) of a specified length and ensures it is unique in the database.
    The function creates a random string composed of digits and lowercase letters.
    If the generated string already exists in the database, the function recursively calls itself to generate a new string.
    Args:
        digit (int, optional): The length of the generated string. Defaults to 6.
    Raises:
        AlreadyInDB: If the generated string already exists in the database.
    Notes:
        - The function relies on `check_for_collision` to verify the uniqueness of the generated string.
        - The `save_secret` function is used to store the unique string in the database.
    """
    # TODO if secret in db, call generator() again and check again.

    cname = "".join(
        secrets.choice(string.digits + string.ascii_lowercase) for _ in range(digit)
    )
    try:
        check_for_collision(cname)
        save_secret(cname)

    except AlreadyInDB:
        generator()


def check_for_collision(cname) -> None:
    """
    Checks for potential collisions of the given cname in the database.

    This function is intended to verify if the provided cname already exists
    in the database. If a collision is detected, an appropriate exception
    (e.g., AlreadyInDB) should be raised. Currently, the database connection
    and collision detection logic are not implemented.

    Args:
        cname (str): The cname to check for collisions.

    Returns:
        None

    Raises:
        AlreadyInDB: If the cname is already present in the database (to be implemented).
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
        The function currently does not call the `send()` function, which is commented out in the code.
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
    Sends data to a proxy server or API endpoint to update configurations and database records.
    This function is intended to:
    - Connect to a proxy server or send an API request containing the CNAME, WireGuard IP,
      and WireGuard public key.
    - Ping the WireGuard gateway to verify connectivity.
    - Update the proxy server's NGINX and WireGuard configurations using an automatic script.
    - Send the CNAME to a database, potentially in the same step as the configuration update.
    Note:
    - Implementation details are currently pending.
    - Ensure proper error handling and security measures when implementing this function.
    """
    # TODO connect to proxy somehow or sand some API request somewhere with cname, WG-IP and wg_pubkey+ ping WG GW.
    # TODO Proxyserverer already has a automatic script for updating NGINX and WG config

    # TODO send cname to DB (can be done in the same step as above)

    pass


if __name__ == "__main__":
    # TODO change path to the location of CNAME.txt
    # if not os.path.exists("CNAME.txt"):
    #    generator()
    generator()
