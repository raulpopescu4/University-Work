def insert_sort(data):
    for i in range(1,len(data)):
        index = i-1
        elem = data[i]

        while index >= 0 and elem < data[index]:
            data[index+1] = data[index]
            index -= 1
