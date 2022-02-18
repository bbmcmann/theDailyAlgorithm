import sys

def find_min_transform(in_str):
    # output min num ops needed to transform, or -1 if impossible
    return -1

if __name__ == '__main__':
    inpt_strs = []
    num_strings = int(sys.stdin.readline())

    for i in range(0, num_strings):
        temp = sys.stdin.readline()
        inpt_strs.append(temp[:len(temp)-1])

    print(inpt_strs)
