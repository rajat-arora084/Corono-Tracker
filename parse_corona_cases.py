import requests
from bs4 import BeautifulSoup


# Fetch corona cases from MOHFW website.
class ParseCovidCases:

    def __init__(self):
        self.url = 'https://www.mohfw.gov.in/'

    def main(self):
        return self.get_active_cases()

    def get_active_cases(self):
        result = list()
        try:
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, 'html.parser')
            class_tag = soup.find_all('div', {'class': 'site-stats-count'})[0]

            active_cases = class_tag.find_all('li', {'class': 'bg-blue'})[0].text
            cured_cases = class_tag.find_all('li', {'class': 'bg-green'})[0].text
            deaths = class_tag.find_all('li', {'class': 'bg-red'})[0].text
            migrated_cases = class_tag.find_all('li', {'class': 'bg-orange'})[0].text

            result = {'active_cases': active_cases, 'cured_cases': cured_cases, 'deaths': deaths,
                      'migrated_cases': migrated_cases}
            self.beautify_result(result)

        except Exception as err:
            print('Data could not be found. {}'.format(err.message))
        finally:
            return result

    def beautify_result(self, result):

        for key, value in result.items():
            result[key] = int(value.split('\n')[2])


#print(ParseCovidCases().main())
