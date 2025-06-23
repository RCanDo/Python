#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:45:46 2024

@author: arek

Do first
https://protobuf.dev/getting-started/pythontutorial/#compiling-protocol-buffers

https://protobuf.dev/getting-started/pythontutorial/#protobuf-api
"""

import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"

phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.PHONE_TYPE_HOME

phone

person
person.phones

person.no_such_field = 1  # raises AttributeError
person.id = "1234"        # raises TypeError

type(person)    # addressbook_pb2.Person
type(phone)     # addressbook_pb2.PhoneNumber
type(person.phones)     # google.protobuf.pyext._message.RepeatedCompositeContainer

# Standard Message Methods
"""
Each message class also contains a number of other methods that let you check or manipulate
the entire message, including:

    IsInitialized(): checks if all the required fields have been set.

    __str__(): returns a human-readable representation of the message, particularly useful for debugging. (Usually invoked as str(message) or print message.)

    CopyFrom(other_msg): overwrites the message with the given message’s values.

    Clear(): clears all the elements back to the empty state.

These methods implement the Message interface.
For more information, see the
[complete API documentation for Message](https://googleapis.dev/python/protobuf/latest/google/protobuf/message.html#google.protobuf.message.Message).
"""
str(person)
print(person)

person3 = addressbook_pb2.Person()
person.IsInitialized()  # True
person3.IsInitialized()  # True
person3.CopyFrom(person)
person3  # ok

person3.Clear()
person3      # nothing

# Serialisation
person.SerializeToString()      # this is BINARY !
# b'\n\x08John Doe\x10\xd2\t\x1a\x10jdoe@example.com"\x0c\n\x08555-4321\x10\x02'
len('\n\x08John Doe\x10\xd2\t\x1a\x10jdoe@example.com"\x0c\n\x08555-4321\x10\x02')  # 45

person2 = addressbook_pb2.Person()
person2.ParseFromString(person.SerializeToString())  # 45  length of the string above
person2  # ok
"""
These are just a couple of the options provided for parsing and serialization.
[complete API documentation for Message](https://googleapis.dev/python/protobuf/latest/google/protobuf/message.html#google.protobuf.message.Message).
"""
