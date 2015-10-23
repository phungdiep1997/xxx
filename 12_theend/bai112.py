import virtualenv
virtualenv.create_environment("xxx")
this_file = "xxx/bin//activate_this.py"
execfile(this_file, dict(__file__=this_file))
import subprocess
subprocess.call(["pip", "install", "requests"])
