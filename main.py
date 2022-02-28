from src import catgirl_bot
import schedule as sch
import logging as log
import time
# ? Need To Eventually Make Logs Decorators ?
# ? Take Into Account what if the image API pulls the same image twice? ?

# ! Not Exactly Sure How Multiple File Logging Works, But Ill Put This Here for now.
log.basicConfig(filename='./catgirl/logs/app.log', filemode='w',
                format='%(asctime)s - %(message)s', level=log.INFO)

def main():
    log.info("--- Starting New Catgirl Post. ---")
    catgirl_bot.newStoicCatgirlPost()
    log.info("--- Catgirl Post Complete. ---")

if __name__ == "__main__":
    log.info("--- Starting Catgirl Bot. ---")
    sch.every(2).hours.do(main)  # Runs Main Every 2 Hours
    # sch.every(1).minutes.do(main)  # Runs Main Every 1 Minute
    while True:
        sch.run_pending()
        time.sleep(1)
