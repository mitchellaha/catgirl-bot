from src import catgirl_bot
import schedule as sch
import time

def main():
    currentTime = time.localtime()
    print("Starting Catgirl Bot at " + str(currentTime.tm_hour) + ":" + str(currentTime.tm_min))
    catgirl_bot.newStoicCatgirlPost()
    print("Catgirl Bot Finished.")

if __name__ == "__main__":
    sch.every(2).hours.do(main)  # Runs Main Every 2 Hours
    while True:
        sch.run_pending()
        time.sleep(1)
