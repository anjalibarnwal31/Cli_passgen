import string
import random
import argparse

parser = argparse.ArgumentParser(description="Password Generator")
parser.add_argument('-p', '--place', type=str, help="Website where u want to use",default='google')
parser.add_argument('-l', '--len', type=int, help="Length of the Password",default=7)
args = parser.parse_args()


def passgenA(venue, length):
    password = []
    a = string.ascii_letters
    b = string.digits
    c = "#@$&*^%"
    password.extend(a)
    password.extend(b)
    password.extend(c)
    random.shuffle(password)

    # pn = password[:length]
    pn=[]
    for i in range(length):
        pn.append(random.choice(password))
    random.shuffle(pn)
    a = "".join(pn)
    # return a
    print(a)
    f = open("password.txt", 'a')
    f.write(venue)
    f.write(" :- ")
    f.write(a)
    f.write('\n')
    f.close


if __name__ == '__main__':
    passgenA(args.place, args.len)