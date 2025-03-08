class NegNumErr(Exception):
    pass

def chknum(value):
    if value < 0:
        raise NegNumErr("Negative numbers are not allowed!")
    print("Great! You entered:", value)

try:
    num = int(input())
    chknum(num)
except NegNumErr as e:
    print("Oops! Error:",e)
