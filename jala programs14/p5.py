def exception():
    raise Exception("This is a custom exception message.")

try:
    exception()
except Exception as e:
    print("Caught Exception:",str(e))
