
import random

male =  ['A','B','C','D','E','F','G','H','I','J']
female = ['1','2','3','4','5','6','7','8','9','10']

def par(par, gender, pri1, pri2, pri3):
    parOpt = {
        "label" : par,
        "gender" : gender,
        "chosen": [pri1,pri2,pri3]
    }
    return parOpt

def femaleMatch( m, f, credit):
    if f['chosen'][0]==m['label']:
            credit = credit + 3
            print("Female 1st prior: "+f['chosen'][0]+"=="+m['label'])
            print('match:')
            return m['label']+f['label'], credit
        
    elif f['chosen'][1]==m['label']:
            credit = credit + 2
            print("Female 2nd prior: "+f['chosen'][1]+"=="+m['label'])
            print('match:')
            return m['label']+f['label'], credit
        
    elif f['chosen'][2]==m['label']:
            credit = credit + 1
            print("Female 3rd prior: "+f['chosen'][2]+"=="+m['label'])
            print('match:')
            return m['label']+f['label'], credit
    else:
        return "No", 0
    
def maleMatch(m, f):
    if m['chosen'][0]==f['label']: 
        credit = 3
        print("------------------------------------------------")
        print("Male 1st prior: "+m['chosen'][0]+"=="+f['label'])
        return femaleMatch(m, f, credit)
    
    elif m['chosen'][1]==f['label']: 
        credit = 2
        print("------------------------------------------------")
        print("Male 2nd prior: "+m['chosen'][1]+"=="+f['label'])
        return femaleMatch(m, f, credit)
    
    elif m['chosen'][2]==f['label']:
        credit = 1
        print("------------------------------------------------")
        print("Male 3rd prior: "+m['chosen'][2]+"=="+f['label'])
        return femaleMatch(m, f, credit)
    else:
        return "No",0
        
def matchMaking( m, f):
    result, credit = maleMatch(m, f)
    if result is not None:
        #print(result)
        if result != "No":
            result = result
            print(result)
    return result, str(credit)

def parMatching(m, f):
    result = ""
    results = []
    for i in m:
        for j in f:
            result, credit =  matchMaking(i,j)
            #print("parMatching:"+result)
            if result != 'No':
                print("parMatching: "+result+" : "+credit)
                tup = (result, credit)
                results.append(tup)
    return results

import collections

def parCompare(lpar):
    m_vars = []
    f_vars = []
    for i in range(len(lpar)):
        # using the unpack Method to split a string into char array in Python https://www.delftstack.com/howto/python/split-string-to-a-list-of-characters/
        m_var = [*lpar[i][0]][0]
        f_var = [*lpar[i][0]][1]
        m_vars.append(m_var)
        f_vars.append(f_var)
    
    # to find duplicate values in a list https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them
    print(m_vars)
    m_vars = [item for item, count in collections.Counter(m_vars).items() if count > 1]
    print(m_vars)
    print(f_vars)
    f_vars = [item for item, count in collections.Counter(f_vars).items() if count > 1]
    print(f_vars)
    
        
    
    # participant generator can be used but the chosen partner can't be matched.
def createPar():
    # we need unique random generator so each male has different options for the chosen womens 
    # solution: https://stackoverflow.com/questions/22842289/generate-n-unique-random-numbers-within-a-range
    m_result = []
    for i in male:
        cf = random.sample(range(1, 11), 3)
        pm = par(i, "male", cf[0], cf[1], cf[2])
        m_result.append(pm)
        print(pm)
    
    f_result = []
    for i in female:
        cf = random.sample(range(0, 10), 3)
        pm = par(i, "female", male[cf[0]], male[cf[1]], male[cf[2]])
        f_result.append(pm)
        print(pm)
    
    return m_result, f_result


def manualPar():
    m_result = [
        par('A','male','1','3','2'),
        par('B','male','1','3','2'),
        par('C','male','4','9','7'),
        # par('D','male','2','1','6'),
        # par('E','male','1','8','7'),
        # par('F','male','6','3','4'),
        # par('G','male','5','7','8'),
        # par('H','male','9','3','2'),
        # par('I','male','4','6','1'),
        # par('J','male','3','2','5')
    ]
    f_result = [
        par('1','female','A','J','E'),
        par('2','female','A','H','I'),
        par('3','female','A','C','B'),
        # par('4','female','B','C','F'),
        # par('5','female','B','E','D'),
        # par('6','female','D','H','J'),
        # par('7','female','I','J','F'),
        # par('8','female','C','F','H'),
        # par('9','female','A','B','H'),
        # par('10','female','E','J','H')
    ]
    return m_result, f_result
        
if __name__ == '__main__':
    #m = par('A','male','2','1','3')
    #f = par('1','female','F','B','A')
    # this algorithm failed
    # m_l, f_l = createPar()
    # match = parMatching(m_l, f_l)
    # crazy possibility, never try this code, most of the results are No match.
    # while match=="No":
    #     m_l, f_l = createPar()
    #     match = parMatching(m_l, f_l)
    # m_l, f_l = manualPar()
    # match = parMatching(m_l, f_l)
    # while match=="No":
    #     m_l, f_l = manualPar()
    #     match = parMatching(m_l, f_l)
    m_l, f_l = manualPar()
    match = parMatching(m_l,f_l)
    print(match)
    parCompare(match)
    
