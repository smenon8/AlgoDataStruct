# vector distance calculator:
def calc_dist_nearest_zero(vct):
	curr_zero = -1
	curr = 0
	dist = [float('inf')]*len(vct)
	while curr < len(vct):
		if vct[curr] == 0:
			curr_zero = curr
			dist[curr_zero] = 0
			curr = curr -1
			while abs(curr - curr_zero) < dist[curr] and curr >= 0:
				dist[curr] = abs(curr - curr_zero)
				curr -= 1
			curr = curr_zero + 1
		else:
			if curr_zero != -1:
				dist[curr] = abs(curr - curr_zero)
			curr += 1

	return dist

def check_isomorphic(str1, str2):
	d = {}

	for i in range(len(str1)):
		if str1[i] in d.keys():
			if d[str1[i]] != str2[i]:
				return False
		else:
			d[str1[i]] = str2[i]

	return True


def huffman_encoding(msg):
    # base case
    if len(msg) == 0:
        return
    prev = None
    enc_msg = []
    count = 1
    for chr in msg:
        if chr == prev:
            count += 1
        else:
            if prev != None:
                enc_msg += [prev, str(count)]
            prev = chr
            count = 1
    enc_msg += [chr, str(count)]
    return ''.join(enc_msg)


def long_non_rep_substr(str):
	dict = {str[0] : 0}
	max_till_now = 1

	for i in range(1,len(str)):
		if dict.get(str[i], None) == None:
			dict[str[i]] = i
			if len(dict.keys()) > max_till_now:
				max_till_now = len(dict.keys())
		else:
			dict = {str[i] : i}
	return max_till_now


def num_primes(n):
	if n < 2:
		return 0
	else:
		visit = [1]*(n+1)

		visit[0] = visit[1] = 0

		for i in range(2,n+1):
			for j in range(i, n+1):
				if i*j <= n:
					visit[i*j] = 0
		return sum(visit)


## Newpassword@yah00

def power_set(inp_set):
	result = [[]]

	for ele in inp_set:
		newSubSets = [subset + [ele] for subset in result]
		result.extend(newSubSets)

	return result 


def power_set2(inp_set, new_set):
	if inp_set == []:
		return [new_set]
	else:
		result = []
		for ele in power_set2(inp_set[1:],new_set + [inp_set[0]]):
			result.append(ele)

		for ele in power_set2(inp_set[1:], new_set):
			result.append(ele)

		return result

def power_set3(inp_set):
	pwr_set_size = 2 ** len(inp_set)
	pwr_set = [[]]

	for i in range(pwr_set_size):
		new_set = []
		for j in range(len(inp_set)):
			if i & 1 << j : # this is to check if the jth bit is set or not
				new_set.extend([inp_set[j]])

		pwr_set.append(new_set)
	
	return pwr_set

def zeros_to_end(arr):
	nz_ptr = 0

	for i in range(len(arr)):
		if arr[i] != 0: 
			arr[nz_ptr] = arr[i] # shift all the non-zero element to the front simply
			nz_ptr += 1

	for i in range(nz_ptr, len(arr)): # the nz_ptr is at the last non-zero number, now start filling zeros from there
		arr[i] = 0

	return arr


def find_missing_num(arr, N):
	xor1 = arr[0]
	for i in range(1, len(arr)):
		xor1 = xor1 ^ arr[i]

	xor2 = 1
	for i in range(2, N+1):
		xor2 = xor2 ^ i

	return xor1 ^ xor2


print(power_set([1,2,3]))
print(power_set2([1,2,3], []))
print(power_set3([1,2,3]))

print(zeros_to_end([1,3,0,8,12,0,4,7,0,0,0,0,9,12,14,15,0,0]))


print(find_missing_num([1,2,4,5,6],6))