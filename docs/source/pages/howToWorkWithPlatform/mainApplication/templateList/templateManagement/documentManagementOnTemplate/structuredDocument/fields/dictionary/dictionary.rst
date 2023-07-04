================
Dictionary field
================

Dictionary field allows you to create dropdown selector of records from dictionary (table), e.g. list of employees (First name, last name, age, address).

How to add dictionary field to template
=======================================

1. To add field to structured document, place text cursor where you want field to be added and click its button (alternatively it can be placed via drag & drop)

.. image:: pic_dictionary/dictionaryIcon.png
   :width: 600
   :align: center

2. To add field to PDF document, drag & drop it to desired place in the document. It can be moved around and resized by lower left corner afterwards

.. image:: pic_dictionary/dictionaryPDF.png
   :width: 600
   :align: center

3. Field creation form will appear, where you should set field attributes

.. image:: pic_dictionary/dictionaryModal.png
   :width: 600
   :align: center

4. Name - this is a name of a field
5. Role name - this is a role which will be assgined to fill this field
6. Placeholder - this text will be shown in the input box before anything is filled in (can be left empty, field name will be used instead)
7. Optional - this attribute specifies if this field is mandatory to fill
8. Allow custom values - this attribute specifies if field will allow free text input besides selection from predefined dictionary values
9. Search - this attribute specifies if this field should be eligible for mailbox page search
10. Dictionary - input for desired dictionary selection. Start typing dictionary name and available dictionaries list will appear
11. Column name (appears after dictionary is selected) - dropdown selector of a desired column

When all attributres are set, you can click Save button and field will be added. You can click field to see its properties and update them. Also you can delete the field in same menu.

.. image:: pic_dictionary/dictionaryStructured.png
   :width: 600
   :align: center