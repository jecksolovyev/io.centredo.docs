=========================
Create audit trail record
=========================

.. list-table::
   :widths: 10 90

   * - Method
     - PUT
   * - URL
     - ``api/v1/audittrail/envelope/{uuid}``
   * - content-type
     - application/json

**Response status codes**

.. list-table::
   :widths: 10 90
   :header-rows: 1

   * - Code
     - Description
   * - 200
     - Success
   * - 400
     - Bad request
   * - 401
     - Not authorized
   * - 403
     - No access to mailbox
   * - 404
     - Envelope not found
   * - 422
     - Invalid request value