from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os

def test_scores_service(url):
    # Set Firefox options
    options = Options()
    options.headless = True  # Run Firefox in headless mode (without opening a visible browser window)

    # Set the path to the geckodriver executable
    geckodriver_path = '/usr/bin/geckodriver'

    # Create a Firefox WebDriver instance
    driver = webdriver.Firefox(options=options, executable_path=geckodriver_path)

    # Navigate to the provided URL
    driver.get(url)

    try:
        # Find the score element on the web page
        score_element = driver.find_element(By.ID, "score")

        # Get the text of the score element
        score_text = score_element.text

        # Convert the score to an integer
        score = int(score_text)

        # Check if the score is between 1 and 1000
        if 1 <= score <= 1000:
            return True
        else:
            return False

    except Exception as e:
        print("Error occurred during testing:", str(e))
        return False

    finally:
        # Quit the browser
        driver.quit()

def main_function():
    # Call the test_scores_service function with the application URL
    url = "http://127.0.0.1:5000"
    result = test_scores_service(url)

    if result:
        print("Tests passed!")
        return 0
    else:
        print("Tests failed!")
        return -1

if __name__ == "__main__":
    exit_code = main_function()
    exit(exit_code)

