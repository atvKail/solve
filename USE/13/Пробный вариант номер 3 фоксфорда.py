subnet_mask = "255.255.255.192"
total_bits = 32

# Подсчёт количества единиц в маске
ones_count = sum(bin(int(octet)).count('1') for octet in subnet_mask.split('.'))
host_bits = total_bits - ones_count

# Количество адресов в сети
total_addresses = 2 ** host_bits

# Количество адресов, оканчивающихся на 1
addresses_ending_in_1 = 2 ** (host_bits - 1)

print(addresses_ending_in_1)
