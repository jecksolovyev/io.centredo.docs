===============
Account domains
===============

.. toctree::

.. role:: red

Account can have own domains and user, registered with emails on this domains. So called corporate user.
Account can add/verify/activate/deactivate domains. All unverified domains will be verified during 72 hours, if verify data was applied.
All verified domains pass through regular verification once a day. If domain was not verified it will be moved to INACTIVE status.

1. Add account domain
==========================================

Create/add new domain, if it is enabled for adding: domain should be resolvable and should not be assigned to another account.

.. list-table::
   :widths: 1 99
   :header-rows: 1

   * - Endpoint
     -
   * - Method
     - POST
   * - Request URL
     - ``/api/v1/account/{accountUuid}/domain``
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
     - .. literalinclude:: createAccountDomain.json

**Request example:**

.. code-block:: JSON

    [
        {
            "domain": "google.com"
        }
    ]


**Response example:**

.. code-block:: JSON

    {
        "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "accountUuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "domain": "google.com",
        "status": "UNVERIFIED"
    }

2. Verify account domain
==========================================

Request domain verification

.. list-table::
   :widths: 1 99
   :header-rows: 1

   * - Endpoint
     -
   * - Method
     - PATCH
   * - Request URL
     - ``/api/v1/account/{accountUuid}/domain/{domainUuid}/verify``
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
   * - domainUuid :red:`*`
     - Account domain UUID
   * - Body
     - .. literalinclude:: verifyAccountDomain.json

**Request example:**

.. code-block:: JSON

    [
        {
            "method": "DNS_CNAME_RECORD"
        }
    ]


**Response example:**

.. code-block:: JSON

    {
        "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "accountUuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "domain": "google.com",
        "status": "UNVERIFIED",
        "verifyInfo" : {
            "domain": "_whitedoc-verify",
            "value": "abc123"
        },
        "verifyMethod": "DNS_TXT_RECORD"
    }


3. Activate account domain
==========================================

Activate account domain

.. list-table::
   :widths: 1 99
   :header-rows: 1

   * - Endpoint
     -
   * - Method
     - PATCH
   * - Request URL
     - ``/api/v1/account/{accountUuid}/domain/{domainUuid}/activate``
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
   * - domainUuid :red:`*`
     - Account domain UUID

**Response example:**

If domain activated domain status will be `ACTIVE` in response.

.. code-block:: JSON

    {
        "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "accountUuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "domain": "google.com",
        "status": "ACTIVE",
        "verifyInfo" : {
            "domain": "_whitedoc-verify",
            "value": "abc123"
        },
        "verifyMethod": "DNS_TXT_RECORD"
    }

4. Deactivate account domain
==========================================

Activate account domain

.. list-table::
   :widths: 1 99
   :header-rows: 1

   * - Endpoint
     -
   * - Method
     - PATCH
   * - Request URL
     - ``/api/v1/account/{accountUuid}/domain/{domainUuid}/deactivate``
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
   * - domainUuid :red:`*`
     - Account domain UUID

**Response example:**

If domain deactivated domain status will be `INACTIVE` in response.

.. code-block:: JSON

    {
        "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "accountUuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "domain": "google.com",
        "status": "INACTIVE",
        "verifyInfo" : {
            "domain": "_whitedoc-verify",
            "value": "abc123"
        },
        "verifyMethod": "DNS_TXT_RECORD"
    }


5. Check account domain
==========================================

Check account domain ownership. Domain will be verified with verifyInfo & verifyMethod data. Check can only be performed once a minute.
Only unverified domains can be checked.

.. list-table::
   :widths: 1 99
   :header-rows: 1

   * - Endpoint
     -
   * - Method
     - PATCH
   * - Request URL
     - ``/api/v1/account/{accountUuid}/domain/{domainUuid}/check``
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
   * - domainUuid :red:`*`
     - Account domain UUID

**Response example:**

Response will be returned only if domain was unverified and verification not yet expired. Domains, which became verified, will have INACTIVE status.

.. code-block:: JSON

    {
        "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "accountUuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "domain": "google.com",
        "status": "INACTIVE",
        "verifyInfo" : {
            "domain": "_whitedoc-verify",
            "value": "abc123"
        },
        "verifyMethod": "DNS_TXT_RECORD"
    }


6. Delete account domain
==========================================

Permanently delete account domain

.. list-table::
   :widths: 1 99
   :header-rows: 1

   * - Endpoint
     -
   * - Method
     - DELETE
   * - Request URL
     - ``/api/v1/account/{accountUuid}/domain/{domainUuid}``
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
   * - domainUuid :red:`*`
     - Account domain UUID

**Response example:**

Response code **200** will be returned, if domain was removed


7. Search account domains
==========================================

Create/add new domain, if it is enabled for adding: domain should be resolvable and should not be assigned to another account.

.. list-table::
   :widths: 1 99
   :header-rows: 1

   * - Endpoint
     -
   * - Method
     - GET
   * - Request URL
     - ``/api/v1/account/{accountUuid}/domain``
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
   * - limit
     - Limit records, max is 1000, default 25
   * - offset
     - Offset records, default 0
   * - keyword
     - Part of domain name for search
   * - status
     - Domain status to search. Can be on of (UNVERIFIED, ACTIVE, INACTIVE) and virtual status VERIFIED, which means ACTIVE + INACTIVE

**Response example:**

.. code-block:: JSON

    {
      "data": [
        {
          "accountUuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "domain": "google.com",
          "status": "ACTIVE",
          "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "verifyInfo": {
            "domain": "_whitedoc-verify",
            "value": "abc123"
          },
          "verifyMethod": "DNS_TXT_RECORD"
        },
        {
          "accountUuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "domain": "facebook.com",
          "status": "ACTIVE",
          "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa5",
          "verifyInfo": {
            "domain": "_whitedoc-verify",
            "value": "abc124"
          },
          "verifyMethod": "DNS_TXT_RECORD"
        }
      ],
      "numberOfElements": 2,
      "sizeRequested": 25,
      "totalElements": 2
    }

8. Domain statuses
==========================================
- **UNVERIFIED**. Domain just listed in account's domain page, ownership of domain not confirmed. This is very first status of domain
- **ACTIVE**. Domain active and can be used to connect users to account
- **INACTIVE**. Domain verified (ownership was confirmed), but inactive, so it can't be used to connect users to account

9. Domain verify methods
==========================================
- **DNS_CNAME_RECORD**. With this method you should add CNAME record with name `verifyInfo.domain` to your domain. Example: _whitedoc-verify-abc123.google.com
- **DNS_TXT_RECORD**. With this method you should add TXT record with name `verifyInfo.domain` and content `verifyInfo.value` to your domain. Example: TXT _whitedoc-verify.google.com = abc123

