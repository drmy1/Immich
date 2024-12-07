import time
import sys
import ipaddress
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

EMAIL: str = "****"
PASSWORD: str = "****"
NAME: str = "****"


def registration(host, browser):
    """
    Registers a new user on the specified host using the provided browser instance.

    Args:
        host (str): The hostname or IP address of the server where the registration page is hosted.
        browser (selenium.webdriver): The Selenium WebDriver instance used to interact with the web page.

    Raises:
        Exception: If any error occurs during the registration process, it will be printed to the console.

    Note:
        This function assumes that the registration page is accessible at the path "/auth/register" on the specified host.
        It also assumes that the form fields have the IDs "email", "password", "confirmPassword", and "name".
        The function will wait for 5 seconds to allow the page to load before interacting with the form elements.

    Example:
        registration("localhost", browser)
    """
    try:
        browser.get(f"http://{host}:2283/auth/register")
        # waiting for the page to load
        time.sleep(5)
        # filling in the form
        email = browser.find_element(By.ID, "email")
        email.send_keys(f"{EMAIL}")
        password = browser.find_element(By.ID, "password")
        password.send_keys(f"{PASSWORD}")
        confpassword = browser.find_element(By.ID, "confirmPassword")
        confpassword.send_keys(f"{PASSWORD}")
        name = browser.find_element(By.ID, "name")
        name.send_keys(f"{NAME}")
        # Find the Submit button and click it
        continue_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        continue_button.click()
    except Exception as e:
        print(e)
    finally:
        print("Admin account created successfully")


def is_valid_ipv4(ip_object):
    """
    Checks if the given object is a valid IPv4 address.

    Parameters:
    - ip_object: The object to be checked for validity as an IPv4 address.

    Returns:
    - True if the object is a valid IPv4 address, False otherwise.

    Raises:
    - None.

    Examples:
    - is_valid_ipv4("192.168.0.1") returns True
    - is_valid_ipv4("256.0.0.1") returns False
    - is_valid_ipv4("192.168.0") returns False
    """
    try:
        ipaddress.IPv4Address(ip_object)
        return True
    except (ValueError, TypeError):
        return False


def main(host):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=chrome_options)
    registration(host, browser)
    browser.quit()

if __name__ == "__main__":
    if (len(sys.argv) - 1) == 1:
        host = sys.argv[1]
        if not is_valid_ipv4(host):
            raise ValueError("invalid IPv4 address")
    else:
        raise ValueError("wrong number of arguments")
    main(host)
