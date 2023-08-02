===============
Duplicate field
===============

Duplicate is a field which allows you to create a static duplicate of other field.

.. warning:: You will not be able to delete parent field of a duplicate untill the duplicate field is removed.

How to add duplicate field to the document
==========================================

1. To add field to structured document, place text cursor where you want field to be added and click its button (alternatively it can be placed via drag & drop)

.. image:: pic_duplicate/duplicateIcon.png
   :width: 600
   :align: center

2. To add field to PDF document, drag & drop it to desired place in the document. It can be moved around and resized by lower left corner afterwards

.. image:: pic_duplicate/duplicatePDF.png
   :width: 600
   :align: center

3. Field creation form will appear, where you should set field attributes

.. image:: pic_duplicate/duplicateModal.png
   :width: 600
   :align: center

4. Name - this is a name of a field
5. Document - a document where parent field is placed
6. Duplicate of - field which will be duplicated

.. note:: If duplicate is placed inside of a dynamic table, only fields from the same table (or outside of all tables) will be available for duplication.

When all attributes are set, you can click Save button and field will be added. You can click field to see its properties and update them. Also you can delete the field in same menu.

.. image:: pic_duplicate/duplicateStructured.png
   :width: 600
   :align: center