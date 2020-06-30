from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

class Method:
	def __init__(self, driver):
		self.driver = driver
		self.wait = self.waittemp(temp=1)
		self.newmsg = '_31gEB',
		self.nome = '_3ko75',
		self.chatdados = '_3Whw5',
		self.aguarde = self.waittemp(slp=3)

	def chatatual(self):
		return self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@contenteditable='true'])[2]")))
	
	def sendResponse(self, response):
		self.chatatual().send_keys(response)
		botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
		self.waittemp(slp=1)
		botao_enviar.click()

	def sendMedia(self, file=False, captiontext=False):
		try:
			clip = self.driver.find_element_by_xpath("//span[@data-icon='clip']")
			clip.click()
			sleep(0.5)
			media = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
			media.send_keys(file)
			self.aguarde
			if (captiontext):
				caption = self.driver.switch_to.active_element
				caption.send_keys(captiontext)
				self.aguarde
			botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
			botao_enviar.click()
		except Exception as error:
			print(error)

	def sendDocument(self, file=False):
		try:
			clip = self.driver.find_element_by_xpath("//span[@data-icon='clip']")
			clip.click()
			sleep(0.5)
			media = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@accept="*"]')))
			media.send_keys(file)
			self.aguarde
			botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
			botao_enviar.click()
		except Exception as error:
			print(error)

	def waittemp(self, temp=False, slp=False):
		if (temp):
			return WebDriverWait(self.driver, temp)
		elif (slp):
			sleep(slp)
			return "ok"
		else:
			return False