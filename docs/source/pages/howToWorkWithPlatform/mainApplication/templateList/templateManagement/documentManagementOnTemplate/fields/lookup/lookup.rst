============
Lookup field
============

Lookup field allows you to create an automatically populating field which will return a value from a specified column of a row of parent dictionary field value.

How to add lookup field to template
====================================

1. To add field to the document, use one of field adding methods with field icon in the Fields tab of template editor menu

.. image:: pic_lookup/lookupIcon.png
   :width: 600
   :align: center

2. Field creation form will appear, where you should set field attributes

.. image:: pic_lookup/lookupModal.png
   :width: 600
   :align: center

3. Name - this is a name of a field
4. Placeholder - this text will be shown in the input box before anything is filled in (can be left empty, field name will be used instead)
5. Optional - this attribute specifies if this field is mandatory to fill
6. Allow custom values - this attribute specifies if field will allow free text input besides automatic population

.. note:: If dictionary has optionality or custom values attributes enabled, same attributes will also be enforced on all related lookups.

7. Search - this attribute specifies if this field should be eligible for mailbox page search
8. Document - dropdown selector of a document, where desired parent dictionary is located
9. Related to - dropdown selector of a desired parent dictionary
10. Column name - dropdown selector of a desired column in a parent dictionary

When all attributes are set, you can click Save button and field will be added. You can click field to see its properties and update them. Also you can delete the field in same menu.

.. image:: pic_lookup/lookupProperties.png
   :width: 600
   :align: center