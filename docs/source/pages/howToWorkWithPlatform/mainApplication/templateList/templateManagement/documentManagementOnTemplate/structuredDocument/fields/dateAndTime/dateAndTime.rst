===================
Date and time field
===================

Date and time field allows you to create calendar selector which will be filled by participants of the envelope processing flow. It can be added to structured and PDF documents.

How to add date and time field to template
==========================================

1. To add field to structured document, place text cursor where you want field to be added and click its button (alternatively it can be placed via drag & drop)

.. image:: pic_dateAndTime/dateIcon.png
   :width: 600
   :align: center

2. To add field to PDF document, drag & drop it to desired place in the document. It can be moved around afterwards

.. image:: pic_dateAndTime/datePDF.png
   :width: 600
   :align: center

3. Field creation form will appear, where you should set field attributes

.. image:: pic_dateAndTime/dateModal.png
   :width: 600
   :align: center

4. Name - this is a name of a field
5. Role name - this is a role which will be assgined to fill this field
6. Placeholder - this text will be shown in the input box before anything is filled in (can be left empty, field name will be used instead)
7. Optional - this attribute specifies if this field is mandatory to fill
8. Time - this attribute specifies if time selector will be added to calendar
9. Search - this attribute specifies if this field should be eligible for mailbox page search
10. Min - minimal timestamp accepted by field (no limit is applied if left empty)
11. Max - maximal timestamp accepted by field (no limit is applied if left empty)

.. note:: Min and max fields only accept integers. They specify boundary dates offset in days. E.g. if min is 0 and max is 1, date interval from today to tomorrow will be available. If min is -1 and max is 0 then range from yesterday to today will be available. If min and max are both same, then only specified day will be available.

When all attributes are set, you can click Save button and field will be added. You can click field to see its properties and update them. Also you can delete the field in same menu.

.. image:: pic_dateAndTime/dateStructured.png
   :width: 600
   :align: center