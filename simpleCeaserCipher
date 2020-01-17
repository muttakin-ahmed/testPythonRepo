original_key_val = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,
                'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
                'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,
                's':19,'t':20,'u':21,'v':22,'w':23,'x':24,
                'y':25,'z':26}
key = 0
while True:
    try:
        key = int(input("Please enter a number less than 25: "))
    except:
        print("Input error! Please enter a number less 25")
    else:
        if key < 25:
            print("Okay! Now the encryption library is being created.")
            break
        else:
            print("Invalid Input!")
            continue

def create_dict(encryption_key):
    encryption_dict = {}
    decryption_dict = {}
    orig_keys = list(original_key_val.keys())
    encryption_keys = orig_keys[encryption_key:]
    for i in range(encryption_key):
        encryption_keys.append(orig_keys[i])
    for i in range(len(encryption_keys)):
        decryption_dict[encryption_keys[i]] = orig_keys[i]
        encryption_dict[orig_keys[i]] = encryption_keys[i]
    return encryption_dict, decryption_dict

decryption_dict, encryption_dict = create_dict(key)
#print(decryption_dict)

def continue_check():
    cc = input("Would you like to continue? Enter y/n: ")
    return cc == 'y'

def take_input_str():
    string = input("Please enter a string: ")
    return string

def encode(string):
    e_str = ""
    for ch in string.lower():
        e_str += encryption_dict[ch]
    return e_str
def decode(string):
    d_str = ""
    for ch in string.lower():
        d_str += decryption_dict[ch]
    return d_str

print("So what are planning to to?")
while True:
    try:
        choice = input("Please enter 'e' to encode or 'd' to decode: ")
    except:
        print("Input error! Please enter a valid input.")
    else:
        if choice == 'e':
            print(encode(take_input_str()))
        elif choice == 'd':
            print(decode(take_input_str()))
        else:
            print("Invalid input.")
            continue
        
        if(continue_check() == True):
            continue
        else:
            print("Goodbye!")
            break
