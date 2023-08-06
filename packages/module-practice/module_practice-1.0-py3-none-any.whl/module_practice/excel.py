from csv import writer, reader
# newline argument disables extra line created by python
with open("data.csv", "w", newline="") as data:
    excel_file = writer(data)
    excel_file.writerow(["name", "post", "destination"])
    excel_file.writerow(["Giri", "software", "UK"])


with open("data.csv") as data:
    excel_file = reader(data)
    for data in excel_file:
        print(data)
