

'''For example with a shift of 1, A would be replaced by B, B would become C, and so on.
A String of lower case letters, called Text.
An Integer between 0-25 denoting the required shift.
We can either write another function decrypt similar to encrypt, that’ll apply the given shift in the opposite direction to decrypt the original text.'''

def encrypt():

  text = input("Enter the text to be encrypted")
  num = int(input("Enter the shift"))

  text = text.upper()

  list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
  code = ""

  for char in text:
    for item in list1:
      if char == item:
        index = list1.index(item)

        if index+num <25:
            code+= list1[index+num]
        if index+num >24:
            newindex = (index+num) - 25
            code+= list1[newindex]

  print(f"Encrypted code : {code}")

def decrypt():

  text = input("Enter the text to be decrypted")
  num = int(input("Enter the shift"))

  text = text.upper()

  list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
  code=""

  for char in text:
    for item in list1:
      if char == item:
        index = list1.index(item)

        if index-num >=0:
            code+= list1[index-num]
        if index-num <0:
            newindex = (index-num) + 25
            code+= list1[newindex]

  print(f"Decrypted code : {code}")

while True:

  print("Welcome to the Caeser Cipher")
  print("\n Would you like to Encrypt or Decrypt")
  choice = input ("\n Enter : \n E to Encrypt \n D to Decrypt \n Your choice :  ")

  if choice == "E":
    encrypt()
    break
  if choice == "D":
    decrypt()
    break
  else:
    print("Please enter a valid option")