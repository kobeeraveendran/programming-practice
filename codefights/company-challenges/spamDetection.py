from fractions import Fraction
import re

def spamDetection(messages, spamSignals):
    num_messages = len(messages)

    test_output = []
    test1 = 0
    test2 = {}
    test3 = {}
    test4 = set()
    spam_msg_count = 0

    for message in messages:
        # split on any non-alphabetic character
        if len(re.split(r'[^a-zA-Z]+', message[0])) < 5:
            test1 += 1

        # dict is of structure {user: {message: count}}
        test2[message[1]] = test2.get(message[1], {})
        test2[message[1]][message[0]] = test2[message[1]].get(message[0], 0) + 1

        # update frequency of message
        test3[message[0]] = test3.get(message[0], 0) + 1

        # counts messages containing any spam word, and adds
        # those words to a set
        contains_spam = False
        for spamSignal in spamSignals:
            if re.search(r'\b' + spamSignal.lower() + r'\b', message[0].lower()):
                test4.add(spamSignal.lower())
                if not contains_spam:
                    spam_msg_count += 1
                    contains_spam = True

    # test1 check
    if test1 / num_messages > 0.9:
        test_output.append('failed: ' + str(Fraction(test1, num_messages))) if test1 != num_messages else test_output.append('failed: 1/1')
    else:
        test_output.append('passed')

    # test2 check
    spammed_users = []
    for user in test2:
        msgs_received = sum(test2[user].values())
        for msg, count in test2[user].items():
            if msgs_received == 1:
                continue
            elif count / msgs_received > 0.5:
                spammed_users.append(user)

    spammed_users.sort()

    if len(spammed_users) > 0:
        test_output.append('failed: ' + ' '.join(spammed_users))
    else:
        test_output.append('passed')

    # test3 check
    if num_messages == 1:
        test_output.append('passed')
    else:
        for msg in test3:
            if test3[msg] / num_messages > 0.5:
                test_output.append('failed: ' + msg)
                break

    if len(test_output) < 3:
        test_output.append('passed')

    # test4 check
    if spam_msg_count / num_messages > 0.5:
        test_output.append('failed: ' + ' '.join(sorted(test4)))
    else:
        test_output.append('passed')

    return test_output

test1_messages = [["Sale today!","2837273"], 
 ["Unique offer!","3873827"], 
 ["Only today and only for you!","2837273"], 
 ["Sale today!","2837273"], 
 ["Unique offer!","3873827"]]

test1_spamSignals = ['sale', 'discount', 'offer']

test6_messages = [["Jkl ABA ty","111"], 
 ["Jkl aba TY","222"], 
 ["Jkl abA Ty","111"], 
 ["jkl Aba tY","111"], 
 ["JKl ABA ty","222"], 
 ["Jkl aba tY","222"], 
 ["Jkl abA Ty","111"], 
 ["jkl Aba tY klk TY","111"], 
 ["Jkl aBa tY","222"], 
 ["Jkl aBA Ty","111"], 
 ["Jkl aBA TY","111"]]

test6_spamSignals = ['ty', 'jk', 'ab']

print(spamDetection(test1_messages, test1_spamSignals))
print(spamDetection(test6_messages, test6_spamSignals))