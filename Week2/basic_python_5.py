import sys

# print(sys.argv)
def avg_grade(*args):    
    arg_list = list(sys.argv[1:])

    n = len(arg_list)
    
    summ = 0
    for i in range(n):
        summ += int(arg_list[i])

    avg = float(summ / n)

    if avg >= 5:
        return print(f"{avg} Pass")
    else:
        return print(f"{avg} Fail")
    
if __name__ == "__main__":
    main()

