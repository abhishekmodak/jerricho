
USERNAME = "*********"
PASSWORD = "*********"

# from time import sleep
# from selenium import webdriver
#
#
# def insta_process_selenium():
#     """
#     Using selenium to log in intagram, not in use
#     """
#     # browser = webdriver.Firefox()
#     browser = webdriver.Firefox(executable_path='/Users/abhishek/Downloads/geckodriver')
#
#     browser.get('https://www.instagram.com/')
#     sleep(10)
#     username_input = browser.find_element_by_name("username")
#     password_input = browser.find_element_by_name("password")
#
#     username_input.send_keys(USERNAME)
#     password_input.send_keys(PASSWORD)
#
#     login_button = browser.find_element_by_xpath("//button[@type='submit']")
#     login_button.click()
#     sleep(50)
#
#     browser.close()


from instapy import InstaPy


def insta_functionalities():
    session = InstaPy(username=USERNAME, password=PASSWORD).login()
    session.login()

    session.set_relationship_bounds(enabled=True, max_followers=500)
    session.set_do_follow(True, percentage=50)
    session.set_dont_like(["naked", "nsfw", "islam", "allah"])
    session.like_by_tags(["fitness", "bodybuilding"], amount=5)

    # session.set_do_comment(True, percentage=50)
    # session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])

    session.end()


insta_functionalities()


# from instapy_cli import client
#
# def post_image_inst():
#     """
#     Posting image in instagram, not working
#     """
#     image = '/Users/abhishek/Desktop/im1.jpg' #here you can put the image directory
#     text = '#fitness'
#
#     with client(USERNAME, PASSWORD) as cli:
#        cli.upload(image, text)


# from instabot import Bot
#
#
# def post_image_inst():
#     """
#     Posting image in instagram, working
#     """
#     bot = Bot()
#
#     bot.login(username=USERNAME,
#               password=PASSWORD)
#
#     # Recommended to put the photo
#     # you want to upload in the same
#     # directory where this Python code
#     # is located else you will have
#     # to provide full path for the photo
#     bot.upload_photo("/Users/abhishek/Desktop/im1.jpg",
#                      caption='#fitness')
