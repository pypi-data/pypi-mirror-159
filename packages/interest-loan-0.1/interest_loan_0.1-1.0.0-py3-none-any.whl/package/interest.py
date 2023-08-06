def interest():
    p = float(input("Principal Amount : "))
    r = float(input("Interest Rate : "))
    m = int(input("Enter Months : "))
    y = int(input("Enter Years : "))
    if m != 0:
        i = ((p * m) / 1200) * r
        if y != 0:
            j = ((p / 100) * r) * y
            t = i + j
            t1 = p + t
            print("Interest Earned : ", t, "\nTotal Amount(Principal + Interest) : ", t1)
        else:
            t1 = p + i
            print("Interest Earned : ", i, "\nTotal Amount(Principal + Interest) : ", t1)
    else:
        if y != 0:
            j = ((p / 100) * r) * y
            t1 = p + j
            print("Interest Earned : ", j, "\nTotal Amount(Principal + Interest) : ", t1)
        else:
            d = int(input("Enter Days :"))
            j = ((p * d) / 37037) * r
            t1 = p + j
            print("Interest Earned : ", j, "\nTotal Amount(Principal + Interest) : ", t1)

