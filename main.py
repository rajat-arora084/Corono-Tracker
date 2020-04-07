import time
from parse_corona_cases import ParseCovidCases
from desktop_notification import DesktopNotification
from parse_current_cases import ParseCurrentCases
from log_file import LogFile


# Utility Function to find the Live cases & provide the inform via desktop notification.
def main():

    result = dict()
    try:
        corona_cases_parser = ParseCovidCases()
        corona_cases = corona_cases_parser.main() or dict()

        current_cases_parser = ParseCurrentCases()
        current_cases = current_cases_parser.find_current_cases()
        print(corona_cases, current_cases)

        log_file = LogFile()
        log_file.write(corona_cases)

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
            result = 1, corona_cases
        else:
            result = 0, corona_cases
    except Exception as err:
        print('Some error occured while fetching the data. Pls check your Internet connection. \n{}'.format(err.message))
    finally:
        return result


def run():

    current_run_results, show_message = list(), False
    desktop_notifier = DesktopNotification()
    while 1:
        result, corona_cases = main()
        if not result:
            print('Same data')
            current_run_results.append(0)
            if len(current_run_results) == 3:
                current_run_results = list()
                show_message = True
        else:
            show_message = True
            current_run_results = list()
        # print(show_message, result, current_run_results)
        if show_message:
            desktop_notifier.show_notification(corona_cases)

        time.sleep(300)
        show_message = False


if __name__ == '__main__':
    run() #main()
