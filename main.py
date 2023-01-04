import threading

# function to input string 
def input_thread():
    print("*********************************************")
    global user_input
    user_input = ""
    while True:
        # exception handling check if string is valid or not
        try:
            a = input("Enter string of charcters : ")
            if a.isalpha():
                print("\nNow other threads will run simultaneously and input will be mixed up")
                print("*********************************************")
                user_input = a
                break
            print("Enter valid string of alphabets only without spaces ")
            print("*********************************************")
        except:
            return  

# function to reverse string
def reverse_thread(user_input):
    reversed_input = user_input[::-1]
    print("Reverse = ",reversed_input)

# function to captalize string
def capital_thread(user_input):
    capitalized_input = ""
    for letter in user_input:
        capitalized_letter = letter.upper()
        capitalized_input += capitalized_letter
    print("Captalize = ",capitalized_input)

# function to perform shift operation 
def shift_thread(user_input):
    shifted_input = ""
    for letter in user_input:
        shifted_letter = chr(ord(letter) + 2)
        shifted_input += shifted_letter
    print("Shifted",shifted_input)


# main function 
def main():
    # input thread which will take input from user
    input_t = threading.Thread(target=input_thread)
    input_t.start()
    input_t.join()

    # Creating reverse capital and shift thread
    reverse_t = threading.Thread(target=reverse_thread, args=(user_input,))
    capital_t = threading.Thread(target=capital_thread, args=(user_input,))
    shift_t = threading.Thread(target=shift_thread, args=(user_input,))

    # Starting the other threads
    reverse_t.start()
    capital_t.start()
    shift_t.start()

    # Wait for the threads to finish
    reverse_t.join()
    capital_t.join()
    shift_t.join()


    print("*********************************************")
    print("The End !")
    print("*********************************************")


if __name__ == "__main__":
    main()