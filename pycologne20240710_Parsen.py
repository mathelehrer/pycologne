# ideas:
# Context Manager:
# trail and error parser

class FormatMismatch(Exception):
    pass

class ValueError:
    """
    Context manager that catches all ValueErrors within the context and reraises them as FormatMismatches
    """
    def __enter__(self):
        pass
    def __exit__(self,exc_type,exc_value,exc_traceback):
        if exc_type:
            if issubclass(exc_type,ValueError):
                raise FormatMismatch from exc_value
# context manager are initialted with with ...

# for else-Schleife
target = 12


for i in range(1,target):
    if i%11==0:
        break
else:
    print("11 hasn't been reached")
