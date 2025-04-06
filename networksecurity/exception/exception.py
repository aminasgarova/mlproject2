# Import the sys module to access exception details (like traceback)
import sys
# Importing a custom logger from your logging module inside the project
from networksecurity.logging import logger


# Define a custom exception class for your project
class NetworkSecurityException(Exception):
    # Constructor takes the error message and error details from sys
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message  # Store the actual error message
        
        # Unpack the exception traceback object using sys.exc_info()
        # exc_info() returns a tuple (type, value, traceback)
        _, _, exc_tb = error_details.exc_info()
        
        # Get the line number where the exception occurred
        self.lineno = exc_tb.tb_lineno      
        # Get the filename where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename 

    # Define string representation of the exception
    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )


## Test
# if __name__ == '__main__':
#     try:
#         logger.logging.info("Enter the try block")
#         a = 1 / 0
#         print("This will not be printed", a)

#     except Exception as e:
#         raise NetworkSecurityException(e, sys)
