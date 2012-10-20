# Temporary file just to illustrate how to capture

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'severino'))
from severino import severino
from ...app.capture import capture

capturer = capture.SeverinoCapture()
capturer.visit_and_capture()
