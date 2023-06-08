=========================
Sign document(s) with EDS
=========================

You can sign document if document has signature field inside assigned to the particular user. Using this endpoint you can sign document(s) with EDS.

Request
=======

.. list-table::
   :widths: 10 90

   * - Method
     - PUT
   * - URL
     - ``/api/v1/envelope/{envelopeUuid}/sign``
   * - Authorization
     - Bearer {token}
   * - content-type
     - application/json
   * - mailboxUuid
     - {uuid}
   * - Body
     - (array[documentId,signatureName,array with signature data,data (binary (base64) data with signature by which we sign document (part of signatures array),source (type of source we send (available sources: binary, text), (part of signatures array)),stamp (boolean)]))

Request structure example
=========================

.. code-block:: JSON

    [
        {
            "documentId": "string",
            "signatureName": "string",
            "signatures": [
                {
                    "data": "string",
                    "source": "binary",
                    "stamp": true
                }
            ]
        }
    ]

Response
========

If data in request is valid in response you will see Status code: **200 OK**.