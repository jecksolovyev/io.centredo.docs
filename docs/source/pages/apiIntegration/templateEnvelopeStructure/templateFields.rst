Template dynamic fields
=======================

+--------------------------------------------------------------------------------------------------------+
|**Text field**                                                                                          |
+========================================================================================================+
|`<field type="text" name="name" placeholder="Placeholder text" roleId="UUID" multilines="true|false" />`|
+--------------------------------------------------------------------------------------------------------+

 - multilines - boolean, multiline or single line text, multiline should be textarea on UI, optional, default false

+------------------------------------------------------------------------------------------------------------------------------+
|**Number field**                                                                                                              |
+==============================================================================================================================+
|`<field type="number" name="name" placeholder="Placeholder text" roleId="UUID" precision="integer" min="float" max="float" />`|
+------------------------------------------------------------------------------------------------------------------------------+

 - min, max - default 'infinite'
 - precision - default 0

+---------------------------------------------------------------------------------------------------------+
|**Currency field**                                                                                       |
+=========================================================================================================+
|`<field type="money" name="name" placeholder="Placeholder text" roleId="UUID" min="float" max="float" />`|
+---------------------------------------------------------------------------------------------------------+

 - max - default 'infinite'
 - min - default 0
 - precision = 2 (always)

+---------------------------------------------------------------------------------------------------+
|**Date and time field**                                                                            |
+===================================================================================================+
|`<field type="datetime" name="name" placeholder="Placeholder text" roleId="UUID" time="boolean" />`|
+---------------------------------------------------------------------------------------------------+

 - format: IS8601
   accept both:
     - 2019-12-31T23:59:59+02:00
     - 2019-12-31T23:59:59Z
 - time - optional (send only if true)

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
|**Dictionary field**                                                                                                                                           |
+===============================================================================================================================================================+
|`<field type="select-dictionary" name="name" placeholder="Placeholder text" roleId="UUID" dictionaryUuid="UUID" columnUuid="UUID" allow-custom-value="true" />`|
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

 - "allow-custom-value" - allow choose custom value if not exists in dictionary
 - dictionaryUuid - dictionary uuid for dict|strict-dict subtypes, optional, required for dict|strict-dict
 - columnUuid - uuid of dictionary column, which value should be taken as text value

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
|**Lookup field**                                                                                                                                               |
+===============================================================================================================================================================+
|`<lookup name="name" relatedTo="dictionary field name" documentId="uuid of document" columnUuid="uuid of dictionary column" placeholder="text when not set" />`|
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

 - relatedTo - name of dictionary to which lookup will be connected
 - documentId - document id from which we take dictionary field
 - columnUuid - uuid of dictionary column, which value should be taken as text value

+------------------------------------------------------------------------------------+
|**Signature field**                                                                 |
+====================================================================================+
|`<field type="einksign" name="name" placeholder="Placeholder text" roleId="UUID" />`|
+------------------------------------------------------------------------------------+

Field value size limited up to 10kb. Field value - base64 encoded png image, size up to 300x300

+----------------------------------------------------------------------------------------------------+
|**Yes/No field**                                                                                    |
+====================================================================================================+
|`<field type="yesno" name="name" roleId="UUID" valueYes="Так, я згоден" valueNo="Ні, не згоден!" />`|
+----------------------------------------------------------------------------------------------------+

Values: exact value from template attribute valueYes or from template attribute valueNo.

+---------------------------------------------------------------------------------------+
|**Dynamic table**                                                                      |
+=======================================================================================+
|`<table name="tableName" class="table-stripped" iterable="true" roleId="UUID"></table>`|
+---------------------------------------------------------------------------------------+

.. code:: xml

    <table name="tableName" class="table-stripped" iterable="true" roleId="UUID">
       <thead>
            <tr>
                <th><div>Column name 1</div></th>
                <th><div>Column name 2</div></th>
            </tr>
        </thead>
        <tbody>
            <tr iterable="true" name="*">
                <field></field>
                <field></field>
            </tr>
        </tbody>
    </table>

+--------------------------------------------------------------------------------------------------------------------------------------------+
|**File field**                                                                                                                              |
+============================================================================================================================================+
|`<field type="attachment" name="fieldName" roleId="Uuid" placeholder="Some text" attachmentType="all | document | image | archive"></field>`|
+--------------------------------------------------------------------------------------------------------------------------------------------+

AttachmentType should be one of the presented above (all, document, image, archive). Supported document types:

1) All: .pdf, .doc, .docx, .xls, .xlsx, .xlsm, .xml, .dbf, .txt, .rtf, .csv, .xps, .eml, .msg, .emlx, .rpmsg, .png, .jpg, .jpeg, .tiff, .tif, .zip, .7z, .rar
2) File: .pdf, .doc, .docx, .xls, .xlsx, .xlsm, .xml, .dbf, .txt, .rtf, .csv, .xps, .eml, .msg, .emlx, .rpmsg
3) PDF document: .pdf
4) Image: .png, .jpg, .jpeg, .tiff, .tif
5) Archive: .zip, .7z, .rar

+----------------------------------------------------------------+
|**Duplicate field**                                             |
+================================================================+
|`<duplicate name="name1" relatedTo="name2" documentId="docId"/>`|
+----------------------------------------------------------------+

Duplicate is read-only field with the value of the related field.

- relatedTo - name of another field in envelope
- documentId - document id where the related is located

+----------------------------------------------------------------------------------+
|**Formula field**                                                                 |
+==================================================================================+
|`<formula name="name" precision="integer" trailingZeros="boolean">value</formula>`|
+----------------------------------------------------------------------------------+
 
Formula is read-only field with the value calculated using EXCEL operations

- precision - default 2
- trailingZeros - default true
- value is a formula with only one operation

SUPPORTED OPERATIONS: SUM,PRODUCT,COUNTA,MAX,MIN,DIVIDE,SUBTRACT

Example 1: SUM({field1},{doc2::field2}) where

- {field1} is a value of field1 from the same document
- {doc2::field2} is a value of field2 in document with id 'doc2'

Example 2: formula SUM({field1}) next to dynamic table where

- {field1} ia a field name from the table
- all values from all rows will summed up