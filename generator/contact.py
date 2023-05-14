from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", last_name="", address="",
                    homephone="", mobilephone="", workphone="",
                    secondaryphone="", email="", email2="", email3="")] \
           + [Contact(first_name=random_string("name", 10), last_name=random_string("name", 10),
                      address=random_string("name", 10), homephone=random_string("name", 11),
                      mobilephone=random_string("name", 11), workphone=random_string("name", 11),
                      secondaryphone=random_string("name", 11), email=random_string("name", 10),
                      email2=random_string("name", 10), email3=random_string("name", 10))
              for i in range(5)
              ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode((testdata)))