# ----------------------------------
# Task 2
#
# 1. Apply discount with fixed and variable discount for given list [prices]
# 2. Create total(*args) that returns the sum of any number of values and describe(**kwargs) that prints every key and value
# 3. Using the prices list, build a list comprehension of prices above 1000
# 4. using map() with lambda to add 18% GST and round 2 decimals
# 5. new list that holds number below 1000 from list prices using filter() with lambda
# ----------------------------------

prices = [500, 1200, 800, 2500, 300]


# 1. apply discount with fixed and variable discount
def apply_discounts(price,discount=10):
   return price-(price*(discount/100))

for num in prices:
    print(f"apply_discount({num})->",apply_discounts(num))

for num in prices:    
    discountpercent=25
    print(f"apply_discount({num},{discountpercent})->",apply_discounts(num,discountpercent))

#2. *args and **kwargs

def total(*args):    
    return sum(args)

print(total(10,20,30))

def describe(**kwargs):
    for key,value in kwargs.items():
        print(f"{key},{value}")
describe(name="AJAY S", rnumber="25", experience=2)

#3. new list that holds number above 1000 from list prices

new_abovelist=[]
for number in prices:
    if(number>1000):
        new_abovelist.append(number)
print("Above 1000: ",new_abovelist)    

#4. using map() with lambda to add 18% GST and round 2 decimals

gst= list(map(lambda num:num*1.18,prices))
print("With GST: ",gst)

#5. new list that holds number below 1000 from list prices using filter() with lambda
new_belowlist=list(filter(lambda num:num<1000,prices))  
print("Below 1000: ",new_belowlist)