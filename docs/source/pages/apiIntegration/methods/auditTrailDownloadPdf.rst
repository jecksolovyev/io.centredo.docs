====================================
Export envelope audit trail PDF file
====================================

.. list-table::
   :widths: 10 90

   * - Method
     - GET
   * - URL
     - ``api/v1/audittrail/pdf/{uuid}``
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
   * - 401
     - Not authorized
   * - 403
     - No access to mailbox
   * - 404
     - Envelope not found