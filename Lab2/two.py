# Factory Design Pattern

from abc import abstractmethod
import os

#Interface
class Notification:
    @abstractmethod
    def notify(self):
        pass





#Implementations (Factory - 1)
class SMSNotification(Notification):
    # Overide Funtion
    def notify(self):
        print("[System] Sending an SMS notification")
    
class EmailNotification(Notification):
    # Overide Funtion
    def notify(self):
        print("[System] Sending an Email notification")

class PushNotification(Notification):
    # Overide Funtion
    def notify(self):
        print("[System] Sending an Push notification")


# Notification Factory - 1
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
            


#Implementations (Factory - 2)
class SocialSMSNotification(Notification):
    def notify(self):
        print("[Social] Sending an SMS notification")

class EmailSMSNotification(Notification):
    def notify(self):
        print("[Social] Sending an Email notification")

class PushSMSNotification(Notification):
    def notify(self):
        print("[Social] Sending an Push notification")


# Notification Factory - 1
class SocialMediaNotificationFactory(NotificationFactory):
    @staticmethod
    def get_notification(type):
        if type == "sms":
            return SocialSMSNotification()
        elif type == "email":
            return EmailSMSNotification()
        elif type == "push":
            return PushSMSNotification()
        else:
            raise Exception("Invalid Notification Type")



# Abstract Factory
class ClientNotificationFactory():
    @staticmethod
    def get_notification_factory(type):
        if type == "social":
            return SocialMediaNotificationFactory()
        elif type == "system":
            return NotificationFactory()
        else:
            raise Exception("Invalid Notification Type")



#Client
def main():
    while True:
        print("-------Notification Factory System-------")
        print("1. System Notification")
        print("2. Social Media Notification")
        print("3. Exit")
        print("-----------------------------------------")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            notification_factory = ClientNotificationFactory.get_notification_factory("system")
            notification = notification_factory.get_notification("sms")
            notification.notify()

            notification = notification_factory.get_notification("email")
            notification.notify()

            notification = notification_factory.get_notification("push")
            notification.notify()
            input("Press Enter to continue...")

            # notification = notification_factory.get_notification("invalid")
            # notification.notify()


        elif choice == 2:
            notification_factory = ClientNotificationFactory.get_notification_factory("social")
            notification = notification_factory.get_notification("sms")
            notification.notify()

            notification = notification_factory.get_notification("email")
            notification.notify()

            notification = notification_factory.get_notification("push")
            notification.notify()

            input("Press Enter to continue...")

            # notification = notification_factory.get_notification("invalid")
            # notification.notify()

        elif choice == 3:
            break

        os.system("clear")



if __name__ == "__main__":
    main()

# Create Factory Design Pattern 