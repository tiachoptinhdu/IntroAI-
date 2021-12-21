import copy


def negative(literal):
    if literal[0] == '-':
        return literal[1]
    else:
        return '-'+literal[0]


def normalize_clause(Ci):
    Ci = list(set(Ci)) # Remove duplicate 
    def T(x):
        if x[0] == '-':
            return x[1]
        else: 
            return x[0]
    Ci.sort(key = lambda x: T(x)) # Sort variable 
    return Ci
with open('input.txt') as f:
    alpha = f.readline().splitlines()[0].replace(' ', '').split("OR")
    NUM_KB = int(f.readline())
    clauses = []
    for line in f:
        clause = line.splitlines()[0].replace(' ', '').split("OR")
        clauses.append(normalize_clause(clause))

clauses.append(alpha)
for item in alpha:
    clauses.append([negative(item)]) 

    
print(clauses)
# Hàm Resolve hai clause trả về một clause sau khi result nếu chúng resolve được và trả về False nếu không result được
def PL_Resolve(Ci, Cj):
    Ci_copy = copy.deepcopy(Ci)
    Cj_copy = copy.deepcopy(Cj)
    for i in range(len(Ci_copy)):
        for j in range(len(Cj_copy)):
            if Ci_copy[i] == negative(Cj_copy[j]):
                Ci_copy.pop(i)
                Cj_copy.pop(j)
                return normalize_clause(Ci_copy+Cj_copy)                
    return False

print(PL_Resolve(['A', 'D'], ['-A', 'C']))
# Hàm check clause có vô nghĩa hay không: True == có nghĩa; False == Vô nghĩa 
def check_clause(Ci):
    for literal in Ci: 
        if negative(literal) in Ci: 
            return False 
    return True 

def sort_clauses(clauses):
    clauses.sort(key = lambda x: len(x))
    return clauses
def Write_Clauses(clauses):
    print(len(clauses))
    for clause in clauses:
        if clause == []:
            print('{ }')
        else: 
            print(' OR '.join(clause))
def PL_Resolution(clauses):
    while True: 
        new = []
        #Hợp giải từng mệnh đề Ci, Cj 
        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)): 
                Ci = clauses[i]
                Cj = clauses[j]
                resolvents = PL_Resolve(Ci, Cj)
                if type(resolvents) is list:
                    if check_clause(resolvents) and resolvents not in clauses and resolvents not in new:
                        new.append(resolvents)
        Write_Clauses(new)
        # Kiểm tra điều kiện của new mới hợp giải xong
        if new == []:
            return False 
        else:
            clauses.extend(new) 
        if [] in new:
            return True
print(PL_Resolution(clauses))




#print(clauses)

#print(PL_Resolve(clauses[2], clauses[1]))




            






