#!python3

from typing import *

class Field(object):
    '''
        Get `name` and `column_type` as private properties
        while initialize class.
        Format as string `Field:xxx`, xxx is the name of class.
    '''
    def __init__(self, name: str, column_type: str):
        self.name = name
        self.column_type = column_type

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}:{self.name}>'

class StringField(Field):
    '''
        Call super.__init__() while initializing.
    '''
    def __init__(self, name: str):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    '''
        Call super.__init__() while initializing.
    '''
    def __init__(self, name: str):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    '''
        1. Construct a new mapping
        1. Iterate each key-value of a class. Print and binding with
           the mapping if the value is a field class
        1. Delete the property just passed in
        1. Create a specific property `__mapping__` to keep the mapping
        1. Create a specific property `__table__` to keey the class name
           that passed in
    '''
    @classmethod
    def __new__(mcs, name: str, bases: tuple, attrs: dict) -> type:
        if name == 'Model':
            return type.__new__(mcs, name, bases, attrs)
        print(f'Found model: {name}')
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                print(f'Found mapping: {k} ==> {v}')
                mappings[k] = v
        for k in mappings:
            attrs.pop(k)
        attrs['__mappings__'] = mappings # keep the mapping of properties and columns
        attrs['__table__'] = name        # presume the table name equal with the class name
        return type.__new__(mcs, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwarg):
        super(Model, self).__init__(**kwarg)

    def __getattribute__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute {key}")

    def __setattr__(self, key: Any, value: Any) -> None:
        self[key] = value

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
        sql = f'insert into {self.__table__} ({",".join(fields)}) ' +\
              f'values ({",".join([str(i) for i in args])})'
        print(f'SQL: {sql}')
        print(f'ARGS: {str(args)}')

class User(Model):
    '''
        - id       : Integer
        - name     : String
        - email    : String
        - password : String
    '''
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
