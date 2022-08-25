def pascal(n):
    arr = [1]
    temp = []
    print("Pascal's triangle of ", n, 'rows')
    for i in range(n):
        print("rows", i+1, end=" : ")
        for j in range(len(arr)):
            print(arr[j], end=' ')
        print()
        temp.append(1)
        for j in range(len(arr)-1):
            temp.append(arr[j] + arr[j + 1])
        temp.append(1)
        arr = temp
        temp = []

n = int(input("Enter the number for the pascal triangle: "))
pascal(n)