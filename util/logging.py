"""
Logging class
Author: Alex (TheAmazingAussie)
"""

def line(output_line=''):
    """
    Prints output line with no tag
    :param output_line: the line to print
    """

    print (output_line)
    return


def info(output_line=''):
    """
    Prints output line with [INFO] tag
    :param output_line: the line to print
    """

    print ("[INFO] " + output_line)
    return


def session(output_line=''):
    """
    Prints output line with [INFO] tag
    :param output_line: the line to print
    """

    print ("[SESSION] " + output_line)
    return


def error(output_line=''):
    """
    Prints output line with [ERROR] tag
    :param output_line: the line to print
    """

    print ("[ERROR] " + output_line)
    return


def write_to_file(file_path, file_data):
    """
    This method will write to a file with the specified file path and file data
    :param file_path : The path to the file
    :param file_data : The data to write to the file
    """
    text_file = open(file_path, "w")
    text_file.write(file_data)
    text_file.close()
