=======================================
Upload attachment or external documents
=======================================

.. list-table::
   :widths: 10 90

   * - Method
     - POST
   * - URL
     - ``/api/v1/envelope/attachment``
   * - Authorization
     - Bearer {token}
   * - content-type
     - application/json
   * - mailboxUuid
     - {uuid}
   * - Body
     - "string($binary)"

For add file to document, you should upload this file in binary format to our system by request above. In response on this request you will get data which should be used in envelope for add this file in document in the appropriate field.

**RESPONSE**

.. code:: json

    {
      "attachmentId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "filename": "string",
      "filesize": 0
    }