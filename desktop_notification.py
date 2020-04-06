from win10toast import ToastNotifier
from parse_corona_cases import ParseCovidCases


# Notify User with a Toast Notification that lasts for 30 seconds.
class DesktopNotification:

    def __init__(self):
        self.notification = ToastNotifier()

    def show_notification(self, data):

        result = '{}: {}\n'.format('Total Cases', sum(list(data.values())))
        for case_wise_data, vicitims in data.items():
            result += '{}: {}\n'.format(case_wise_data.capitalize(), vicitims)
        result = result[:-1]
        self.notification.show_toast('Corona Update!', result, icon_path='coronavirus_virus_bacteria_icon.ico',
                                     duration=30)



