#!/usr/bin/env python

def checkAuth(password, attempt):
    status = 0
    session = 0

    while session != attempt:
        review = str(input("Enter your password: "))
        if review == password:
            status = "Access Allow"
            break
        else:
            status = "Access Denied"
            session += 1

    return status


print(checkAuth(" ", 3))
