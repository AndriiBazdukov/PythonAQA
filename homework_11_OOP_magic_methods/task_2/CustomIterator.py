class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self.sequence = sequence
        self.start_index = start_index
        self.end_index = end_index
        self.current_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.start_index or self.current_index > self.end_index:
            raise StopIteration

        if self.current_index >= len(self.sequence):
            raise StopIteration

        value = self.sequence[self.current_index]
        self.current_index += 1
        return value

