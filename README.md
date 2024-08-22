# Twitter/X Automation with Selenium

This project is an automation script that interacts with Twitter/X using the Selenium WebDriver. It logs into your Twitter account, searches for a specific hashtag, retrieves the tweets, optionally likes them, and saves the tweets to a text file.

## Features

- **Login Automation**: Logs into Twitter/X using provided credentials.
- **Hashtag Search**: Searches for tweets with a specified hashtag.
- **Tweet Retrieval**: Scrolls through the results to gather a list of tweets.
- **Like Tweets**: Automatically likes the retrieved tweets.
- **Save Tweets**: Saves the retrieved tweets to a `.txt` file.

## Prerequisites

- **Python 3.x**: Make sure you have Python installed.
- **Selenium**: You can install it via pip:
  ```zsh
   pip install selenium
- **ChromeDriver**: : Ensure you have the ChromeDriver that matches your Chrome browser version.
-  A valid Twitter account with login credentials.

## Setup

1. **Clone the Repository**:

      ```zsh
   git clone https://github.com/zeysnepk/X-SELENIUM.git
   cd twitter-selenium-automation

2. **Run login.py**:

	First run loginInfo.py file to store your Twitter/X login credential.

      ```zsh
   python loginInfo.py
   
## Usage

1. Run the Scrip:

      ```zsh
   python x_automation.py

2. Script Execution:

   - The script will open a Chrome browser, navigate to Twitter/X, and log in with the provided credentials.
   - It will search for the specified hashtag (in the script, this is **'#ezoterikbilgi'** by default).
   - The script will scroll through the results, collect the tweets, and optionally like them.
   - Finally, it will save the collected tweets to a **'tweets.txt'** file.
  
## Customization

You can customize the script further by modifying the following:

- **Change Hashtag**: Modify the **'SEARCH_KEY'** variable in **'twitter_automation.py'** to search for a different hashtag.
- **Change XPATH or CSS selectors**: The XPATH or CSS selectors used to find the various elements on the Twitter website.
- **Customize Delay**: You can change the delay time in time.sleep() function.
- The behavior of the script, such as the number of tweets to like or the way the tweet text is saved to the file.

## Notes

- **Rate Limiting**: Be aware that Twitter/X might limit your actions if you interact with the platform too rapidly.
- **Error Handling**: The script includes basic error handling for element interaction issues, but further enhancements can be made based on your needs.

## Contribution

Feel free to fork this repository and submit pull requests. Any improvements or new features are welcome!
  
   
