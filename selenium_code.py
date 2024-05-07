from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
from test2 import first_comment
import pickle

def check_for_new_video(channel_url):
    
    chrome_options = Options()
    # chrome_options.add_argument('headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('disable-gpu')
    chrome_options.add_argument('log-level=3')
    chrome_options.add_argument('--disable-crash-reporter')
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    
    prefs = {'profile.default_content_setting_values': {'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    chrome_options.add_experimental_option('prefs', prefs)
    
    # Launch the Chrome browser
    driver = webdriver.Chrome(options=chrome_options)
    count = 1000
    try:
        previous_link = None
        driver.get(channel_url)
        sleep(1)
        with open('test_cookies.pkl', 'rb') as f:
            cookies = pickle.loads(f.read())
            # print(cookies)

        for cookie in cookies:
            driver.add_cookie({'name': cookie['name'], 'value': cookie['value']})
        driver.refresh()
        
        while True: 
            # Open the YouTube channel URL
            # driver.get(channel_url)
            # sleep(1)
            # with open('test_cookies.pkl', 'rb') as f:
            #     cookies = pickle.loads(f.read())
            #     # print(cookies)

            # for cookie in cookies:
            #     driver.add_cookie({'name': cookie['name'], 'value': cookie['value']})

            # driver.refresh()
            #print("hi")
            # Wait for the videos to load (increased timeout to 30 seconds)
            # videos
            result = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.yt-simple-endpoint.focus-on-expand.style-scope.ytd-rich-grid-media')))
            # shorts
            #result = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.yt-simple-endpoint.focus-on-expand.style-scope.ytd-rich-grid-slim-media')))
            
            # print(result)
            # #log.debug(result)
            
            # # Find the first video element1
            # video_element = driver.find_element(By.CSS_SELECTOR, 'ytd-rich-grid-media')
            # print("video element:", video_element)
            # Get the title of the first video
            video_link = None
            for element in result:
                video_link = element.get_attribute('href')
                break
            #video_link = driver.find_element(By.CSS_SELECTOR, '#video-title-link').get_attribute('href')
            
            if video_link != previous_link:
                print("New video title:", video_link)
                previous_link = video_link
                # first_comment(count)
                count += 1
                
        
            sleep(1)
            #print("checking...")
            driver.refresh()
        # You can implement further logic here to compare the latest video title with a previously stored title to check for new uploads
        
    finally:
        # Close the browser
        driver.quit()

# Example usage: provide the URL of the YouTube channel you want to check
channel_url = "https://www.youtube.com/feed/subscriptions"
check_for_new_video(channel_url)
