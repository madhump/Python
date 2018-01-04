import statistics
import numbers
import datetime
from statistics import mean

# finding the exponential values
print (10**2)

print(100*1.10**7)

savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")


list1 = [100,300,120]
list2 = [10,220,580]
print("2nd value  list1 is:" + str(list1[1]) + " and 2nd value in list2 is:" + str(list2[1]))

list3 = list1 + list2
print ("list3 is:" + str(list3))
sortedarray = sorted(list3)
print("Sorted list is:" + str(sortedarray))
print("Minm number in the array is " + str(min(sortedarray)))
print("Maxm number in the array is "+ str(max(sortedarray)))
#print("Average of the array is " + str(round(sum(sortedarray)/len(sortedarray))))
print("Average of the array is {0}".format(str(round(sum(sortedarray) / len(sortedarray)))))
print("Mean Average is " + str(round(mean(sortedarray))))


oTime = datetime.datetime.now()
finalTime =oTime.isoformat()
stime = oTime.today()
print(stime)