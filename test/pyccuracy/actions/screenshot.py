from pyccuracy.actions import ActionBase
from pyccuracy.errors import ActionFailedError

class ScreenshotAction(ActionBase):
	regex = r'(And )?I take a screenshot'

	def execute(self, context, whatever):
		browser = context.settings.browser_to_run
		page = context.current_page.__class__.__name__
		filename = browser + "-" + page + ".png"
		
		raise ActionFailedError(filename)
