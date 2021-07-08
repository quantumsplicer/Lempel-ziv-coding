from struct import *
   
file = open("input_file.txt")                 
data = file.read()                      

dictionary_size = 256                   
dictionary = {chr(i): i for i in range(dictionary_size)}    
string = ""             
compressed_data = []    

for symbol in data:                     
    string_plus_symbol = string + symbol 
    if string_plus_symbol in dictionary: 
        string = string_plus_symbol
    else:
        compressed_data.append(dictionary[string])
        if(len(dictionary) <= 4096):
            dictionary[string_plus_symbol] = dictionary_size
            dictionary_size += 1
        string = symbol

if string in dictionary:
    compressed_data.append(dictionary[string])

data_bin = ''.join(format(ord(i), '08b') for i in data)
res = ''.join(format(i, '09b') for i in compressed_data)
print("Total bits before compression: " + str(len(data_bin)))
print("Total bits after compression: " + str(len(res)))
output_file = open("file_encoded.lzw", "wb")
for data in compressed_data:
    output_file.write(pack('>H',int(data)))
  
output_file.close()
file.close()