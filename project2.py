import random, time

letters='abcdefghijklmnopqrstuvwxyz'

def caesar_cipher(x, n):   
    s=''
    for i in range(len(x)):
        if x[i] == ' ':
            s = s + ' '
        else:
            idx = letters.find(x[i])
            new_idx = (idx+n)%26
            s = s + letters[new_idx]
    return s




def even_odd_swap(x):
    if len(x) % 2 != 0:
        x = x + ' '
    even_letters = x[0::2]
    odd_letters = x[1::2]
    s = ''
    for i in range(len(even_letters)):
        s = s+odd_letters[i]
        s = s+even_letters[i]
    return s

def swap_middle(x):
    if len(x) % 2 != 0:
        x = x + ' '
    first_half = x[0:int(len(x)/2):1]
    second_half = x[int(len(x)/2)::1]
    s = ''
    s = s + second_half
    s = s + first_half
    return s

def reverse(x):
    s = x[::-1]
    return s

def swap_mid_rev(x):
    s_swap = swap_middle(x)
    s = reverse(s_swap)
    return s

def swap_mid_rev_decode(x):
    s_rev = reverse(x)
    s = swap_middle(s_rev)
    return s

def reverse_word(x):
    words = x.split(' ')
    s = ''
    for kk in range(len(words)):
        s = s+reverse(words[kk])+' '
    return s
"""
def make_sure():
    global x
    x = input("plz type a sentence you want to encode: ")
    if x == "" :
        print ("sorry didn't get that PLAESE RETRY")                
        make_sure()
    else:
        print("i got yout message :", x)

make_sure()

print()

def main():
    x_even_odd = even_odd_swap(x)
    x_rev = reverse(x)
    x_rev_word = reverse_word(x)
    x_swap_mid = swap_middle(x)
    x_swap_mid_rev = swap_mid_rev(x)

    print("encoded version")

    print("1.", x_even_odd)

    print("2.", x_rev)

    print("3.", x_rev_word)

    print("4.", x_swap_mid)

    print("5.", x_swap_mid_rev)

    print()

    print("decoded verion")

    print("1.", even_odd_swap(x_even_odd))  
    
    print("2.", reverse(x_rev))  
    
    print("3.", reverse_word(x_rev_word))  
    
    print("4.", swap_mid_rev(x_swap_mid_rev))  
    
    print("5.", swap_middle(x_swap_mid)) 

#main()
#def ask_if_want_to_encode_again():
 #   print("1.again/retry")
  #  print("2.exit")
   # input()

"""
print()
print()


msg = 'python'
secret_code = ''

for kk in range(10):
    n = random.randint(0, 25)
    secret_code = secret_code + letters[n]

msg = msg + secret_code


encoder = random.randint(0, 3)
encoder = 0
if encoder == 0:
    msg_enc = msg
elif encoder == 1:
    msg_enc = even_odd_swap(msg)
elif encoder == 2:
    msg_enc = reverse(msg)
else:
    msg_enc = swap_middle(msg)

msg_enemy = caesar_cipher(msg_enc, random.randint(1, 25))



print()
print('I am hearing ...')
print(msg_enemy)
print()
time.sleep(1)
print("decoding time")




for kk in range(1, 26):

    msg_dec = caesar_cipher(msg_enemy, kk)
    msg_dec_eo = even_odd_swap(msg_dec)
    msg_dec_r  = reverse(msg_dec)
    msg_dec_ms = swap_middle(msg_dec)
   

    print(msg_dec, msg_dec_eo, msg_dec_r, msg_dec_ms)



    

    if msg_dec[0:6:1]=='python':
        print('code cracked ...')
        print('Secret code is ...')
        print(msg_dec[6::1])
        break
    elif msg_dec_eo[0:6:1]=='python':
        print('code cracked ...')
        print('Secret code is ...')
        print(msg_dec_eo[6::1])
        break
    elif msg_dec_r[0:6:1]=='python':
        print('code cracked ...')
        print('Secret code is ...')
        print(msg_dec_r[6::1])
        break
    elif msg_dec_ms[0:6:1]=='python':
        print('code cracked ...')
        print('Secret code is ...')
        print(msg_dec_ms[6::1])
        break
