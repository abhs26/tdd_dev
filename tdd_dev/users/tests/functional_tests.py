from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')

print(browser.title)

#User has heard about our webpage. User
#go to the website through the webbrowser
browser.get('http://127.0.0.1:8000')

#When page opens user see tdd_dev in title
assert 'tdd_dev' in browser.title


#user is interested to signup
#user clicks on the signup button

#new page opens
#User see all the fields
#email , username, password, retype password and signup button


#User Enters the fields value


#user enter the submit

#user see the email confirmation mail

