class Bird:
    def __init__(self, isFly):
        self.isFly = isFly

    def intro(self):
        if(self.isFly):
            return "Bisa Terbang"
        else:
            return "Tidak Bisa Terbang"

class Child(Bird):
    def __init_subclass__(self) -> Bird:
        return super().__init_subclass__()

    def tes(self):
        return self.isFly

burung = Bird(True)
child = Child(burung)

print(child.intro())
# print(burung.intro())