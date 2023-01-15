from core import Eurydice

def main(start_message):
    while True:
        try:
            print(start_message)
            start = Eurydice("Эвридика")
            start.listen()
        except Exception as e:
            print(e)
            pass

if __name__ == "__main__":
    main("Bot is starting...")
