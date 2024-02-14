import dlt

def people_1():
   for i in range(1, 6):
     yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

# define the connection to load to.
# We now use duckdb, but you can switch to Bigquery later
pipeline = dlt.pipeline(pipeline_name="workshop_hw",
						destination='duckdb',
						dataset_name='people_data')


# for person in people_1():
#   person_list = []
#   person_list.append(person)
   # run the pipeline with default settings, and capture the outcome
  # info = pipeline.run(person_list,
  #                   table_name="users",
  #                   write_disposition="append")

# to find sum of age of all users:
# select sum(age) from people_data.users;result: 140

# show the outcome
# print(info)
def people_2():
   for i in range(3, 9):
     yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

for person in people_2():
  person_list = []
  person_list.append(person)
  info = pipeline.run(person_list,
                    table_name="users",
                    write_disposition="append")

print(info)

# checking sum age now:
# select sum(age) from people_data.users; result: 353
