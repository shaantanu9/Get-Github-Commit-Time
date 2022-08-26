import email
from warnings import catch_warnings
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Some of the Above Package are auto Imported or used while build this so please ignore it will correct it and

# Import JSON library
import json

j = 1
i2 = 0

# Get Student Github links from JSON file
filename = ''  # filename of
# Import json file
with open(f'./{filename}.json') as json_file:
    student_list = json.load(json_file)

# open an webpage in a browser
browser = webdriver.Chrome()

email = 'shantanubombatkar2@gmail.com'  # //
password = ''  # your password should be here


# # open the github page
browser.get('https://github.com/login')

# # wait till the page loads completely
time.sleep(5)

browser.find_element(By.ID, 'login_field').send_keys(email)
browser.find_element(By.ID, 'password').send_keys(password)

# # Click Enter to login
browser.find_element(By.ID, 'password').send_keys(Keys.ENTER)

# # wait till the page loads completely
time.sleep(15)


# # Open in New Tab
browser.execute_script("window.open('')")

# # Switch to that new tab
browser.switch_to.window(browser.window_handles[j])

# # browser.get(url)
j += 1


def commit_github_time(student_list):

    for i in student_list:
        # if i["IA Name"] == 'Shantanu Gajanan Bombatkar':
        # Get the student github link from
        # github_link = i['githubLink']
        try:
            # print(i['githubLink']) #githubLink
            browser.get(i['githubLink'])
            time.sleep(3)

            # get inspect page code
            # page_source = browser.page_source
            # print(page_source)

            # //*[@id="repo-content-pjax-container"]/div/div/div[3]/div[1]/div/div[2]/div[2]/a[2]/relative-time
            commitTime = browser.find_element(
                By.TAG_NAME, 'relative-time')
            title = commitTime.get_attribute('title')
            dataTime = commitTime.get_attribute('datetime')
            i["commitTime"] = dataTime
            i["commitTitle"] = title
            # i["gitLink"] = i['githubLink']
            # i[]
            print(i["commitTime"], "\n [commitTitle]")
            print(i["commitTitle"], "\n [commitTitle]")

            print(i)

            # Save the data to a json file
            # time.sleep(5)
            # save_file(i)

            # # Open in New Tab
            # browser.execute_script("window.open('')")

            # # Switch to that new tab
            # browser.switch_to.window(browser.window_handles[j])

            # if i2>10:
            # # browser.get(url)
            # j += 1

        except:
            print("Error")
            continue
        # break
        # open an webpage in a browser from

        # Save the data to a json file
        file = open(f'aaa{filename}AugLastTime.txt', 'a')
        file.write(str(i))
        file.close()

    # browser.get(i['githubLink'])

    # # # Open in New Tab
    # browser.execute_script("window.open('')")

    # # # Switch to that new tab
    # browser.switch_to.window(browser.window_handles[j])
    # # # browser.get(url)
    # j += 1
commit_github_time(student_list)


# def save_file(i):
#     # Save the data to a json file
#     with open('./edited17julyFunction.json', 'a') as my_data_file:
#         json.dump(i, my_data_file)
#         my_data_file.write('\n')
#         print('Saved')
