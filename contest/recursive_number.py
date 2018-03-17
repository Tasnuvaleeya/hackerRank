def sum_digit(list_of_num):
    if len(list_of_num)==1:
        return list_of_num[0]
    else:
        sum_num = sum(list_of_num)
        return sum_digit([int(x) for x in str(sum_num)])

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [str(n), int(k)]
    num_string = [int(i) for i in str(n)]
    num_string = [int(i) for i in str(sum(num_string) * k)]
    result = sum_digit(num_string)
    print(result)
