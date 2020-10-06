==========
Dictionary
==========

.. contents:: Сontent:
   :depth: 6

---------

Dictionary - is a list of records in a systematic form, e.g. list of employee(Name, Surname, Age, Address).
Data from dictionary could be used in envelope:

1. Create dictionary field in template.

2. Set dictionary and column from which recipient will select data to field.

Dictionary template field
=========================
To add dictionary field to template drag and drop dictionary field from the fields bar to the document. Select dictionary, receiver role and column of the dictionary.
Also it's possible to set "Allow custom value" it allows to enter custom value on envelope stage (when receiver fill in the document).


Dictionary envelope field
=========================
User need to select value from the list of records values. If allow custom value attribute is true - user can enter custom value.
After value was set to field and processing flow was continued - value of dictionary field is blocked. Any updates in dictionary doesn't apply to this field.