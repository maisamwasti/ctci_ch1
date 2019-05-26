

def isUnique(s): #using set
    setOfChars = set()
    for i in s:
        if i in setOfChars:
            return False
        setOfChars.add(i)
    return True

def isUniqueBrute(s): #O(N^2)
    for i in range(len(s)): #this is an open interval too
        for j in range(i+1,len(s)): #this is an open interval too
            #print(i,j)
            if s[i] == s[j]:
                return False
    return True

def isUniqueSort(s): #O(N) + O(nlogn) + O(N) = O(NlogN)
    numList = [ord(i) for i in s]
    numList.sort()
    for i in range(len(numList)-1):
        if numList[i] ==  numList[i+1]:
            return False
    return True

if __name__ == "__main__":
    s = input()
    print(isUnique(s))
    print(isUniqueBrute(s))
    print(isUniqueSort(s))
    print("A MINOR CHANGE TO TEST PULL REQUESTS")
