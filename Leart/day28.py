class SetOneMixin:
    __slots__ = []
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'Already Has this Key')
        return super().__setitem__(key, value)
class SetOneDict(SetOneMixin, dict):
    pass

my_dict = SetOneDict()
try:
    my_dict['username'] = 'Jack'
    my_dict['username'] = 'Toby'
except KeyError:
    print('Something wrong')
print(my_dict)