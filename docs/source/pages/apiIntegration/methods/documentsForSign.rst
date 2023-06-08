========================
Get document(s) for sign
========================

Customer can sign document if document has signature field inside assigned to the particular customer. Using this endpoint customer can get the list of the documents to sign. To get documents list for sign customer should send the following api request.

Request
=======

.. list-table::
   :widths: 10 90

   * - Method
     - POST
   * - URL
     - ``/api/v1/envelope/{envelopeUuid}/for-sign``
   * - Authorization
     - Bearer {token}
   * - content-type
     - application/json
   * - mailboxUuid
     - {uuid}
   * - envelopeUuid
     - {uuid}
   * - docIds
     - (array[string])

Depending on body of the request customer can get two type of the response:

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

.. list-table::
   :widths: 10 90

   * - documentId
     - id of the document
   * - pdf
     - PDF binary data
   * - pdfName
     - Name of the docuemnt
   * - signatureName
     - Name of the signature field
   * - xml
     - Document in .xml format
   * - xmlName
     - Structured document name