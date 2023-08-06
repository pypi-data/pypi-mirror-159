def is_exec():
    import sys
    if getattr(sys, 'frozen', False):
        return True
    else:
        return False
def get_dir():
    import os
    if is_exec():
        import sys
        mydir=os.path.dirname(os.path.abspath(sys.executable))
    else:
        mydir=os.path.dirname(os.path.abspath(__file__))
    return mydir