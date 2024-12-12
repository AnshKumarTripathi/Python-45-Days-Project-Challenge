# Day 12 of 45 days coding challnege. Pyhton edition
import re
import pyttsx3

engine = pyttsx3.init()

# in future updates this will be removed....

def option():
  print("This is a simple chatbot with limited lessons. You can take lessons about life from below option.")
  print("Are you having problems regarding...")
  print("Life?\nduty?\nFear of something?\nEternal Truth about life?\nWork?\nNeed wisdom?\nWhat is meditation?")
  
quotes = {
    r'life|living': [
        "For one who has conquered the mind, the mind is the best of friends, but for one who has failed to do so, his mind will remain the greatest enemy. - Bhagavad Gita 6.6",
        "You have the right to perform your prescribed duties, but you are not entitled to the fruits of your actions. - Bhagavad Gita 2.47"
    ],
    r'duty|karma': [
        "Perform your obligatory duty, because action is indeed better than inaction. - Bhagavad Gita 3.8",
        "It is better to live your own destiny imperfectly than to live an imitation of somebody else's life with perfection. - Bhagavad Gita 3.35"
    ],
    r'fear|worry|anxiety': [
        "He who has faith has wisdom; who lives in self-harmony, whose faith is his life; and who seeks wisdom, shall come to perfect peace. - Bhagavad Gita 4.39",
        "Fear not. What is not real, never was and never will be. What is real, always was and cannot be destroyed. - Bhagavad Gita 2.16"
    ],
    r'existence|truth':[
      "For one who has been born, death is certain, and for one who has died, birth is certain. Therefore, you should not lament over the inevitable. - Bhagavad Gita 2.27",
      "The soul is never born nor does it ever die; nor, once it is, does it ever cease to be. The soul is without birth, eternal, immortal, and ageless. It is not destroyed when the body is destroyed. - Bhagavad Gita 2.20"
    ],
    r'work':[
      "You have the right to perform your prescribed duties, but you are not entitled to the fruits of your actions. - Bhagavad Gita 2.47"
    ],
    r'knowledge|wisdom|learning':[
      "When a man dwells on the objects of sense, he develops attachment for them; from attachment springs desire, and from desire comes anger. - Bhagavad Gita 2.62",
      "The wise see that there is action in the midst of inaction and inaction in the midst of action. Their consciousness is unified, and every act is done with complete awareness. - Bhagavad Gita 4.18"
    ],
    r'peace|meditation|mind':[
      "Through selfless service, you will always be fruitful and find the fulfillment of your desires: this is the promise of the Creator. - Bhagavad Gita 3.11",
      "When meditation is mastered, the mind is unwavering like the flame of a lamp in a windless place. - Bhagavad Gita 6.19"
    ],
}

def get_quote(user_input):
    for pattern, quotes_list in quotes.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return quotes_list
    return ["Sorry, I don't have a quote for that."]

def speak_quote(quote):
    engine.say(quote)
    engine.runAndWait()

def chat():
    print("Chatbot: Hi! I am your Bhagavad Gita assistant. Ask me anything related to life, duty, fear, etc. Type 'exit' to end the conversation.")
    while True:
        option()
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! May you find peace and wisdom.")
            break
        quotes_list = get_quote(user_input)
        for quote in quotes_list:
            print(f"Chatbot: {quote}")
            speak_quote(quote)  

chat()
