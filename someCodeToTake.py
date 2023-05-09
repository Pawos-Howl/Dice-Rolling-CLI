import random
dice = "5d20 +20 *5"
parts_s1 = [
  
]
parts_s2 = [
  
]
parts_s3 = [
  
]
parts_s4 = [
  
]
parts_s5 = [
  
]
parts_s6 = [
  
]
roll = [
  
]
add = 0
mult = 1
total = 0
new_dice = dice.replace(" ", "")
if "+" not in new_dice:
  new_dice = new_dice + "+0"
if "-" not in new_dice:
  new_dice = new_dice + "-0"
if "*" not in new_dice:
  new_dice = new_dice + "*1"
if "/" not in new_dice:
  new_dice = new_dice + "/1"
for part in new_dice.split("d"):
  parts_s1.append(part)
for part_num in range(len(parts_s1)):
  for part in parts_s1[part_num].split("+"):
    parts_s2.append(part)
for part_num in range(len(parts_s2)):
  for part in parts_s2[part_num].split("-"):
    parts_s3.append(part)
for part_num in range(len(parts_s3)):
  for part in parts_s3[part_num].split("*"):
    parts_s4.append(part)
for part_num in range(len(parts_s4)):
  for part in parts_s4[part_num].split("/"):
    parts_s5.append(part)
for part in parts_s5:
  parts_s6.append(int(part))
roll.append(parts_s6[0])
roll.append(parts_s6[1])
add += parts_s6[2]
add -= parts_s6[3]
mult = mult * parts_s6[4]
mult = mult / parts_s6[5]
for die in range(roll[0]):
  total += random.randint(1, roll[1])
total += add
total = total * mult
print(int(total))