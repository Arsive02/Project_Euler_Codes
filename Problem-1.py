#Sum of multiples of 3 and 5 below 1000

List = [i for i in range(1000) if i%3==0 or i%5==0]
print(sum(List))