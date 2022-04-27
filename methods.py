def is_member_present_in_dict(cost_for_each,member):
    for each in member:
        if member in cost_for_each:
            return True
        else:
            return False