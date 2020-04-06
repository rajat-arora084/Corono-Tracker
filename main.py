import time
from parse_corona_cases import ParseCovidCases
from desktop_notification import DesktopNotification
from parse_current_cases import ParseCurrentCases
from log_file import LogFile


# Utility Function to find the Live cases & provide the infor via desktop notification.
def main():

    corona_cases_parser = ParseCovidCases()
    corona_cases = corona_cases_parser.main()

    current_cases_parser = ParseCurrentCases()
    current_cases = current_cases_parser.find_current_cases()
    print(corona_cases, current_cases)

    log_file = LogFile()
    log_file.write(corona_cases)

    desktop_notifier = DesktopNotification()

    data_updated = False

    for key in corona_cases.keys():
        if corona_cases[key] != current_cases[key]:
            data_updated = True
            break

    if data_updated:
        if current_cases_parser.update_data(corona_cases):
            log_file.write('Data Updated in Current Cases txt')
        else:
            message = 'Please manually update the corona cases.\nOtherwise you will get repeated updates.'
            log_file.write(message)
            print(message)
        desktop_notifier.show_notification(corona_cases)
    else:
        print('Same data')


def run():
    while 1:
        main()
        time.sleep(900)


if __name__ == '__main__':
    run()
