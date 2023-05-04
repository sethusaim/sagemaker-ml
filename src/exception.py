import sys


def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    This function returns a detailed error message including the name of the Python script, line number,
    and error message.
    
    Args:
      error (Exception): The error parameter is an Exception object that represents the error that
    occurred in the code. It could be any type of exception such as ValueError, TypeError, etc.
      error_detail (sys): The `error_detail` parameter is expected to be an instance of the `sys`
    module, which is used to access information about the Python interpreter and its environment.
    Specifically, the `exc_info()` method of the `sys` module is used to retrieve information about the
    current exception being handled by the
    
    Returns:
      a string that contains details about the error that occurred, including the name of the Python
    script where the error occurred, the line number where the error occurred, and the error message
    itself.
    """
    _, _, exc_tb = error_detail.exc_info()

    file_name: str = exc_tb.tb_frame.f_code.co_filename

    error_message: str = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        """
        This is a class that initializes an error message and its details and returns the error message as a
        string.
        
        Args:
          error_message (Exception): The error message that will be displayed when the exception is raised.
          error_detail (sys): The `error_detail` parameter is of type `sys`, which is a module in Python
        that provides access to some variables used or maintained by the interpreter and to functions that
        interact strongly with the interpreter. It is likely that this parameter is used to provide
        additional information about the error that occurred, such as
        """
        super().__init__(error_message)

        self.error_message: str = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
