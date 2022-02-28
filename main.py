from src import catgirl_bot
import schedule as sch
import time

def main():
    currentTime = time.localtime()
    print("Starting Posting at " + str(currentTime.tm_hour) + ":" + str(currentTime.tm_min))
    catgirl_bot.newStoicCatgirlPost()
    print("Catgirl Bot Posted To Twitter.")

if __name__ == "__main__":
    print("Starting Catgirl Bot")
    sch.every(2).hours.do(main)  # Runs Main Every 2 Hours
    # sch.every(1).minutes.do(main)  # Runs Main Every 1 Minute
    while True:
        sch.run_pending()
        time.sleep(1)
