from main_function import Main_Function


clauses = Main_Function.Read_File('input.txt')
Main_Function.PL_Resolution(clauses, 'output.txt')
