from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import loginInfo
import time

SEARCH_KEY = "#ezoterikbilgi" # Replace with the search key
FILE_NAME = "tweets.txt" # Replace with the desired output file name

browser = webdriver.Chrome() # Open Chrome browser
browser.get("https://x.com/") 
time.sleep(4)

def go_back():
    browser.back() # Go back one page
    time.sleep(3)
    
def go_forward():
    browser.forward() # Go forward one page
    time.sleep(3)

def login(username, password):
    login = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/span/span") # Find login button and click it
    login.click()
    time.sleep(5)
    try:
        # Try logging in with saved credentials
        username_input = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input") 
        username_input.send_keys(username)
        time.sleep(3)

        next_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]")
        next_button.click()
        time.sleep(5)

        password_input = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_input.send_keys(password)
        time.sleep(3)

        confirm_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button")
        confirm_button.click()
        time.sleep(5)
    except:
        print(f"Please ensure you're logged in with a valid account. Check your credentials and try again.")
        exit()
        
def search():
    #Find search input and enter the search key
    search_input = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input")
    search_input.send_keys(SEARCH_KEY)
    search_input.send_keys(Keys.ENTER) 
    time.sleep(5)
    
def get_tweets():
    tweets = []
    # Scroll to the bottom of the page to load more tweets
    last_height = browser.execute_script("return document.body.scrollHeight") # Get current scroll height
    while True:
        new_tweets = browser.find_elements(By.CSS_SELECTOR, "article[data-testid='tweet']") 
        tweets.extend(new_tweets)
        
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Wait for page to load more tweets
        time.sleep(3)
        new_height = browser.execute_script("return document.body.scrollHeight") # Get new scroll height
        if new_height == last_height:
            break # If the height did not change, break the loop
        last_height = new_height
    return tweets

def like_tweets(tweets):
    for tweet in tweets:
        try:
            # Scroll tweet into view
            browser.execute_script("arguments[0].scrollIntoView();", tweet)
            time.sleep(1)

            # Find like button and click it if it exists
            like_button = tweet.find_element(By.CSS_SELECTOR, "button[data-testid='like']") 
            if like_button:
                like_button.click()
                time.sleep(1)
        except Exception as e:
            print(f"Error while liking tweet: {e}")
            pass

def print_tweets(tweets):
    for tweet in tweets:
        tweet_text = tweet.find_element(By.CSS_SELECTOR, "div[data-testid='tweetText']").text # Get tweet text
        print(tweet_text)
        print("---------------------------------------------------------------------------------------------------------------------")
        
def save_to_file(file_name, tweets):
    tweet_count = 1
    with open(file_name, "w", encoding="utf-8") as file:
        # Save tweets to the output file
        for tweet in tweets:
            tweet_text = tweet.find_element(By.CSS_SELECTOR, "div[data-testid='tweetText']").text
            file.write(f"{str(tweet_count)}. {tweet_text}\n")
            file.write("---------------------------------------------------------------------------------------------------------------------\n")
            tweet_count += 1

if __name__ == "__main__":
    username, password = loginInfo.read_info() # Read saved credentials from loginInfo.py
    print(f"Username: {username}, Password: {password}")
    login(username, password) 
    search()
    elements = get_tweets()
    like_tweets(elements)
    print_tweets(elements)
    save_to_file(FILE_NAME, elements)
    browser.close() # Close the browser after all operations are done