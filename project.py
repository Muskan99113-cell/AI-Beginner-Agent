from logic import handle_query

print("AI Agent Started")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("AI: Bye 👋")
        break

    answer = handle_query(user)
    print("AI:", answer)
