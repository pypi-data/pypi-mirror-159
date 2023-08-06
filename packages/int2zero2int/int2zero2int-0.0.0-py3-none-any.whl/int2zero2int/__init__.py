import sys
from slogger import SLogger
logger = SLogger("int2zero2int")
def main(number: int):
	# !!! START !!!
	main_number_list = list(range(-number, number))
	for num in main_number_list:
		logger.info(str(str(num) + "-").replace("-", ""))
		# !!! END !!!
if __name__ == "__main__":
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
