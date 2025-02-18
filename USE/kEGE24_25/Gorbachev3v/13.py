network_ip = (105 << 24) + (241 << 16) + (48 << 8) + 0

count_not_multiple_of_6 = 0

for i in range(2048):
    ip = network_ip + i
    bin_ip = format(ip, '032b')
    zero_count = bin_ip.count('0')
    
    if zero_count % 6 != 0:
        count_not_multiple_of_6 += 1

print(count_not_multiple_of_6)
