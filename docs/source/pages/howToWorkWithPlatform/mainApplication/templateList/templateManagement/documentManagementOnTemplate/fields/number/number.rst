============
Number field
============

Number field allows you to create dynamic input box which will be filled by participants of the envelope processing flow. It can be added to structured and PDF documents.

How to add number field to template
===================================

1. To add field to the document, use one of field adding methods with field icon in the Fields tab of template editor menu

.. image:: pic_number/numberIcon.png
   :width: 600
   :align: center

2. Field creation form will appear, where you should set field attributes

.. image:: pic_number/numberModal.png
   :width: 600
   :align: center

3. Name - this is a name of a field
4. Role name - this is a role which will be assgined to fill this field
5. Placeholder - this text will be shown in the input box before anything is filled in (can be left empty, field name will be used instead)
6. Optional - this attribute specifies if this field is mandatory to fill
7. Search - this attribute specifies if this field should be eligible for mailbox page search
8. Adapt to the local format - this attribute specifies if numbers will be formatted according to regional standard

.. note:: Numbers in envelope view will be formatted according to standard of a region which is selected on User profile page. You can see formatting example under region selector on that page. Numbers in printable versions of the documents will always be formatted according to platform region standard.

9. Increase decimal places - if enabled, zeroes will be added to fill all empty decimal places of field value
10. Precision - number of decimal places allowed in field (no limit is applied if left empty)

.. note:: If value inside the field has more decimal places then allowed by precision attribute, all extra places will be trimmed. No rounding will be applied. E.g. if original value is 1.99 it will be changed to 1.9 if precision is set to 1 and will be changed to 1 if precision is set to 0.

11. Min - minimal value allowed in field (no limit is applied if left empty)
12. Max - maximal value allowed in field (no limit is applied if left empty)

.. warning:: Maximum allowed character count for number field is 15 (according to `IEEE 754 <http://https://en.wikipedia.org/wiki/IEEE_754>`_). Please note this includes decimal places. This means that if your field has precision attribute set to 3 and you insert a value 999999999999999 or more characters, it will be converted to 999999999999.000.

When all attributes are set, you can click Save button and field will be added. You can click field to see its properties and update them. Also you can delete the field in same menu.

.. image:: pic_number/numberProperties.png
   :width: 600
   :align: center