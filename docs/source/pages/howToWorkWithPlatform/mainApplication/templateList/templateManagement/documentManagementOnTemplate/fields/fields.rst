.. _fields:

==============
Dynamic fields
==============

Dynamic fields allow you to create various inputs for different data types in the documents. There are several ways to add them to template:

Text cursor method
==================

This method is only available for structured documents. To create a field, click where you want it to be placed in the document. When flashing text cursor appears, click on a field icon in the Fields tab of template editor menu. Field will be placed on the spot of a cursor.

Drag & drop method
==================

This method works with all types of documents. As it is clear from the name, you can drag & drop fields (press button on pick, drag while button is pressed, release button to drop) from the Fields tab of the template editor menu on the spot in the document where you want it to be placed. Preview of the field will be shown near pointer while dragging it. Note that in structured documents position of field will be approximate to drop point and will be placed in the closest place where text cursor can be placed. This method suits best to PDF documents, as position of the field will be exactly as preview shows in such documents.

'Sticky fields' method
======================

This method is similar to drag & drop, but works in 2 clicks instead of 1. Click (without holding the button pressed) on the field in the fields menu and its preview will 'stick' to mouse pointer. Hover pointer with attached field to desired spot in the document and place it with 2nd click. Note that in structured documents it will be place to the spot approximately, similar to drag & drop method. Also, if text cursor is visible on screen, this method will not activate (field will be placed on cursor after click). This method suits best for PDF documents and when working on a tablet with touch screen (drag & drop is not supported on touch devices, so this is the only available method to place fields on PDF documents on a tablet without additional input devices).

.. note:: If you`ve picked up a wrong field or just changed your mind on adding it, you can clear it from mouse pointer with ESC, backspace or delete buttons. Alternatively, you can click outside of all documents.

**List of dynamic field types**

.. toctree::

   text/text.rst
   number/number.rst
   currency/currency.rst
   dateAndTime/dateAndTime.rst
   dictionary/dictionary.rst
   file/file.rst
   table/table.rst
   signature/signature.rst
   checkbox/checkbox.rst
   yesNo/yesNo.rst
   lookup/lookup.rst
   eds/eds.rst
   duplicate/duplicate.rst
   formula/Formula.rst
   autonumber/autonumber.rst