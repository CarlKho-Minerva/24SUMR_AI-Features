# video_recommender/utils.py
from pprint import pprint


def debug_print(msg, function_name):
    """
    Helper function to print debug messages.

    Parameters:
    msg (str): Message to be printed.
    function_name (str): Name of the function where the debug print is called.
    """
    print(f"START ------- DEBUG (INFUNC): {function_name}\n")
    pprint(msg)
    print(f"\nEND ------- DEBUG (INFUNC): {function_name}\n\n\n")
