name_data = "[a, b, c]"
mail_data = "[leahpar0401@gmail.com,leahpar0401@icloud.com,leahpar0401@kookmin.ac.kr]"

# Remove extra characters and split into individual elements
manito_sender = [name.strip() for name in name_data[1:-1].split(',')]
manito_mail = [email.strip() for email in mail_data[1:-1].split(',')]

shuffle_manito = manito_sender.copy()  # Make a copy to shuffle

print(manito_sender)
print(manito_mail)
print(shuffle_manito)
