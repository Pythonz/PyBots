import os
import sys

for cmd in os.listdir("bots"):
	if cmd.endswith(".py"):
		cmd = ' '.join(cmd.split(".")[:-1])
		if cmd != "__init__":
			if not sys.modules.has_key("commands."+cmd):
				exec("import bots."+cmd)
			else:
				exec("reload(bots."+cmd+")")
