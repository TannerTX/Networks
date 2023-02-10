import statistics

def average_and_stddev(numbers):
    average = sum(numbers) / len(numbers)
    stddev = statistics.stdev(numbers)
    
    print("Average: {:.3f}".format(average))
    print("Standard deviation: {:.4f}".format(stddev))


# average_and_stddev([0.189, 0.153, 0.133, 0.228, 0.143, 0.142, 0.154, 0.147, 0.146, 0.164])

ip_times_total = {}
curr_addy = ""
std_dev = []


with open("pings.txt", 'r') as f:
    for line in f.readlines():
        line = line.split(" ")
        
        if line[0] == "PING":
            curr_addy = line[1]
            ip_times_total[curr_addy] = 0

        for ele in line:
            if "time=" in ele:
                std_dev.append({curr_addy: float(ele.split("=")[1])})
                ip_times_total[curr_addy] += float(ele.split("=")[1])



keys = set()
for item in std_dev:
    keys.update(item.keys())

for key in keys:
    values = [item[key] for item in std_dev if key in item]
    average_and_stddev(values)


# # curr_ip = ""
# # TCP_UDP = []
# # with open("iperf.txt", 'r') as fin:
# #     for line in fin.readlines():
# #         line_content = line.split(" ")
# #         if "connecting" in line_content:
# #             if line_content[4] == "TCP":
# #                 TCP_UDP.append({line_content[4]: "YES"})
# #             elif line_content[4] == "UDP":
# #                 TCP_UDP.append({line_content[4]: "YES"})
# #             curr_ip = line_content[3][:-1]
# #             print(curr_ip)

# # print(TCP_UDP)
