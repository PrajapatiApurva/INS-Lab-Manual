import random 
P = 13  
G = 23   
a = random.randint(1, P-1)
b = random.randint(1, P-1)

A = pow(G, a, P) 
B = pow(G, b, P)
 
S_Apurva = pow(B, a, P) 
S_Jay = pow(A, b, P)
 
print(f"Apurva’s Shared Secret: {S_Apurva}")
print(f"Jay’s Shared Secret: {S_Jay}")
 
if S_Apurva == S_Jay:
    print("Key exchange successful! Shared secret established.")
else:
    print("Key exchange failed. The shared secrets do not match.")
