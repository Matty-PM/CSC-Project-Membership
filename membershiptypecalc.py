def membertype(package_value):
    if package_value > 0 and package_value < 999:
        print("Regular Membership")

    elif package_value > 1000 and package_value < 1199:
        print("Bronze Membership")

    elif package_value > 1200 and package_value < 1499:
        print("Silver Membership")

    else:
        print("Gold Membership")