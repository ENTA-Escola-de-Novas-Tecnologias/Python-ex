class Control:
    def __init__(self, controlfile):
        self.controlfile = controlfile
        self.headers = None
        self.ids = {}
        self.ler_control_file()

    def ler_control_file(self):
        with open(self.controlfile, encoding='utf-8') as file:
            self.headers = next(file)
            fields = self.headers.rstrip().split(',')
            values = next(file).rstrip().split(',')
        for idx in range(0, 4):
            self.ids[fields[idx]] = values[idx]

    def getset(self, chave):
        self.ids[chave] = str(int(self.ids[chave]) + 1)
        with open(self.controlfile, 'w', encoding='utf-8') as file:
            file.write(self.headers)
            file.write(",".join(self.ids.values()))
        return self.ids[chave]
