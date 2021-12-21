import copy
def negative(literal:str):
    if literal[0] == '-':
        return literal[1]
    else:
        return '-'+literal[0]
# clause là một câu  A OR B OR -C OR D
class Clause: # clause have attribute clause is list of literal
    def __init__(self, clause:list): #clause is list of string 
        self.clause = clause
        self.normalize()
    def normalize(self): # Chuẩn hóa clause: bao gồm các biến phải unique và sắp xếp theo bảng chữ cái
        self.clause = list(set(self.clause))
        def T(x):
            if x[0] == '-':
                return x[1]
            else: 
                return x[0]
        self.clause.sort(key = lambda x: T(x))
    def __str__(self):
        if self.clause == []:
            return '{}'
        else:
            return ' OR '.join(self.clause)
    def check_clause(self):
        for literal in self.clause: 
            if negative(literal) in self.clause: 
                return False 
        return True
    def __eq__(self, obj):
        return set(obj.clause) == set(self.clause)

    @staticmethod
    def PL_Resolve(Ci, Cj):
        Ci_copy = copy.deepcopy(Ci.clause)
        Cj_copy = copy.deepcopy(Cj.clause)
        for i in range(len(Ci_copy)):
            for j in range(len(Cj_copy)):
                if Ci_copy[i] == negative(Cj_copy[j]):
                    Ci_copy.pop(i)
                    Cj_copy.pop(j)
                    return Clause(Ci_copy+Cj_copy)
        return False    