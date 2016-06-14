#!/usr/bin/env python

def getUser(num):
    identifiers = ["id1"]
    logins = ("root",)
    passwords = {logins[0]: "arnd9al0"}

    massive = "{0}\n{1}\n{2}\n".format(str(identifiers[num]), str(logins[num]), str(passwords[logins[num]]))
    return massive


def writeUser():
    output = open("plain.decrypted", "w")
    file = "plain.decrypted"

    output.write(getUser(0))
    output.close()

    with open(file) as fn:
        content = fn.readlines()

    return content


print(writeUser())
