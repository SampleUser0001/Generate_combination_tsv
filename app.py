import sys
import itertools

def file_load(file_path):
    return_list = []
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            return_list.append(line)
    return return_list

def print_list(values, indexes):
    l = []
    for i in range(len(values)):
        l.append(values[i][indexes[i]])
    print("\t".join(l))

def is_finish(values, indexes):
    for i in range(len(values)):
        if indexes[i] < len(values[i]) - 1:
            return False
    return True

def main():
    
    pattern_list = []
    index_list = []
    sys.argv.pop(0)
    
    for file in sys.argv:
        pattern_list.append(file_load(file))
        index_list.append(0)

    print_list(pattern_list, index_list)
    while not is_finish(pattern_list, index_list):
        for i in range(len(index_list)-1,-1,-1):
            if index_list[i] < len(pattern_list[i]) - 1:
                index_list[i] += 1
                break
            else:
                index_list[i] = 0
        print_list(pattern_list, index_list)

if __name__ == "__main__":
    main()