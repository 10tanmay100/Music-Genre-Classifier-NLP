# importing libraries
import os, sys


#defining class for custom exception
class music_genre_exception(Exception):

    def __init__(self,error_msg:Exception,error_details:sys):
        super().__init__(error_msg)
        self.error_msg=music_genre_exception.get_detailed_error_msg(error_msg=error_msg,error_details=error_details)


    @staticmethod
    def get_detailed_error_msg(error_msg:Exception, error_details:sys):
        _,_,exc_tb=error_details.exc_info()
        line_number=exc_tb.tb_lineno
        filename=exc_tb.tb_frame.f_code.co_filename

        error_msg=f"Error occured in script: [{filename}] at line number: [{line_number} and error message: {error_msg}]"

        return error_msg
    

    def __str__(self):
        return self.error_msg
    
    def __repr__(self):
        return music_genre_exception.__name__.str()






