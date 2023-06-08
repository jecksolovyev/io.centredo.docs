=============
Authorization
=============

.. list-table::
   :widths: 10 90

   * - Method
     - POST
   * - URL
     - ``/api/login``
   * - content-type
     - application/json
   * - Body
     - {"login":"email","password":"password"}

Authorization token should return in response (expires in 12 hours).

**Response example (JSON):**

.. code:: json

  {"token":"b16b61fc-4706-4c90-a57d-fe0cd0dcd2f0"}

**Response status codes**

.. list-table::
   :widths: 10 90
   :header-rows: 1

   * - Code
     - Description
   * - 200
     - Success
   * - 201
     - Created
   * - 401
     - Not authorized
   * - 403
     - Forbidden
   * - 404
     - Not found