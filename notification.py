import dbus

class Notification:
    def __init__(self):
        self.notification_interface = dbus.Interface(
    object=dbus.SessionBus().get_object("org.freedesktop.Notifications", "/org/freedesktop/Notifications"), dbus_interface="org.freedesktop.Notifications")

    def notify(self, title, message):
        self.notification_interface.Notify("", 0, "", title, message, [], {"urgency" : 1}, 10000)
