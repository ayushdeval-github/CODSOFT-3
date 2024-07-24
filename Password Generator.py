while True:
  import string
  import random

  def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
  def save_password(password, filename):
    try:
        with open(filename, 'w') as file:
            file.write(password)
        print(f"Password saved to {filename}")
    except IOError as e:
        print(f"An error occurred while saving the password: {e}")

  def main():
    try:
        length = int(input("Enter the desired length for the password: "))
        if length < 1:
            raise ValueError("Password length must be at least 1")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return

    password = generate_password(length)

    print(f"Generated password: {password}")

    filename = input("Enter the filename to save the password: ")
    
    save_password(password, filename)

  if __name__ == "__main__":
    main()
  another_password=input("do you want to another password ? (yes/no):") 
  if another_password== "no":
      break
