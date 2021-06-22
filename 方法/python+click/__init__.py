
filename = "click_1"
classname = "say_hello"
action = exec(f"from {filename} import {classname}")
action2 = exec(f"obj = {classname}()")