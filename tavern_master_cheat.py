import json

save_file_path = "/Users/brad/Library/Application Support/com.UntitledStudio.TavernMaster/CustomSave/s_3.json"

with open(save_file_path, "r") as f:
    data = json.load(f)

# Money
print(f"[!] Money: {data['TavernModelBase']['money']}")
# data["TavernModelBase"]["money"] = 9999999

# Bed prcies 1004
print(f"[!] N of beds: {len(data['TavernModelBase']['BedPrices'])}")

for i, bed in enumerate(data['TavernModelBase']['BedPrices']):
    data["TavernModelBase"]["BedPrices"][i]["Price"] = 1004

# Staff
staff_infos = data["StaffModelBase"]["StaffInfos"]

print(f"[!] N of staff: {len(staff_infos)}")

# Salary 1
for i, staff_info in enumerate(staff_infos):
    data["StaffModelBase"]["StaffInfos"][i]["Mood"] = 100
    data["StaffModelBase"]["StaffInfos"][i]["Salary"] = 1
    data["StaffModelBase"]["StaffInfos"][i]["SalaryAtStartOfDay"] = 1
    data["StaffModelBase"]["StaffInfos"][i]["LastDayNumberWhenSalaryWasChanged"] = 99999

with open(save_file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
