# This code run when selected Pypy3
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))

# This another code don't run but its correct too

'''
    n = int(input())
    numbers_tuple = tuple(map(int, input().split()))
    print(hash(numbers_tuple))
'''