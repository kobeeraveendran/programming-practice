import operator

def campusCup(emails):
    domain_count = {}
    space_count = {}
    
    for i in range(len(emails)):
        email_parse = emails[i].split('@')
        domain = email_parse[1]
        
        if domain in domain_count:
            domain_count[domain] += 1
        else:
            domain_count[domain] = 1
            
        if domain_count[domain] * 20 < 100:
            space_count[domain] = 0
        elif domain_count[domain] * 20 == 100:
            space_count[domain] = 3
        elif domain_count[domain] * 20 == 200:
            space_count[domain] = 11
        elif domain_count[domain] * 20 == 300:
            space_count[domain] = 26
        elif domain_count[domain] * 20 == 500:
            space_count[domain] = 51

    # sort by space from highest to lowest
    school_standings = sorted(list(space_count.items()), key = lambda x: x[0])
    print(school_standings)
    print('----------------------------------')
    school_standings.sort(key = lambda x: x[1], reverse = True)
    print(school_standings)
    print('----------------------------------')
    #school_standings = sorted(space_count, key = operator.itemgetter(1, 0), reverse = True)
    school_standings = [x[0] for x in school_standings]
            
    return school_standings
        
test3 = ["b@harvard.edu", 
 "c@harvard.edu", 
 "d@harvard.edu", 
 "e@harvard.edu", 
 "f@harvard.edu", 
 "a@student.spbu.ru", 
 "b@student.spbu.ru", 
 "c@student.spbu.ru", 
 "d@student.spbu.ru", 
 "e@student.spbu.ru", 
 "f@student.spbu.ru", 
 "g@student.spbu.ru"]
print(campusCup(['a@rain.ifmo.ru', 'b@rain.ifmo.ru', 'c@rain.ifmo.ru', 'd@rain.ifmo.ru', 'e@rain.ifmo.ru', 'noname@mit.edu']))
print(campusCup(['b@harvard.edu', 'c@harvard.edu', 'a@student.spbu.ru', 'b@student.spbu.ru']))
print(campusCup(test3))