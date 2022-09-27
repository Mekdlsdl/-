# 2.1

for i in range(1,10):
    print(6 * i)



# 2.2

i = 1

while True:
    if i < 10 :
        print(6 * i)

    i += 1



# 2.3

for i in range(9,0,-1):
    print(6 * i)



# 2.4

c = int(input())
f = 32 + 180 / 100 * c
print(f)



# 2.5

def c_to_f(c):
    f = 32 + 180 / 100 * c
    print(f)



# 2.6

a = [1, 2, 3, 4]

for i in range(len(a)-1, -1, -1):
    print(a[i], end = ' ')



# 2.7

a = [1, 2, 3, 4]
sum_a = 0

for temp in a:
    sum_a += temp
    
print(sum_a)



# 2.8

msg = "Data Structures in Python"
print(msg)
print(msg.upper())
print(msg.lower())


    
# 2.9

price = {'콩나물해장국':4500, '갈비탕':9000, '돈가스':8000}
price['팟타이']= 7000
print(price)



# 2.10

