
    
    

            



with open('input.txt', 'r') as f:
    clauses = []
    alpha = f.readline().splitlines()[0].replace(' ', '').split("OR")
    NUM_KB = int(f.readline())
    for line in f:
        clause = Clause(line.splitlines()[0].replace(' ', '').split("OR"))
        clauses.append(clause)
for item in alpha: 
    clauses.append(Clause([negative(item)]))
Main_Function.PL_Resolution(clauses)





    

        
 






