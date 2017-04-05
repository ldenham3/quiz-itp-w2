def eldest_customer_per_state(customers):
    newDict = {}
    for state,customer_info in customers.items():
        oldest = 0
        if customer_info:
            for person in customer_info:
                if person:
                    if person['age'] > oldest:
                        newDict[state] = person
                        oldest = person['age']
        else:
            newDict[state] = None
    return newDict
