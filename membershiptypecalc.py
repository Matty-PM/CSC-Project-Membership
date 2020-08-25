x = 'global'

def membertype(membership_total):
    if membership_total > 0 and membership_total < 999:
        print("x inside:", x)

    elif membership_total > 1000 and membership_total < 1199:
        print("Bronze Membership")

    elif membership_total > 1200 and membership_total < 1499:
        print("Silver Membership")

    else:
        print("Gold Membership")

membertype()
print("x outside:", x)