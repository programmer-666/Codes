total = 0;ip0 = 0;ip1 = 0;ip2 = 0;ip3 = 0
with open("ips.txt", "w") as f:
	for i in range(1,256):
		total+=1
		ip0 = i
		f.write(f"{ip3}.{ip2}.{ip1}.{ip0}\n")
		for a in range(1,129):
			total+=1
			ip1 = a
			f.write(f"{ip3}.{ip2}.{ip1}.{ip0}\n")
			for b in range(1,65):
				total+=1
				ip2 = b
				f.write(f"{ip3}.{ip2}.{ip1}.{ip0}\n")
				for c in range(1,33):
					total+=1
					ip3 = c
					f.write(f"{ip3}.{ip2}.{ip1}.{ip0}\n")
print(f"ip.max: {ip3}.{ip2}.{ip1}.{ip0}", total, "ip generated")