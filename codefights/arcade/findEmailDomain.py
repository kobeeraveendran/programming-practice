def findEmailDomain(address):
    address = address[::-1]

    return address[address.index('@') - 1::-1]