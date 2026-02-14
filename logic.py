import datetime

def handle_query(text):
    text = text.lower()

    now = datetime.datetime.now()

    if "time" in text:
        return now.strftime("Time is %H:%M:%S")

    elif "date" in text:
        return now.strftime("Today's date is %d-%m-%Y")

    elif "day" in text:
        return now.strftime("Today is %A")

    elif "hello" in text:
        return "Hello Muskan 😊"

    else:
        return "I am still learning. Try something else."
