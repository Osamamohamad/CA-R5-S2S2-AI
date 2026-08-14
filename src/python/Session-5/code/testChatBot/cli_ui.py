from model import get_response
def ChatBot():
    print("\nChatBot : Hi! how can i assist you today")
    while True:
        
        user_input = input("User: ").lower()
        response=get_response(user_input)
        print("ChatBot",response)

        if user_input == "Goodbye":
            break