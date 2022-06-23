import select
import sys
from io import StringIO


def processSomething():
    # text = sys.stdin.readline().rstrip()
    print("Do something")
    # if text:
    #     sys.stdin = StringIO(text)
    pass


while True:
    input_ = select.select([sys.stdin], [], [], 1)[0]
    if input_:
        value = sys.stdin.readline().rstrip()

        if (value == "q"):
            print("Exiting")
            sys.exit(0)
        else:
            print("You entered: %s" % value)

    else:
        processSomething()
