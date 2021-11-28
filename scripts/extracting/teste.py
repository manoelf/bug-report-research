

def testArray(nArray): # TODO: Possui um erro aqui
    copy_array = nArray[:]
    for index in range(len(copy_array) -1, -1, -1):
        item = copy_array[index]
        if len(item.strip()) == 0:
            copy_array.pop(index)

    return copy_array

myArray = ['   ', '    r', 'dfasdfsf', 'sdfsdf']


print(testArray(myArray))