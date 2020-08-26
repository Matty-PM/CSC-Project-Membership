def membershipdiscountammount(membership_type):
    if membership_type == "Gold Membership":
        global membership_discount
        membership_discount = 15

    elif membership_type == "Silver Membership":
        membership_discount = 10

    elif membership_type == "Bronze Membership":
        membership_discount = 5
    
    else:
        membership_discount = 0
