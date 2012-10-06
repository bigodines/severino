from pyccuracy.actions import ActionBase
from pyccuracy.errors import ActionFailedError
import os

class ScreenshotAction(ActionBase):
	regex = r'(And )?I take a screenshot'

	def execute(self, context, whatever):
		browser = context.settings.browser_to_run
		page = context.current_page.__class__.__name__
		filename = browser + "-" + page + ".png"
		
		#TODO: save to the base severino folder
		path =  "screenshots/" + page
		
		if not os.path.exists(path):
			os.makedirs(path)
		
		#TODO: increment file names
		finalpath = path + "/" + filename

		if hasattr(context.browser_driver, 'selenium'):
			context.browser_driver.selenium.save_screenshot(finalpath)
		elif hasattr(context.browser_driver, 'webdriver'):
			context.browser_driver.webdriver.get_screenshot_as_file(finalpath)
