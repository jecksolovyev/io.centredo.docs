===================================
Download envelope documents archive
===================================

Everyone who has access to envelope can download it. You can download full envelope or specific document from this envelope with following request:

.. list-table::
   :widths: 10 90

   * - Method
     - POST
   * - URL
     - ``/api/v1/envelope/{envelopeUuid}/zip``
   * - Authorization
     - Bearer {token}
   * - content-type
     - application/json
   * - mailboxUuid
     - {uuid}
   * - envelopeUuid
     - {uuid}
   * - documentId
     - {uuid},{uuid}
   * - onlyPrimaryFiles
     - boolean

Depending on query parameter you can control what will be included in archive:

1. Send request without query parameter - download full envelope (all documents which contain envelope)
2. Send request with documentID in query parameter - download only document which specified in query parameter
3. Send request with onlyPrimaryFiles in query parameter - download only primary files in archive (pdf and xml documents and signatures for internal document and original document and signatures for external document)

Zip archive with documents will be sent in response.