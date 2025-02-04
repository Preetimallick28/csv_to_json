# how to convert csv file to json

# step 1 - import two modules i.e csv and json

import csv
import json

# step 2 - now we will load the csv file through open() method. 

csv_file = open("C:/Users/preet/python_developer_internship_01-02-2025/task_1_csv_to_json_convert/Zomato_data .csv",'r')


# step 3 - next we will read the content of the csv file 

# using csv.reader() and passing the actual csv file

csv_content = csv.reader(csv_file)

# step 4 - Now we will read the number of fields with the help of next().

fields_names = next(csv_content)

# step 5 - let us see what content get stored in field_names , so let us print the variable once 

print (fields_names)

# step 6 - Now we will initializing the data which will be an empty array.

data = []

# step 7 - Now we will iterate a loop in which we are going to append the content of the csv file into the empty array.

for row in csv_content:
	data.append(dict(zip(fields_names,row)))

# step 8 - Now simply we would print the array to see what data got stored in the array

print(data)

# step 9 - After this we need to convert this data to a basically a json .
# For this I am going to use json.dumps() and inside the method I am going to pass data array.

json_data = json.dumps(data,indent=4)

# step 10 - now I will write the code to open this file in the site write mode
json_file = open("data.json",'w')
json_file.write(json_data)

# step 11 - now will close the csv file and json file 
csv_file.close()
json_file.close()


