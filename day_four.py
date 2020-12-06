import re

passports = []

with open('project_files/day4-puzzle1.txt', 'r') as f:
    current_passport = "  "
    while True:
        line = f.readline()
        if line.isspace():
            if not current_passport.isspace():
                passports.append(current_passport + "  ")
                current_passport = "  "
            continue
        if not line:
            break
        current_passport = current_passport + "  " + line.strip()

    if not current_passport.isspace():
        passports.append(current_passport + "  ")

# count_valid_passports = 0
# for passport in passports:
#     matches = []
#     matches.append(len(re.findall("byr:", passport)))
#     matches.append(len(re.findall("iyr:", passport)))
#     matches.append(len(re.findall("eyr:", passport)))
#     matches.append(len(re.findall("hgt:", passport)))
#     matches.append(len(re.findall("hcl:", passport)))
#     matches.append(len(re.findall("ecl:", passport)))
#     matches.append(len(re.findall("pid:", passport)))
#     # matches.append(len(re.findall("\scid:\S+\s", passport)))
    
#     if max(matches) == 1 and sum(matches) == 7:
#         count_valid_passports += 1

count_valid_passports = 0
for passport in passports:
    matches = []

    matches.append(len(re.findall("hcl:#[0-9a-f]{6} ", passport)))
    matches.append(len(re.findall("ecl:(amb|blu|brn|gry|grn|hzl|oth) ", passport)))
    matches.append(len(re.findall("pid:\d{9} ", passport)))

    match = re.findall("byr:\d{4} ", passport)
    if len(match) == 0:
        matches.append(0)
    else:
        year = int(match[0].strip().split(":")[1])
        matches.append(year >= 1920 and year <= 2002)

    match = re.findall("iyr:\d{4} ", passport)
    if len(match) == 0:
        matches.append(0)
    else:
        year = int(match[0].strip().split(":")[1])
        matches.append(year >= 2010 and year <= 2020)

    match = re.findall("eyr:\d{4} ", passport)
    if len(match) == 0:
        matches.append(0)
    else:
        year = int(match[0].strip().split(":")[1])
        matches.append(year >= 2020 and year <= 2030)

    match = re.findall("(hgt:\d+(?:in|cm))", passport)
    if len(match) == 0:
        matches.append(0)
    else:
        value = int(re.findall("\d+", match[0])[0])
        if "in" in match[0] and value >= 59 and value <= 76:
            matches.append(1)
        elif "cm" in match[0] and value >= 150 and value <= 193:
            matches.append(1)
        else:
            matches.append(0)
    if max(matches) == 1 and sum(matches) == 7:
        count_valid_passports += 1

print(count_valid_passports)
    