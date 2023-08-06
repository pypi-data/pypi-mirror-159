class Table(object):
    name = ""
    table_content = [[]]

    def display(self, divider=", "):
        string = ""
        for row in self.table_content:
            for record in range(int(len(row))):
                string = string + str(row[record])
                if int(len(row)) != record + 1:
                    string = string + str(divider)
            string = string + "\n"
        return string

        return string

    def get_col(self, col_name):
        col_position = self.table_content[0].index(col_name)

        col = []

        for i in range(int(len(self.table_content))-2):
            col.append(self.table_content[i+1][col_position])

        return col

    def add_expand(self, new_col_name, old_col_name, action, value):
        result = []

        for i in self.get_col(old_col_name):
            if action == "+" or action == "add":
                result.append(float(i) + float(value))

            elif action == "-" or action == "subtract":
                result.append(float(i) - float(value))

            elif action == "*" or action == "multiply":
                result.append(float(i) * float(value))

            elif action == "/" or action == "divide":
                result.append(float(i) / float(value))

            elif action == "join":
                result.append(str(i) + str(value))

            else:
                raise Exception(f"Unkown action '{action}'")

        self.add_col(new_col_name, result)

    def add_row(self, new_content):
        self.table_content.append(new_content)

    def add_col(self, col_name, default_value=""):
        self.table_content[0].append(col_name)

        for i in range(int(len(self.table_content)) - 2):
            if type(default_value) is str:
                self.table_content[i + 1].append(default_value)
            elif type(default_value) is list:

                self.table_content[i + 1].append(default_value[i])

    def edit_row(self, row_num, col_name, new_value):
        self.table_content[row_num][self.table_content[0].index(col_name)] = new_value

    def filter(self, col_name, value, type="exact", search_start=1, search_end="END", add_headers_to_result=True, legecy=False):
        if search_end == "END":
            search_end = int(len(self.table_content))

        result_list = []
        for i in self.table_content[search_start:search_end]:

            if type == "exact":
                if i[self.table_content[0].index(col_name)] == value:
                    result_list.append(i)
            elif type == "iexact":
                if i[self.table_content[0].index(col_name)].lower() == value.lower():
                    result_list.append(i)

            elif type == "greaterthan":
                if float(i[self.table_content[0].index(col_name)]) > float(value):
                    result_list.append(i)

            elif type == "lessthan":
                if float(i[self.table_content[0].index(col_name)]) < float(value):
                    result_list.append(i)

            else:
                raise Exception(f'Could not find filter method "{type}"')

        if add_headers_to_result:
            result_list.insert(0, self.table_content[0])

        if legecy:
            return result_list
        else:
            temp_table = Table()
            temp_table.table_content = result_list
            return temp_table

    def save(self, path, divider=","):
        content = self.display(divider)
        with open(path, 'w') as csv:
            csv.write(content)


class CsvTable(Table):
    def __init__(self, csv_path, divider=","):
        self.csv_path = csv_path

        with open(csv_path) as csv_file:
            csv_content = csv_file.read()

        csv_content = csv_content.split("\n")

        csv_content_list = []
        for row in csv_content:
            csv_content_list.append(row.split(divider))

        self.table_content = csv_content_list
