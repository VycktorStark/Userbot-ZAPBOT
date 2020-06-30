from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from method import Method
import traceback, os

"""
Set the name of a group or contact for the bot to open the chat after responding to someone, 
this is part of the polling
"""
contactorgroupname = "esperaumpouco"

def whatsapp(drive, api):
	"""
	This function will be the heart of the project, 
	it will be responsible for analyzing if there is a new chat waiting for an answer 
	and responding within the pre-defined functions.
	"""
	name = message = ''
	wait = api.waittemp(temp=1)
	unread = driver.find_elements_by_class_name(api.newmsg)
	if len(unread) > 0:
		__unread = unread[-1]
		action = ActionChains(driver)
		action.move_to_element_with_offset(__unread, 0, -20)
		try:
			action.click(); action.perform(); action.click(); action.perform()
		except Exception as error:
			pass
		try:
			"""
			here the interaction between the bot and the user takes place, 
			the bot will read the predetermined settings, as in the examples below
			"""
			name = driver.find_element_by_class_name(api.nome).text 
			message_content = driver.find_elements_by_class_name(api.chatdados)[-1]
			message = message_content.text.lower()
			if len(message) > 0:
				if (message == "/ping"):
					api.sendResponse(response='PONG')
				elif (message == "/img"):
					api.sendMedia(file=os.path.dirname(os.path.realpath(__file__)) + '/img/Prev.png')
				elif (message == "/doc"):
					api.sendDocument(file=os.path.dirname(os.path.realpath(__file__)) + '/main.py')
		except Exception as error:
			traceback.print_exc()
			pass
		driver.find_element_by_xpath(f"//span[@title='{contactorgroupname}']").click()
	api.waittemp(slp=1)


if __name__ == '__main__':
	options = webdriver.ChromeOptions()
	options.add_argument("user-data-dir={}".format(os.path.join(os.getcwd(), "profile", "wpp")))
	driver = webdriver.Chrome(executable_path='chromedriver', options=options)
	meth = Method(driver)
	meth.waittemp(temp=1)
	driver.get("https://web.whatsapp.com/")
	try:
		while True:
			whatsapp(driver, meth)
	except KeyboardInterrupt:
			print("\nClosing bot ...")
