def print_operation_table(operation, num_rows=6, num_columns=6):
    initial_lst = [ i for i in range(num_rows + 1) if i != 0]
    for i in initial_lst:
        print("\n")
        print([(operation(i, j)) for j in range(num_columns+1) if j !=0])
            

print_operation_table(lambda x,y : x*y)
