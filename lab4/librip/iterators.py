class Unique():
    """Итератор для удаления дубликатов"""
    def __init__(self, input, **kwargs):
        self.item = iter(input)
        self.lst = []
        self.ignore_case = kwargs.get('ignore_case')
        print("Ignore case = ", self.ignore_case)

    def __next__(self):
        if self.ignore_case:
            buffer = next(self.item)
            buf_str = str(buffer)
            buf_str = buf_str.lower()
            while buf_str in self.lst:
                buffer = next(self.item)
                buf_str = str(buffer).lower()
            self.lst.append(buf_str)
            return buffer
        else:
            buffer = next(self.item)
            buf_str = str(buffer)
            while buf_str in self.lst:
                buffer = next(self.item)
                buf_str = str(buffer)
            self.lst.append(buf_str)
            return buffer

    def __iter__(self):
        return self
