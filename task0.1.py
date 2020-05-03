a,b = input('enter two numbers separated by comma : ').split(',')
a = int(a)
b = int(b)
product = (a*b)
if product>1000:
    print(f"the sum is : {sum((a,b))}")
else:
    print(f"the product is : {product}")