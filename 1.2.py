def isPerm(a,b): #O(nlogn)
    if len(a) != len(b): return False
    a = sorted(a)
    b = sorted(b)
    return a == b

def isPermVector(a,b): # O(n)
    vec = [0]*128
    for i in a:
        vec[ord(i)] += 1

    for i in b:
        vec[ord(i)] -= 1
        if vec[ord(i)] < 0: return False

    return True

if __name__ == "__main__":
    a = input()
    b = input()
    print(isPerm(a,b))
    print(isPermVector(a,b))