import csv


class Control:
    def __init__(self, controlfile):
        self.controlfile = controlfile
        self.headers = None
        self.ids = {}
        self.ler_control_file()

    def ler_control_file(self):
        with open(self.controlfile) as file:
            for num, line in enumerate(file, 1):
                if num == 1:
                    self.headers = line
                    fields = self.headers.rstrip().split(',')
                elif num == 2:
                    values = line.rstrip().split(',')
        if num == 1:
            values = []
            for field in fields:
                values.append(0)
            with open(self.controlfile, 'a') as file:
                writer = csv.writer(file)
                writer.writerow(values)
        for idx in range(0, len(fields)):
            self.ids[fields[idx]] = values[idx]

    def getset(self, chave):
        print(f'self.ids={self.ids} chave={chave}')
        self.ids[chave] = int(self.ids[chave]) + 1
        with open(self.controlfile, 'w') as file:
            writer = csv.writer(file)
            writer.writerows([self.ids.values()])
        return self.ids[chave]
