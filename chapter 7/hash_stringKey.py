M = 13

def hashFn(key):
    sum = 0
    for c in key:
        sum = sum + ord(c)

    return sum, sum % M


#-------------------------------------------------------------------


def main():
    keyStr = ['do', 'for', 'if', 'case', 'eles', 'return', 'function']
    sumTrans = []
    key = []
    noKey = len(keyStr)

    for i in keyStr:
        tempSum, tempKey = hashFn(i)
        sumTrans.append(tempSum)
        key.append(tempKey)


    for i in range(noKey):
        print(keyStr[i], '-', sumTrans[i], '-', key[i])


#-------------------------------------------------------------------

        
if __name__ == '__main__':
    main()
