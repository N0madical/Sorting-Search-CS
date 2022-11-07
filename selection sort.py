ogarr = [43,66,10,0,2,5,9]

def selectionsort(ogarr):
    arr = ogarr
    ogarr = str(ogarr)

    print("")
    print("Sorting the array: " + str(ogarr) + " in ascending order using selection sort...")
    print("")

    print(arr)
    for i in range (0, len(arr)):
        print (str(i) + " - " + str(arr))
        for j in range (1, (len(arr) - (i))):
            if (arr[i + j]) < arr[i]:
                temp = arr[i]
                arr[i] = arr[i + j]
                arr[i + j] = temp
            print("- " + str(arr) + ", " + str(j + i))

    print("")
    print("Sorted array: " + str(arr))