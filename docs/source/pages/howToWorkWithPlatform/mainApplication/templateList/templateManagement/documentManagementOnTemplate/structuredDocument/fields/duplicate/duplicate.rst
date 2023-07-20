===============
Duplicate Field
===============

.. toctree::

Duplicate field copies the value of the parent field.
Duplicate field is available only when the template contains at least one field to which you can assign a duplicate.
Allowed fields for duplicating: text, number, currency, date and time, dictionary, yes/no.

Create Duplicate Field
======================

1. Open template for edition and open document for edition
2. Drag and drop duplicate-field to the document
3. Form should appear
4. Fill the name of the field (Should be unique per document)
5. Choose document from list of documents with allowed fields for duplicating
6. Choose which field should use duplicate field to set value
7. Click save
8. Field added

Edit Duplicate Field
====================

1. Open template for edition and open document for edition
2. Click on the duplicate field in the document
3. Edit field form should appear on the right side
4. Click on "Delete" button will delete field and close edit form
5. Click on Cancel will close edit form
6. You can change parameters the same way as described in "Create Duplicate Field"
7. Click on "Save" will Save all the changes you mad and close edit form

Duplicate Field Template
========================

Duplicate field at document can use any allowed field from any document in template if they are not inside table-field.

Duplicate Inside Table-field
============================

Duplicate field inside table field can use only allowed field from this table or any allowed field from any document in template.
Duplicate field inside table can't use fields from other table-field.

Disabled Duplicate Field
========================

Duplicate field is disabled when template hasn't have any allowed field.

Deleting Duplicate Field
=========================

You can delete Duplicate Field without limits.

But deleting allowed field (text, number, currency, date and time, dictionary, yes/no) isn't available when the field has duplicate field that is related to him. Need to delete duplicate field first.

Duplicate Field in Envelope
===========================

Duplicate field is disabled on envelope. 
To fill in duplicate field you have to fill value in parent field. All duplicates fields which related to this parent field will be automatically fill.

If parent of the duplicate field is optional you can don't fill in parent field and in this case duplicate field will be emty too.