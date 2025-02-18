import sys 

def remove_odds(*args):
    arg_list = list(sys.argv[1:])
    
    arg_list = [int(i) for i in arg_list if int(i) % 2 == 0]
    print(arg_list)
    return None

if __name__ == '__main__':
    remove_odds()