
def remove_duplicates_set(some_list):
    return list(set(some_list))

def remove_duplicates_for(some_list):
    without_duplicates = []
    for item in some_list:
        if item not in without_duplicates:
            without_duplicates.append(item)
    return without_duplicates

def run():
    some_list = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7]
    print(remove_duplicates_set(some_list))
    print(remove_duplicates_for(some_list))


if __name__ == '__main__':
    run()