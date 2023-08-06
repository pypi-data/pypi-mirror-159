import re

#pattern = r"= (\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+) ms"
pattern_all = r"Minimum = (\d+\S+), Maximum = (\d+\S+), Average = (\d+\S+)"

output = "Minimum = 16ms, Maximum = 20ms, Average = 18ms"

avg = re.findall(pattern_all,output)[0][0]
#print(avg)


rtt = ["16", "17", "18"]
rtt_i = [0, 2, 1]
rtt = [rtt[i]+"ms" for i in rtt_i]
print(rtt)