nums = list(map(int,input().split()))
print(nums)
vow = ['a','e','i','o']
cons = ['b','c','d','f','g']
prime = {2,3,5,7}
non_prime = {1,4,6,8,9}
hash_map = {}
res = ''
for i in nums:
  print(hash_map)
  if i not in hash_map:
    print('not hash')
    if i in prime:
      res+=vow[0]
      hash_map[i] = vow[0]
      vow.pop(0)
    else:
      res+=cons[0]
      hash_map[i] = cons[0]
      cons.pop(0)
  else:
    print('hash')
    res+=hash_map[i]
print(res)