from pyspark import SparkConf, SparkContext
from operator import add
import os
import time

start = time.time()
os.environ['PYSPARK_PYTHON'] = 'C:/Users/JackBar/AppData/Local/Programs/Python/Python311/python.exe'
os.environ['PYSPARK_DRIVER_PYTHON'] = 'C:/Users/JackBar/AppData/Local/Programs/Python/Python311/python.exe'


conf = SparkConf().setAppName("PasswordLengths").set("spark.executor.memory", "4g")
sc = SparkContext(conf=conf)

#Read in file
rdd = sc.textFile("C:/BigData/rockyou.txt")

#Map each password to a number/key e.g 11, 1) 
rdd_with_count = rdd.map(lambda password: (len(password), 1))

#Start adding the keys together and sort them in order
rdd_sorted = rdd_with_count.reduceByKey(add).sortBy(lambda x: x[0], ascending=True).collect()

#Print out most frequent password
for val in rdd_sorted:
    print(f"Length: {val[0]}, Frequency: {val[1]}\n")


#Stop the SparkContext
sc.stop()

end = time.time()

print(end - start)