# ----------------------------------
# Task :1
#
# 1. write every datatypes and print its value with what type it is
# 2. using given list, Loop  it through using a for loop
#    if zero or negative values present, print Skipped invalid value <value> and continue loop
#    Keep a running total and use break to stop as soon as the total goes above 30000
#    to print Target reached or Target not reached after the loop
# ----------------------------------

# 1. Data types and print value with data type.
number= 10
floatingNumber=20.5
name = "AJAY S"
listex=["apple","banana","mango"]
dictex={"name":"AJAY S","rnumber":"25","location":"chennai"}
setex={"AJAY","AJITH","AGAN"}
tupleex=("orange","kiwi","cherry")

print(number,type(number).__name__)
print(floatingNumber,type(floatingNumber).__name__)
print(name,type(name).__name__)
print(listex,type(listex).__name__)
print(dictex,type(dictex).__name__)
print(setex,type(setex).__name__)
print(tupleex,type(tupleex).__name__)


#2. sales list
sales=[12000,0,15000,-200,9800]

total=0
target="Target not Reached"
for num in sales:
    
    if(num<=0):
        print(f"Skipped invalid value:{num}")
        continue    
    print(num)
    total+=num 

    if(total>=30000):
        target=f"Target reached. Stopped at {total}"
        break

print(target)    