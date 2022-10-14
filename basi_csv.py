import csv
import os
os.chdir(r"C:\Users\User\OneDrive\Desktop\filehandling\files\csv_files")

#reader()
with open("sample.csv") as file:
    reader_obj=csv.reader(file)
    for data in reader_obj:
        print(data)
#DictReader()
with open("sample.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        print(data)


# to write the data into excel sheet
"""
with open("sample.csv","w") as file:
    writer_obj = csv.writer(file)
    #writing in single row
    writer_obj.writerow(["emp","emp_id"])
    writer_obj.writerow(["prasanna",123])

    #multiple rows

    
    writer_obj.writerows([["sunil",456],["bhagya",789]])

fieldname = ["emp","emp_id"]
with open("sample.csv","w",newline="") as file:
    writer_obj = csv.DictWriter(file,["emp","emp_id"],skipinitialspace=True)
    writer_obj.writeheader()
    #single row
    writer_obj.writerow({"emp":" prasanna","emp_id":123})
    #multiple row
    writer_obj.writerows([{"emp":"sunil","emp_id":456},{"emp":"bhagya","emp_id":789}])



csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)
    
with open("sample.csv","r") as file:
    obj = csv.reader(file, dialect = 'myDialect')
    for data in obj:
        print(data)

"""










    

