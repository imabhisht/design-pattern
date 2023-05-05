# Factory Design Method
from abc import abstractmethod

class Notification:
    @abstractmethod
    def notify(self):
        pass

class SMSNotification(Notification):
    # Overide Funtion
    def notify(self):
        print("Sending an SMS notification")

class EmailNotification(Notification):
    # Overide Funtion
    def notify(self):
        print("Sending an Email notification")


class PushNotification(Notification):
    # Overide Funtion
    def notify(self):
        print("Sending an Push notification")


class NotificationFactory:
    @staticmethod
    def get_notification(type):
        if type == "sms":
            return SMSNotification()
        elif type == "email":
            return EmailNotification()
        elif type == "push":
            return PushNotification()
        else:
            raise Exception("Invalid Notification Type")

def main():
    notification = NotificationFactory.get_notification("sms")
    notification.notify()

    notification = NotificationFactory.get_notification("email")
    notification.notify()

    notification = NotificationFactory.get_notification("push")
    notification.notify()

    notification = NotificationFactory.get_notification("invalid")
    notification.notify()


if __name__ == "__main__":
    main()