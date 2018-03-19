
def GetChecksum(Pin):
	
	pin = Pin * 10
	acc = 0
	
	acc = acc + 3 * ((pin//10000000) % 10)
	acc = acc + 1 * ((pin//1000000) % 10)
	acc = acc + 3 * ((pin//100000) % 10)
	acc = acc + 1 * ((pin//10000) % 10)
	acc = acc + 3 * ((pin//1000) % 10)
	acc = acc + 1 * ((pin//100) % 10)
	acc = acc + 3 * ((pin//10) % 10)
	digito = acc % 10
	checksum = (10 - digito) % 10
	
	return pin + checksum

#      PIN     CHECKSUM
# 2012822          7
# 0938604          4
# 1234567          0

Checksum = GetChecksum(938604)

print('\n\n PIN:', Checksum)
