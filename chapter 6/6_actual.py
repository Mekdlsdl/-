# 6.1

word = input()

total = len(word)
stan = total // 2
count = 0
#print(stan, word[stan])

for i in range(total-1):
    if word[i] == word[-1-i]:
        #print(word[i], word[-1-i])
        count += 1
    #print(count)

if count == total-1 :
    print("이 문자열은 회문입니다.")
    #print(count,stan)

else:
    print("이 문자열은 회문이 아닙니다.")
