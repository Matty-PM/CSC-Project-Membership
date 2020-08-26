import packages
import totalannualamount
import membershiptypecalc
import membershipdiscountcalc

var = "%"

totalannualamount.calctotalannualammout()
membershiptypecalc.membershiptype(totalannualamount.membership_total)
membershipdiscountcalc.membershipdiscountammount(membershiptypecalc.membership_type)

print("Customer Membership is", membershiptypecalc.membership_type, "and the customer is entitled to a", membershipdiscountcalc.membership_discount, var, "discount.")
print(totalannualamount.userid)