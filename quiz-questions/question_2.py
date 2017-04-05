def number_of_customers_per_state(customers):
    newDict = {}
    if type(customers) == dict and customers != {}:
        for key in customers:
            if customers[key] != 0 and customers[key] != None:
                newDict[key] = len(customers[key])
            else:
                newDict[key] = 0
    else:
        return {}
    return newDict
