from pyspark import SparkConf, SparkContext
from operator import add
import os
import re
import time

start = time.time()


os.environ['PYSPARK_PYTHON'] = 'C:/Users/danbw/AppData/Local/Programs/Python/Python311/python.exe'
os.environ['PYSPARK_DRIVER_PYTHON'] = 'C:/Users/danbw/AppData/Local/Programs/Python/Python311/python.exe'


conf = SparkConf().setAppName("PasswordFrequency").set("spark.executor.memory", "4g")
sc = SparkContext(conf=conf)

#Read in file
rdd = sc.textFile("C:/BigData/output.txt")
rdd_with_count = rdd.map(lambda password: (password, 1))

#Start adding the keys together and sort them in order
rdd_sorted = rdd_with_count.reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1], ascending=False)

#Take the first password in the sorted list
most_frequent_password = rdd_sorted.take(1)

#Print out most frequent password
print(f"Password: {most_frequent_password[0][0]}, Frequency: {most_frequent_password[0][1]}")
#print(f"Password: {most_frequent_password[1][0]}, Frequency: {most_frequent_password[1][1]}")
#print(f"Password: {most_frequent_password[2][0]}, Frequency: {most_frequent_password[2][1]}")


#Stop the SparkContext
sc.stop()

end = time.time()

print(end - start)