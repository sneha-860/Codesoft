import random

class BakeryChatbot:
    def __init__(self):
        self.greetings = ['hello', 'hi', 'hey', 'howdy']
        self.menu = {
            'bread': {'white bread': 35, 'whole wheat bread': 40, 'sourdough bread': 450},
            'pastries': {'croissant': 20, 'danish': 20, 'muffin': 25, 'scone': 20},
            'cakes': {'chocolate cake': 400, 'vanilla cake': 400, 'carrot cake': 450},
            'cookies': {'chocolate chip cookies': 200, 'sugar cookies': 450, 'oatmeal cookies': 300}
        }

    def respond_to_greeting(self):
        return random.choice(["Hello! Welcome to our bakery.", "Hi there! How can I help you today?", "Hey! What can I do for you?"])

    def get_menu_item(self, category):
        if category.lower() in self.menu:
            items = self.menu[category.lower()]
            item_prices = [f"{item}: {price:.2f}" for item, price in items.items()]
            return f"We have {', '.join(item_prices)} available in our {category.lower()} section."
        else:
            return "I'm sorry, we don't have that in our menu. Would you like to see our menu?"

    def handle_message(self, message):
        message = message.lower()
        if any(greeting in message for greeting in self.greetings):
            return self.respond_to_greeting()
        elif 'menu' in message:
            return "Sure, here's what we have: Bread, Pastries, Cakes, and Cookies. What are you interested in?"
        elif 'bread' in message:
            return self.get_menu_item('bread')
        elif 'pastries' in message:
            return self.get_menu_item('pastries')
        elif 'cakes' in message:
            return self.get_menu_item('cakes')
        elif 'cookies' in message:
            return self.get_menu_item('cookies')
        else:
            return "I'm sorry, I didn't quite understand that. Could you please repeat or ask something else?"

if __name__ == "__main__":
    bakery_bot = BakeryChatbot()
    print("Bakery Chatbot: Fluffy " + bakery_bot.respond_to_greeting())
    print("You can start chatting by typing your message. It would be great if i could know your name ")
    while True:
        user_input = input(" ")
        print(" it's great to see you here ")
        if user_input.lower() == 'exit':
            print("Bakery Chatbot: Goodbye! Have a great day!")
            break
        response = bakery_bot.handle_message(user_input)
        print("Bakery Chatbot:", response)
