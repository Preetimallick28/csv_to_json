import csv
import json
csv_file = open("C:/Users/preet/python_developer_internship_01-02-2025/task_1_csv_to_json_convert/Zomato_data .csv",'r')
csv_content = csv.reader(csv_file)
fields_names = next(csv_content)
print (fields_names)
data = []
for row in csv_content:
	data.append(dict(zip(fields_names,row)))
print(data)
json_data = json.dumps(data,indent=4)
json_file = open("data.json",'w')
json_file.write(json_data)
csv_file.close()
json_file.close()


