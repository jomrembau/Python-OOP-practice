class BiDirectionalDict(dict):

    def __setitem__(self, key, value):
        if key in self:
            del self[key]

        if value in self:
            del self[value]

        super().__setitem__(key,value)
        super().__setitem__(value, key)

    def __delitem__(self, key):
        super().__delitem__(self[key])
        super().__delitem__(key)

    def __len__(self):
        return super().__len__() // 2


bd = BiDirectionalDict()

bd["a"] = "1"
bd["b"] = "2"

print(bd)