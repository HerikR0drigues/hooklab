from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Funcao para pegar os UpVotes
def getUpVotes():
    upvotes = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.reddit.com/r/programming/")

    posts = driver.find_elements(By.CSS_SELECTOR, 'shreddit-post')[:3]

    for post in posts:
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', post)
        upvote_number = shadow_root.find_element(By.CSS_SELECTOR, 'faceplate-number').get_attribute('textContent')
        upvotes.append(upvote_number)

    driver.quit()
    return upvotes
# ----------------------------------------------------------------- #


