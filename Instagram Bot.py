#NOTE - remember to "pip install selenium" ,or else the code wont work lol :P



from selenium import webdriver #importing selenium instead of beautifulSoup because BS is for web dev types and selenium is majorly
#for automating stuff on the web

from webdriver_manager.chrome import ChromeDriverManager
#did so bcz it's easier for me to not care to put the "chromedrive.exe" in path and the whole task is itself managed by chromeDriverManager
from time import sleep

#just so that to give a pause in b/w our code

#driver = webdriver.Chrome(ChromeDriverManager().install())

class InstaBot:
	def __init__(self,insta_username,insta_password):
		self.insta_username = insta_username
		self.insta_password = insta_password

		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		#self.driver = webdriver.Chrome()
		#self.driver.get("https://instagram.com")
		self.driver.get("https://www.instagram.com/accounts/login/")
		sleep(2)

		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(insta_username) #entering user's username

		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(insta_password) #entering user's passwrod
		self.driver.find_element_by_xpath('//button[@type="submit"]').click() #clicking the login button
		sleep(4) #sleeping for a while

	def get_unfollowers(self):
		self.driver.get("https://www.instagram.com/"+self.insta_username) #now to avoid the whole "NOT NOW " section that pops up , i directly opened the #profile of the user to have an easy access of the user's followers and following list
		
		#prinitng the list of followers
		self.driver.find_element_by_partial_link_text("follower").click()
		

#		print("FOLLOWERS")
		my_followers = self._get_names() #my followers meaning jo mujhe follow krte hai

#		print("people in your instagram FOLLOWERS are = ",my_followers) #names of my followers
		#task done

		#printing the list of FOLLOWING

#		print("FOlLOWING")
		self.driver.find_element_by_partial_link_text("following").click()
		my_following = self._get_names() # my following meaning jinko me follow krta hu
#		print("people in your instagram FOlLOWING are = ",my_following) #names of my followers
		#task done

		#printing list of people not following you back 

		people_not_following_back = not_following_back = [user for user in my_following if user not in my_followers]
		print("People NOT FOlLOWING YOU BACK ARE = " , people_not_following_back) 



	def _get_names(self):
		sleep(2)
		scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
		last_ht = 0
		ht =1
		while last_ht != ht:
			last_ht = ht
			sleep(1)
			ht  = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight;""", scroll_box)

		
		links = scroll_box.find_elements_by_tag_name('a') # "elements" use krna hai instead of "element"
		names = [name.text for name in links if name !=' ']
	#	print("people in your instagram are = ",names) #names of my followers

		self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click() #closes followers tab

		return names 
	



your_username = "ENTER your username here in b/w the quotes"
your_password = "enter your password here in b/w the quotes"

my_insta_bot = InstaBot(your_username,your_password)
my_insta_bot.get_unfollowers()


