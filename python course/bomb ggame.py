with open("test.txt","r") as f:
    nums = f.readlines()

    ss =[]
    for num in nums:
        ss.append(float(num.strip()))

    for i in range(len(ss)):
        ss[i] = ss[1]*ss[1]
f.close()
