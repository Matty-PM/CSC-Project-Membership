def membershiptype(membership_total):
    if membership_total > 0 and membership_total < 999:
        global membership_type
        membership_type = "Regular Membership"

    elif membership_total > 1000 and membership_total < 1199:
        membership_type = "Bronze Membership"

    elif membership_total > 1200 and membership_total < 1499:
        membership_type = "Silver Membership"

    else:
        membership_type = "Gold Membership"