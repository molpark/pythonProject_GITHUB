nums = [3,3]
lens=len(nums)
white=[]
target=6
i = 0
while i < lens-1:
    numa=nums[i]
    lista=nums[i+1:lens+1]
    print(lista)
    for ia in lista:
        # print(ia)
        if numa+ia ==target:
            d=nums.index(ia,i+1)   ##从i后面开始找
            white.append(i)
            #print(white)
            white.append(d)
            #print(white)
    i=i+1
print(white)



n=len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            listb= [i,j]
print(listb)