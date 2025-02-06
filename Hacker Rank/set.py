def average(array):
    # your code goes here
    arr1 = set(array)
    return sum(arr1) / len(arr1)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)