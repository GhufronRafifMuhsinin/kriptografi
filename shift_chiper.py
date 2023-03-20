import string

alphabet = string.ascii_lowercase 

def shift_cipher(text, shift, mode):
    plain = text.lower()
    shift %= len(alphabet)
    ciphertext = ''
     
    for letter in plain:
        position = alphabet.find(letter)
         
        if position == -1:
            ciphertext += letter
            continue
         
        if mode == 'enc':
            ciphertext += alphabet[(position+shift)%len(alphabet)]
        elif mode == 'dec':
            ciphertext += alphabet[(position-shift)%len(alphabet)]
              
    return ciphertext

#ENKRIPSI
print("ENKRIPSI 43")
print(f'{shift_cipher("ghufron rafif muhsinin",43,"enc")}')
print("============================")
#DESKRIPSI
print("DESKRIPSI 43")
print(f'{shift_cipher("xylwife irwzw dlyjzeze",43,"dec")}')

