import math

key=input("Masukan teks keyword =    ").lower().replace(" ", "")
plain_text = input("Masukkan plain text =   ").lower().replace(" ", "")

len_key = len(key)
len_plain = len(plain_text)
row = int(math.ceil(len_plain / len_key))
matrix = [ ['X']*len_key for i in range(row) ]

t = 0
for r in range(row):
  for c,ch in enumerate(plain_text[t : t+ len_key]):
    matrix[r][c] = ch
  t += len_key


sort_order = sorted([(ch,i) for i,ch in enumerate(key)])


cipher_text = ''
for ch,c in sort_order:
  for r in range(row):
    cipher_text += matrix[r][c]
  
print("Encryption")
print("Plain text  =   ",plain_text)
print("Cipher text =   ",cipher_text)

matrix_new = [ ['X']*len_key for i in range(row) ]
key_order = [ key.index(ch) for ch in sorted(list(key))]  


t = 0
for c in key_order:
  for r,ch in enumerate(cipher_text[t : t+ row]):
    matrix_new[r][c] = ch
  t += row

p_text = ''
for r in range(row):
  for c in range(len_key):
    p_text += matrix_new[r][c] if matrix_new[r][c] != 'X' else ''

print("Decryption")
print("Cipher text =   ",cipher_text)
print("Plain text  =   ",p_text)
