expenses = []

def get_next_id() :
    if expenses == [] :
        return 1
    else :
        max_id = 0
        for expense in expenses :
            if expense['Id'] > max_id :
                max_id = expense['Id']

        return max_id + 1
