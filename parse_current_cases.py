import ast

# Find corna cases from file.
class ParseCurrentCases:

    def __init__(self):
        self.file_name = 'Current_cases.txt'

    def find_current_cases(self):

        file = open(self.file_name, 'r')
        current_data = ast.literal_eval(file.readlines()[0])
        file.close()
        return current_data

    def update_data(self, data):

        data_updated = True
        try:
            file = open(self.file_name, 'w')
            file.write(str(data))
            file.close()
        except Exception as err:
            print(err.message)
            data_updated = False
        finally:
            return data_updated
