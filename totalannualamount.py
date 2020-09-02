import userpackages

def calctotalannualammout():
    global userid
    userid = int(input("Enter User ID:")) 

    if userid in userpackages.member_id:
     print("Yes, '2134' found in List : " , userpackages.member_id)

    global membership_total
    membership_total = 500