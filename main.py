from datetime import datetime

print("=" * 40)
print("📚 Study Buddy AI Chatbot")
print("Type 'exit' to quit")
print("=" * 40)

while True:
    user = input("\nYou: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Ready to learn something new today?")

    elif "how are you" in user:
        print("Bot: I'm doing great and ready to help you study!")

    elif "your name" in user:
        print("Bot: I am Study Buddy AI, your learning assistant.")

    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence, which enables machines to mimic human intelligence.")

    elif "study tip" in user:
        print("Bot: Study for 25 minutes and take a 5-minute break. This is called the Pomodoro Technique.")

    elif "motivate me" in user:
        print("Bot: Success is the sum of small efforts repeated every day. Keep going!")

    elif "time" in user:
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Best of luck with your studies.")
        break

    else:
        print("Bot: Sorry, I don't understand that. Try asking for a study tip, motivation, or AI information.")