ogarr = [43,66,10,0,2,5,9]
arr = ogarr
ogarr = str(ogarr)

print(arr)
for i in range (0, 6):
    print (str(i) + " - " + str(arr))
    for j in range (1, (6 - (i))):
        if (arr[i + j]) < arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        print("- " + str(arr) + ", " + str(j + i))

print("")
print("Sorting the array: " + str(ogarr) + " in ascending order...")
print("Sorted array: " + str(arr))