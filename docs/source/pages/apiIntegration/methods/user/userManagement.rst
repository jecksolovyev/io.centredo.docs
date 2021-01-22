===============
User/Profile
===============

.. toctree::

.. role:: red

User can be created via registration or as a corporate user by account admin.
Corporate users cannot delete themselves and cannot create own accounts.

1. Create corporate user
==========================================

Create new corporate user in domain which has to be verified and activated.

.. list-table::
   :widths: 1 99
   :header-rows: 1

   * - Endpoint
     -
   * - Method
     - POST
   * - Request URL
     - ``/api/v1/user/domain``
   * - **Headers**
     -
   * - Authorization :red:`*`
     - Bearer TOKEN
   * - Content-Type
     - application/json
   * - **Request**
     -
   * - accountUuid :red:`*`
     - Target account UUID
   * - Body
     - .. code-block:: JSON

        {
          "domainUuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "email": "string",
          "firstName": "string",
          "lastName": "string"
        }

**Response example:**

.. code-block:: JSON

    {
      "createdAt": "yyyy-MM-dd'T'HH:mm:ss.SSSXXX",
      "email": "string",
      "firstName": "string",
      "lastName": "string",
      "status": "VALIDATING",
      "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }

2. Delete corporate users
==========================================

Account admin can delete many corporate users at once.
In case of exception, no user will be deleted.

.. list-table::
   :widths: 1 99
   :header-rows: 1

   * - Endpoint
     -
   * - Method
     - DELETE
   * - Request URL
     - ``/api/v1/user/domain``
   * - **Headers**
     -
   * - Authorization :red:`*`
     - Bearer TOKEN
   * - Content-Type
     - application/json
   * - **Request**
     -
   * - checkMessage :red:`*`
     - Proof message
   * - Body :red:`*`
     - .. code-block:: JSON

        [
          {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
          }
        ]
