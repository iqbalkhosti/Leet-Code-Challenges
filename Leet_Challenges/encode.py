
s = ["name", "strabuck"]

def encode_list(words):

    encoded_str = ""

    for word in words:

        encoded_str +=str(len(word))+"@"+word 

    return encoded_str

def decode_string(s):

    decoded = []
    i = 0

    while(i<len(s)):
        j = i

        while(s[j] != "@"):
            j+=1
        
        
        length_of_word = int(s[i:j])

        print(f"length of word: {length_of_word}\n")

        word = s[j+1:j+1+length_of_word]
        print(f"word: {word}")
        
        decoded.append(word)

        i = j+1 +length_of_word
        print(f"\nvalue of i: {i}")
    return decoded

encoded = encode_list(s)
print(encoded)
print(decode_string(encoded))
