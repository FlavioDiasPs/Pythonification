"""A module for demonstrating exceptions."""

def convert(s):
    """Convert to integer"""
    try:        
        return int(s)        
    except (ValueError, TypeError) as e:
        print("Convertion error: {}".format(str(e)), file=sys.stderr)
        return -1
    
convert("sdgfdshdg")
convert([1, 2, 34])
convert(1)

from math import log
def string_log():
    v = convert(s)
    return log(v)

string_log("sdgdfhgd")