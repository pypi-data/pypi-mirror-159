import sys
from . import *
def run():
	if len(sys.argv) != 2:
		args_text = sys.argv
		del args_text[0]
		args_text = " ".join(args_text)
		logger.error("Systax of arguments:\n\t python %s <number>\nYou input this:\n\tpython %s %s" % (__file__, __file__, args_text))
		sys.exit(1)
	try:
		main(int(sys.argv[1]))
	except ValueError:
		logger.error("!!!!!!!number is NUMBER!!!!!!")
		sys.exit(1)
if __name__ == "__main__":
	run()
