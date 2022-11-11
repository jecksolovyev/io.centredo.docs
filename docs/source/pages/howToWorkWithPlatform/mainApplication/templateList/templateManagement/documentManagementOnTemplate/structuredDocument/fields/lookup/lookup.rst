============
Lookup Field
============

.. toctree::

Lookup field automatically pulls value from related dictionary.

Create Lookup Field
===================

1. Navigate to https://staging.whitedoc.space/template/form/editor

2. Drag and drop lookup field to the document (note that at least one dictionary field should be added to the document for you to be able to add lookup fields).

3. Next window should appear:

.. image:: pic_lookup/LookupCreationForm.png
   :width: 600
   :align: center

4. Fill the "Name" attribute of the field (should be unique per document).

5. Fill the "Placeholder" attribute for this field (not mandatory, if you won't fill this field, name will be used as placeholder).

6. Select "Optional" attribute status for this field. If it is enabled value in the field can be left empty (note that if same value for related dictionary is enabled control will be locked in enabled state).

7. Select "Allow custom values" attribute status for this field. If it is enabled value in the field can be modified by hand instead of using only predefined values from dictionary.

8. Select "Search" attribute status for this field. If it is enabled value in the field can be used for envelope search in mailbox.

9. Choose "Document" from the list of documents with dictionaries.

10. Choose dictionary from "Related to" list of dictionaries for this field to refer to.

11. Choose column from "Column name" list of columns for this field to refer to.

12. Click on "Save" will add new lookup field.

Edit Lookup Field
=================

1. Navigate to https://staging.whitedoc.space/template/form/editor

2. Click on the lookup field in the document.

3. Edit field form should appear on the right side:

.. image:: pic_lookup/LookupEditionForm.png
   :width: 600
   :align: center

4. Click on "Delete" button will delete field and close edit form.

5. Click on "Cancel" will close edit form.

6. You can change parameters the same way as described in "Create Lookup Field".

7. Click on "Save" will Save all the changes you made and close edit form.

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
