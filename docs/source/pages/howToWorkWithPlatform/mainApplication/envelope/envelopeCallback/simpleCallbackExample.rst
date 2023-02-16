=======================
Simple callback example
=======================

**To configure and receive callbacks follow the instruction bellow**

To create callbacks you have to achieve following requirements:

1. You have to be a user of platform with owner access to at least one mailbox
2. You have to have URL which will receive callbacks
3. You have to be familiar with API (as callback interface doesn't have UI)

**If you reached three points above you can start configuring you callback**

1. Create callback using following data. This callback will be triggered on each envelope receive with following statuses WAITING, COMPLETED, EXPIRED, CANCELLED

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
    "filter": {},
    "url": "URL which can receive callbacks",
    "retries": 5,
    "timeout": 10000,
    "successCode": 200,
    "login": "",
    "password": ""
  }

2. Send at least one envelope to mailbox where callback was created
3. Follow to URL you defined in callback and wait for callback data
4. As soon as your URL received callback you will see the following JSON data (data of UUIDs, status, labels, subject, dates, template and sender will be according to envelope you received)

.. code:: json

  {
    "uuid": "74acfb70-78e9-4ca5-ac73-054c72402c0a",
    "label": ["string"],
    "status": "string",
    "subject": "string",
    "receiveDate": 1676039226765,
    "expireDate": 1678631226504,
    "template": "ebeb302b-597e-4b47-9de2-5ad3a33e4385",
    "sender": "fdfde267-6558-40a9-93fd-e59529baef36"
  }
