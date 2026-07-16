# If pyperclip is not installed
# pip install pyperclip

# import section
import pyperclip

# function
def capitalise_sentence():
    input_text=pyperclip.paste()
    pyperclip.copy(input_text.title())

# Function Call
if __name__ == "__main__":
    capitalise_sentence()