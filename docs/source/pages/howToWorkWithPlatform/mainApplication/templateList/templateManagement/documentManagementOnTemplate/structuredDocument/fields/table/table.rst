===========
Table Field
===========

.. toctree::

Table field allows user to add dynamic data to the document. Also it allows to prepare table of exact needed size for participant of the envelope processing flow.

Create Table Field
===================

1. Navigate to /template/form/create

2. Drag and drop Table field to the document

3. Form should appear

4. Fill the name of the field (should be unique per document)

5. Select the owner of the table

6. If you want to add column with row numbers enable show column number attribute

7. Fill the quantity of the columns of the table

8. Click save

Fill the Table with fields
==========================

1. Add table to the document

2. Drag and drop needed fields to the table cells, set and save field properties. Next fields can be added to the Table: Text, Number, Currency, Date and time, E-ink signature, Dictionary, Lookup and Duplicate fields. Adding new table inside other table is not supported

Edit Table Field properties
===========================

1. Navigate to /template/form/create

2. Click on the table field in the document

3. Edit field form should appear on the right side

4. Click on "Delete" button will delete table and close edit form

5. Click on "Cancel" will close edit form

6. You can change name of the field and role to whom table is assigned

7. Click on "Save" will save all the changes you made and close edit form

.. note::
   If you want to truncate some columns of the table in it's initial state you can click on according column, enable "Initially hidden" attribute in column properties and click "Save". Note that this is supported only for columns which have optional dynamic fields in them. Columns with static text, non-optional fields or empty cells can not be hidden. On the envelope view user will be able to show such columns from the menu on the right end of the table (only columns which have optional fields assigned for viewing user will be presented). If hidden column fields will not be filled during document processing these columns will be excluded from the final version of the document.

Edit Table field content
========================

1. Add table to the document

2. Click on the header of a column and type the name different from from defaul "Column name" value

3. Name of the column has been updated

4. At the header you're able to add or remove column of the table using "+" and "-" buttons, if you press "-" of the last column table will be removed

5. You also can change vertical text alignment in the header right click menu for each column

Fill table field as owner
=========================

Only owner of the table has management buttons to add or remove rows "+" and "-" which located at the left side of the table field.

.. image:: pic_table/tableFieldEnvelope.png
   :width: 600
   :align: center

Each added row will be added with same fields which were added to the first row.

.. image:: pic_table/tableFieldEnvelopeAddedRows.png
   :width: 600
   :align: center

When table owner added table rows and filled all mandatory fields he can send the document according to the flow. As an owner of the table he can be one of the participants of the processing flow.

The rest of the participants only can edit fields in the table assigned to them.