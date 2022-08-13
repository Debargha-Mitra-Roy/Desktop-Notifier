from plyer import notification
import time

if __name__ == '__main':

    notification.notify(

        title="*** Take Rest ***",
        message="Rest is vital for better mental health.",
        app_icon="./images/rest.ico",  # for Windows System
        timeout=5
    )

    time.sleep(60)
