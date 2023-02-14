=======================================
Upload attachment or external documents
=======================================

.. toctree::

.. csv-table::
  :file: uploadAttachment.csv
  :widths:  10, 41

For add file to document, customer should upload this file in binary format to our system by request above. In response on this request customer got data which he should use in envelope for add this file in document in the appropriate field.

**RESPONSE**

.. code:: json

    {
      "attachmentId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "filename": "string",
      "filesize": 0
    }