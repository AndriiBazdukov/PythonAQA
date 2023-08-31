# Task 1
palindrome = input("Please enter palindrome ")
reverted_palindrome = palindrome[::-1]
message = "+" if palindrome == reverted_palindrome else "-"
print(message)

# Task 2
text = "Hello world".lower()
splitted_text = text.split()
word = input("Please enter word for search ").lower()

if word in splitted_text:
    print("YES")
else:
    print("NO")

# Task 3
email_address = input("Please enter email address ")
email_validation_message = "YES" if "@" in email_address and "." in email_address else "NO"
print(email_validation_message)

# Task 4

text_with_spaces = input("Please enter text with spaces ")
text_with_spaces_splitted = text_with_spaces.split()
list_length = len(text_with_spaces_splitted)
if list_length >= 3:
    print(text_with_spaces_splitted[-3:])
else:
    print(f"List is too short, Length: {list_length}")

# Task 5

ip_address = input("Enter IP address separated with dots \".\"").replace(" ", "")
list_of_numbers_in_IP_address = ip_address.split(".")

if (len(list_of_numbers_in_IP_address) == 4
    and list_of_numbers_in_IP_address[0].isdigit()
    and 0 <= int(list_of_numbers_in_IP_address[0]) <= 255
    and list_of_numbers_in_IP_address[1].isdigit()
    and 0 <= int(list_of_numbers_in_IP_address[1]) <= 255
    and list_of_numbers_in_IP_address[2].isdigit()
    and 0 <= int(list_of_numbers_in_IP_address[2]) <= 255
    and list_of_numbers_in_IP_address[3].isdigit()
    and 0 <= int(list_of_numbers_in_IP_address[3]) <= 255):
    print("IP is correct")
else:
    print("Invalid IP address")

# Альтернатива

ip_address = input("Enter IP address separated with dots \".\"").replace(" ", "")
list_of_numbers_in_IP_address = ip_address.split(".")

if (len(list_of_numbers_in_IP_address) == 4
        and all(strings.isdigit() and 0 <= int(strings) <= 255 for strings in list_of_numbers_in_IP_address)):
    print("IP is correct")
else:
    print("Invalid IP address")
