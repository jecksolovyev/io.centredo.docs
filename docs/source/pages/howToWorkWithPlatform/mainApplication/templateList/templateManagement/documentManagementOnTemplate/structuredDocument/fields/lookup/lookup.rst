============
Lookup Field
============

.. toctree::

Lookup field automatically pull value from field dictionary field from record.
Lookup field available only when template has one or more dictionaries without allow custom value attribute.

Create Lookup Field
===================

1. Navigate to https://staging.whitedoc.space/template/form/editor

2. Drag and drop lookup-field to the document

3. Form should appear

4. Fill the name of the field (Should be unique per document)

5. Fill the placeholder for this field (Not mandatory, if you won't fill this field, name will be used as placeholder).

6. Choose document from list of documents with dictionaries without allow custom value attribute.

7. Choose to with dictionary field lookup field will be applied by setting related to attribute.

8. Choose which column (from dictionary column) should use lookup field to set value.

9. Click save.

10. Field added

Edit Lookup Field
=================

1. Navigate to https://staging.whitedoc.space/template/form/editor

2. Click on the lookup field in the document

3. Edit field form should appear on the right side

4. Click on "Delete" button will delete field and close edit form

5. Click on Cancel will close edit form

6. You can change parameters the same way as described in "Create Lookup Field"

7. Click on "Save" will Save all the changes you mad and close edit form

Lookup Field Template
=====================

Lookup field at document can use dictionary field from any document in template if they are not inside table-field.

Lookup Inside Table-field
=========================

Lookup field inside table field can use only dictionary field from this table or dictionary field from any document in template.
Lookup field inside table can't use dictionary from other table-field.

Missing Column At Lookup Field
==============================

When lookup field use dictionary column that was deleted - he became invalid and template became invalid too.
To fix lookup field need to select new column.

No Access To Dictionary
=======================

When dictionary field has no access to dictionary template became invalid and field became invalid and lookup field that was related to this dictionary field became invalid too.
To fix lookup field need to select new dictionary at dictionary field to which lookup was attached and set new column at every lookup field that was related to this dictionary field.

Disabled Lookup Field
=====================

Lookup field is disabled when template hasn't have any dictionary field.

Deleting Dictionary Field
=========================

Deleting dictionary field isn't available when dictionary has lookup field that is related to him. Need to delete lookup field or set them related to other dictionary field first.

Lookup Field Envelope
=====================

Lookup field disabled on envelope. For fill in lookup field need select dictionary value, when dictionary value selected all lookup fields which related to this dictionary field will be automatically fill. User can’t fill in lookup fields if he don’t have access to dictionary which used in dictionary field. User can fill in all lookup fields on envelope and save this envelope as a draft and send later. If somebody change dictionary(update records, delete column or delete dictionary) before user send envelope draft with lookup fields, user will observe error message with information about dictionary changes. If dictionary was deleted all lookup fields which related to this dictionary field will be highlighted by red color.
