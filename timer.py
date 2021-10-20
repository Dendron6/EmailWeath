import time
from test import *

repetitions = 3
intervals = 60

while repetitions>0:
    repetitions-=1
    time.sleep(intervals)
    sendEmail()
    print("email sent")