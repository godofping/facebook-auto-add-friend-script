from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By



class FacebookBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()

	def login(self):
		bot = self.bot
		bot.get('https://www.facebook.com/')
		time.sleep(3)
		email = bot.find_element_by_id('email')
		passw = bot.find_element_by_id('pass')

		email.clear()
		passw.clear()

		email.send_keys(self.username)
		passw.send_keys(self.password)
		passw.send_keys(Keys.RETURN)
		time.sleep(3)
	
	def addFriend(self, key_words):
		bot = self.bot
		bot.get('https://www.facebook.com/search/people/?q=' + key_words + '&epa=SEARCH_BOX')
		time.sleep(3)
		for i in range(1,5):
			bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
			time.sleep(2)
			friends = bot.find_elements_by_class_name('_2ial')
			links = [elem.get_attribute('href') for elem in friends]



			for link in links:
				bot.get(link)
				time.sleep(10)

				bot.find_elements_by_class_name("addButton")[0].click()
				
#change the email, pass and keyword
re = FacebookBot('email','pass')
re.login()
re.addFriend('keyword')
