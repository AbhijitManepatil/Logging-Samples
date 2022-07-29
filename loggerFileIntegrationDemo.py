#Logs
'''
#Logs level
Debug
Info
warning
error
Critical
'''


#*Sample
import logging

#wrapping all logging object in a function
def loggingFunc():
	#object
	#object is reponsible logging

	logger=logging.getLogger(__name__) #__name__ Capture file name

	# which file to store logs #and format of logging
	fileHandler=logging.FileHandler('pythonAPIlogfile.log')
	#format of logging
	formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(filename)s->%(funcName)s() : %(message)s")
	#connect formatter to file handler
	fileHandler.setFormatter(formatter)
	#connect handler to logger object
	logger.addHandler(fileHandler)  #fileHandler object


	#set level to get those levels logs in log file
	logger.setLevel(logging.DEBUG)
    
	# #use logger type to add logger message 
	# logger.debug("A debug statement")
	# logger.info("Information message")
	# logger.warning("Warning message")
	# logger.error("A major error")
	# logger.critical("Critical issue")
	return logger

logger=loggingFunc()

def myfun():
	logger.info("I am from a Test Integration:")

myfun()