import sys

def error_message_details(error,error_details:sys):
    '''
    exc_info( ) If the current thread is handling an exception, 
    exc_info returns a tuple whose three items are the class, object, and traceback 
    for the exception. If the current thread is not handling any exception, 
    exc_info returns (None,None,None) 
    '''
    _,_, exc_tb = error_details.exc_info()

    # To get the file name where exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class SensorException(Exception):
    def __init__(self,error_message,error_details):
        '''
        :param error_message: error message in string format
        '''


        #The super() function is used to give access to methods and properties of a parent or sibling class.
        # The super() function returns an object that represents the parent class.
        super().__init__(error_message)

        self.error_message = error_message_details(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message

