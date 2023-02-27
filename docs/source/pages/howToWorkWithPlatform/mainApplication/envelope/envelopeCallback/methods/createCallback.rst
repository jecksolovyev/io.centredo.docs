===============
Create callback
===============

.. toctree::

+---------------+--------------------------------------------------------------+
|   **URL**     |                                                              |
+---------------+--------------------------------------------------------------+
|    Method     |                         POST                                 |
+---------------+--------------------------------------------------------------+
|  request URL  |          ``/api/v1/envelope/callback/add``                   |
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

**REQUEST BODY**

.. code:: json

   {
    "filter": {
        "label": ["string"],
        "status": ["COMPLETED"],
        "subject": "string",
        "receiveDateFrom": "2023-02-16T12:34:26.606Z",
        "receiveDateTo": "2023-02-16T12:34:26.606Z",
        "expireDateFrom": "2023-02-16T12:34:26.606Z",
        "expireDateTo": "2023-02-16T12:34:26.606Z",
        "template": ["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
        "sender": ["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
        "scope": ["inbox"]
    },
    "url": "string",
    "retries": 10,
    "timeout": 60000,
    "successCode": 200,
    "login": "string",
    "password": "string"
  }

Request body parameters described below:

+-----------------+------------------------------------------------------------------------------------------------------+
| filter          | Is an object with filter data according to which callbacks will be triggered                         |
+-----------------+------------------------------------------------------------------------------------------------------+
| label           | Filter envelopes by label which assigned to envelope                                                 |
+-----------------+------------------------------------------------------------------------------------------------------+
| status          | Filter envelopes by status. Allowed statuses for callbacks are WAITING, COMPLETED, CANCELLED, EXPIRED|
+-----------------+------------------------------------------------------------------------------------------------------+
| subject         | Filter envelopes by respective subject of envelope. Filter works according to the contain rule.      |
|                 | It means if we apply filter by subject "agreement" all envelopes with word "agreement" will be added |
|                 | to callback queue and callback will be sent.                                                         |
+-----------------+------------------------------------------------------------------------------------------------------+
| receiveDateFrom | Filter envelopes by receive date FROM specified date and time                                        |
+-----------------+------------------------------------------------------------------------------------------------------+
| receiveDateTo   | Filter envelopes by receive date TO specified date and time                                          |
+-----------------+------------------------------------------------------------------------------------------------------+
| expireDateFrom  | Filter envelopes by envelope expire date FROM specified date and time                                |
+-----------------+------------------------------------------------------------------------------------------------------+
| expireDateTo    | Filter envelopes by envelope expire date TO specified date and time                                  |
+-----------------+------------------------------------------------------------------------------------------------------+
| template        | Filter envelopes specific template (template from which envelope created).                           |
|                 | Allowed values are template UUIDs                                                                    |
+-----------------+------------------------------------------------------------------------------------------------------+
| sender          | Filter envelopes by envelope sender. Allowed values are senders UUIDs                                |
+-----------------+------------------------------------------------------------------------------------------------------+
| scope           | Filter envelopes by direction of the email. Allowed values inbox and outbox                          |
+-----------------+------------------------------------------------------------------------------------------------------+
| url             | Parameter defines URL where callback will be sent                                                    |
+-----------------+------------------------------------------------------------------------------------------------------+
| retries         | Parameter defines quantity of callback send retires. Retries could be applied if URL unreachable     |
|                 | or successCode received from URL is different from expected. Allowed values from 0 to 10.            |
|                 | If 0 value set in callback it means that system tires to send callback once and will not retry       |
+-----------------+------------------------------------------------------------------------------------------------------+
| timeout         | Parameter defines timeout in milliseconds which system wait for response with successCode.           |
|                 | If timeout reached retries procedure starts (if configured). Allowed values from 100 to 60000        |
+-----------------+------------------------------------------------------------------------------------------------------+
| successCode     | Parameter defines status code which system wait for successfully sent callback. If status code       |
|                 | received from URL is different from required retries procedure will be initiated (if configured)     |
+-----------------+------------------------------------------------------------------------------------------------------+
| login           | Parameter defines login of the Basic auth                                                            |
|                 | (If URL is reachable only with Basic auth this parameter has to be defined)                          |
+-----------------+------------------------------------------------------------------------------------------------------+
| password        | Parameter defines password of the Basic auth                                                         |
|                 | (If URL is reachable only with Basic auth this parameter has to be defined)                          |
+-----------------+------------------------------------------------------------------------------------------------------+


**RESPONSE**

In response you get 201 status code (in case of successful callback creation) and JSON data of the callback

**Response example (JSON):**

.. code:: json

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


