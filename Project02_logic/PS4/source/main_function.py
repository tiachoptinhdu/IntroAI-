from clause import negative, Clause
class Main_Function:
    @staticmethod
    def PL_Resolution(clauses, filename):
        with open(filename, 'w') as f:
            result = False
            while True: 
                new = []
                #Hợp giải từng mệnh đề Ci, Cj 
                for i in range(len(clauses)):
                    for j in range(i+1, len(clauses)): 
                        Ci = clauses[i]
                        Cj = clauses[j]
                        resolvents = Clause.PL_Resolve(Ci, Cj)
                        if type(resolvents) is Clause:
                            if resolvents.check_clause() and resolvents not in clauses and resolvents not in new:
                                new.append(resolvents)
                # Kiểm tra điều kiện của new mới hợp giải xong
                f.write(str(len(new))+'\n')
                for clause in new:
                    f.write(str(clause)+"\n")
                if new == []:
                    result = False 
                    break  
                else:
                    clauses.extend(new) 
                if Clause([]) in new:
                    result = True
                    break 
            if result == False:
                f.write("NO")
            else: 
                f.write("Yes")
    @staticmethod
    def Read_File(filename):
        with open(filename, 'r') as f:
            clauses = []
            alpha = f.readline().splitlines()[0].replace(' ', '').split("OR")
            NUM_KB = int(f.readline())
            for line in f:
                clause = Clause(line.splitlines()[0].replace(' ', '').split("OR"))
                clauses.append(clause)
            for item in alpha: 
                clauses.append(Clause([negative(item)]))
            return clauses