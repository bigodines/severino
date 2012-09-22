import os
import sys
import json
from pprint import pprint
import selenium.webdriver as webdriver

class SeverinoCapture(object):

	def __init__(self):
		json_data=open('config/config.json')
		data = json.load(json_data)
		self.selenium = data["selenium"]
		self.pages = data["pages"]
		self.screenshots_dir = data["severino"]["screenshots_dir"]
		if not os.path.exists(self.screenshots_dir):
			os.makedirs(self.screenshots_dir)

		json_data.close()

	def visit_and_capture(self):
		server = self.selenium["server"]
		browsers = self.selenium["browsers"]
		pages = self.pages

		print server
		
		for browser in browsers:		
			remote = server
			caps = { "browserName": browser }
			driver = webdriver.Remote(command_executor=remote, desired_capabilities=caps, browser_profile=None)
			for page in pages:
				print browser + " - " + page
				driver.get(pages[page]["url"])
				screenshot_filename = browser + "-" + pages[page]["filename"]
				driver.get_screenshot_as_file(self.screenshots_dir + screenshot_filename)
			driver.quit()
