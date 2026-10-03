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

x = input("plz type a sentence you want to encode: ")

if x == "" :
    print ("sorry didn't get that so im deafulting to : I im typing this for no reason ")                
    x = "I im typing this for no reason"
else:
    print("i got yout message :", x)

print()

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
