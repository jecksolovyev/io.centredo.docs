==============
List callbacks
==============

.. toctree::

+---------------+--------------------------------------------------------------+
|   **URL**     |                                                              |
+---------------+--------------------------------------------------------------+
|    Method     |                         GET                                  |
+---------------+--------------------------------------------------------------+
|  request URL  |          ``/api/v1/envelope/callback/list``                  |
+---------------+--------------------------------------------------------------+
| **Headers**   |                                                              |
+---------------+--------------------------------------------------------------+
| content-type  |                    application/json                          |
+---------------+--------------------------------------------------------------+
| authorization |``Bearer {token}`` where {token} is authorization token which |
|               |user received after successful authorization on platform      |
+---------------+--------------------------------------------------------------+
| mailbox       |   UUID of mailbox to which you configured callbacks          |
+---------------+--------------------------------------------------------------+

**RESPONSE**

In response you get 200 status code (in case of successful callback list retrieving) and JSON data with callbacks

**Response example (JSON):**

.. code:: json

  [
    {
        "id": "f8c97405-9185-4998-a3c0-2c4d0edaf43b",
        "filter": {
            "label": ["string"],
            "status": ["COMPLETED"],
            "subject": "string",
            "receiveDateFrom": null,
            "receiveDateTo": null,
            "expireDateFrom": null,
            "expireDateTo": null,
            "template": ["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
            "sender": ["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
            "scope": ["inbox"]
        },
        "url": "string",
        "retries": 10,
        "timeout": 60000,
        "successCode": 200,
        "authType": "BASIC"
    }
  ]

