if __name__ == '__main__':
    my_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append([name, score])
    second_highest = sorted(set([score for name, score in my_list]))[1]
    print('\n'.join(sorted([name for name, score in my_list if score == second_highest])))