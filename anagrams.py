def anagrams_builtin(string1, string2):
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()

    string1 = sorted(string1)
    string2 = sorted(string2)

    return string1 == string2

# testing
print(" Clint Eastwood and Old West Action: " + str(anagrams_builtin('Clint Eastwood', 'Old West Action')))

print("Dog and God: " + str(anagrams_builtin('dog', 'God')))

print("Public relations and crap built on lies: " + str(anagrams_builtin('Public relations', 'crap built on lies')))

print("Cat and Taco: " + str(anagrams_builtin('cat', 'taco')))