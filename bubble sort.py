ogarr = [43,66,10,0,2,5,9]

def bubblesort(ogarr):
    arr = ogarr
    ogarr = str(ogarr)

    print("")
    print("Sorting the array: " + str(ogarr) + " in ascending order using bubble sort...")
    print("")

    for i in range (1, len(arr) + 1):
        print(str(i) + " - " + str(arr))
        for j in range (0, (len(arr) - i)):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                print(str(arr) + ", " + str(j))

    print("")
    print("Sorted array: " + str(arr))