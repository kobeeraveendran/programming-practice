def bankRequests(accounts, requests):
    
    for request in range(len(requests)):
        parsed = request.split(' ')

        if len(parsed) > 4 or len(parsed) < 3:
            return [-1]
        
        if parsed[0] == 'transfer':
            i = eval(parsed[1])
            j = eval(parsed[2])
            sum_amt = eval(parsed[3])
            # remove sum from i - 1 and add to j - 1 if available
            if i - 1 >= len(accounts) or i - 1 < 0 or j - 1 >= len(accounts):
                return [0 - (request + 1)]
            
            if accounts[i - 1] - sum_amt >= 0:
                accounts[i - 1] -= sum_amt
                accounts[j - 1] += sum_amt
            else:
                return [0 - (request + 1)]
        
        elif parsed[0] == 'deposit':
            # add sum to i - 1
            i = eval(parsed[1])
            sum_amt = eval(parsed[2])

            if i - 1 >= len(accounts) or i - 1 < 0:
                return [0 - (requests + 1)]

            accounts[i - 1] += sum_amt
        
        elif parsed[0] == 'withdraw':
            # if subtracting sum doesn't result in negative
            # results, withdraw sum

            i = eval(parsed[1])
            sum_amt = eval(parsed[2])

            if i - 1 >= len(accounts) or i - 1 < 0:
                return [0 - (request + 1)]

            if accounts[i - 1] - sum_amt >= 0:
                accounts[i - 1] -= sum_amt
            
            else:
                return [0 - (request + 1)]

    return accounts