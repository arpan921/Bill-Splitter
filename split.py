from methods import is_member_present_in_dict

members = input("Enter names of all members (give comma ',' in between names):").split(',')
cost_for_each = dict.fromkeys(members, 0.0)
print(cost_for_each)
any_item_left=True
item_count=0
while (any_item_left):
    print(f"This is for item {item_count+1}")
    item_price = float(input("Price:"))
    divided_among = input("Enter list of members the item is divided using comma in between/type 'all' if you want to select all persons:").split(',')
    if divided_among[0]=='all':
        divided_among=members
    cost_on_each = item_price/len(divided_among)
    for member in divided_among:
        if is_member_present_in_dict(cost_for_each,member):
            cost_for_each[member] += cost_on_each
    print(cost_for_each)
    any_item_left = eval(input("Any item left? True or False:"))
    item_count += 1
    print("-------------------------------------------------------------------------------------------")

print(f"Cost per member before any adjustments: {cost_for_each}")
adjustment_needed=False
adjustment_needed = eval(input("Any adjustments needed? True or False:"))

if adjustment_needed:
    adjustment_members=input("Name members for whom adjustment is needed:")
    for member in adjustment_members.split(','):
        if is_member_present_in_dict(cost_for_each,member):
            adjust_amount = float(input(f"Enter amount to be adjusted for {member}:"))
            cost_for_each[member]-=adjust_amount
print(f"Final amount to be payed after adjustments: {cost_for_each}")



