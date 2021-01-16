========================
Get document(s) for sign
========================

.. toctree::

Customer can sign document if document has signature field inside assigned to the particular customer. Using this endpoint customer can get
the list of the documents to sign.

To get documents list for sign customer should send the following api request.

Request
=======

.. csv-table::
  :file: documentsForSign.csv
  :widths:  10, 41

Depends on body of the request customer can get two type of the response:

1. Send request with empty array in body - get all documents from the envleope with signature related to particular customer
2. Send request with particular documentID in body - get particular document for sign

In response we get an array with information about documents for sign.

Response
========

Status code: **200 OK**

.. code-block:: JSON

    [
        {
            "documentId": "string",
            "pdf": "string",
            "pdfName": "string",
            "signatureName": "string",
            "xml": "string",
            "xmlName": "string"
        }
    ]


Description of the response data:

.. csv-table::
  :file: documentForSignResponse.csv
  :widths:  10, 41