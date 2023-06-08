=====================
Check envelope status
=====================

.. list-table::
   :widths: 10 90

   * - Method
     - GET
   * - URL
     - ``/api/v1/mailbox/{uuid}``
   * - Authorization
     - Bearer {token}
   * - content-type
     - application/json
   * - mailboxUuid
     - {uuid}
   * - q
     - query parameter
   * - archived
     - boolean (default false)
   * - expireDatePeriod
     - ‘expirationDate’ period 
   * - label
     - {uuid},{uuid}
   * - limit
     - integer (default 25)
   * - offset
     - integer (number of envelopes to skip, default 0)
   * - receiveDatePeriod
     - ‘receiveDate’ period
   * - scope
     - inbox,outbox
   * - sender
     - {uuid}
   * - sort
     - asc/desc
   * - status
     - DRAFT,WAITING,COMPLETED,EXPIRED,CANCELLED
   * - subject
     - string
   * - template
     - {uuid},{uuid}

In response you will get short information about envelopes from this mailbox which match to filter criteria. For more information on this request was used filter by template.

**Request URL example**

``https://api.platform_address_here/api/v1/mailbox/837bc65e-4818-48f5-a933-2d00b24b6e12?receiveDatePeriod=&expireDatePeriod=&params=%5Bobject%20Object%5D&scope=outbox&archived=false&period=null&sender=&subject=&template=e5705211-51d1-4c34-9429-c537038b3c44&expireperiod=null&label=&limit=20&offset=0&sort=desc``

**Response example:**
Status code: 200 OK

.. code:: json

    {
   "totalElements":3,
   "sizeRequested":20,
   "numberOfElements":3,
   "data":[
      {
         "envelopeUuid":"e8d5a176-d75e-4d9d-ad19-c66ef300a4a1",
         "subject":"test 111",
         "message":"test 111",
         "archived":false,
         "sentByMe":false,
         "createdAt":"2020-12-08T13:35:29.228Z",
         "seenAt":null,
         "expiredAfter":"2021-01-07T13:35:29.330Z",
         "notifyBeforeExpire":false,
         "status":"SENT",
         "mailboxUUID":"837bc65e-4818-48f5-a933-2d00b24b6e12",
         "mailboxName":"testMailbox",
         "total":3,
         "completed":1,
         "labels":[

         ],
         "templateUuid":"e5705211-51d1-4c34-9429-c537038b3c44",
         "templateName":"Job Offer"
      },
      {
         "envelopeUuid":"24d0c0b1-0ad5-4122-9834-bcab5e8b3ea5",
         "subject":"test 111",
         "message":"test 111",
         "archived":false,
         "sentByMe":false,
         "createdAt":"2020-12-08T13:29:00.646Z",
         "seenAt":"2020-12-08T13:29:01.154Z",
         "expiredAfter":"2021-01-07T13:29:00.745Z",
         "notifyBeforeExpire":false,
         "status":"SENT",
         "mailboxUUID":"837bc65e-4818-48f5-a933-2d00b24b6e12",
         "mailboxName":"testMailbox",
         "total":3,
         "completed":1,
         "labels":[

         ],
         "templateUuid":"e5705211-51d1-4c34-9429-c537038b3c44",
         "templateName":"Job Offer"
      },
      {
         "envelopeUuid":"94544d72-301c-4cda-a7fa-e2b7ec4fec7a",
         "subject":"Test",
         "message":"Test",
         "archived":false,
         "sentByMe":false,
         "createdAt":"2020-12-07T16:23:40.133Z",
         "seenAt":"2020-12-07T16:23:41.312Z",
         "expiredAfter":"2021-01-06T16:23:40.244Z",
         "notifyBeforeExpire":false,
         "status":"COMPLETED",
         "mailboxUUID":"837bc65e-4818-48f5-a933-2d00b24b6e12",
         "mailboxName":"testMailbox",
         "total":3,
         "completed":3,
         "labels":[

         ],
         "templateUuid":"e5705211-51d1-4c34-9429-c537038b3c44",
         "templateName":"Job Offer"
      }
   ]
   }

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
     - Forbidden
   * - 404
     - Not found

**Request for full envelope with template**

.. list-table::
   :widths: 10 90

   * - Method
     - GET
   * - URL
     - ``/api/v1/mailbox/{uuid}``
   * - Authorization
     - Bearer {token}
   * - content-type
     - application/json
   * - mailboxUuid
     - {uuid}
   * - uuid
     - {uuid}

In response you will get full envelope and template.

**Response example:**
Status code: 200 OK

.. code:: json

    {
      "envelope": {
        "completed": 0,
        "data": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
                <envelope templateUuid=\"6a9147f2-ec26-41f6-b694-7dd33eb3a659\"
                templateVersion=\"dd598d80-8856-401c-a45c-06503c0d8a19\"
                created=\"2020-12-09T20:11:39.593Z\">
                <state><status>SENT</status><date>2020-12-09T20:11:39.774Z</date>"
        "labels": [
          "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        ],
        "receivedAt": "string",
        "total": 0,
        "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      },
      "template": {
        "access": "account",
        "archive": true,
        "categories": [
          0
        ],
        "createdAt": "string",
        "data": "string",
        "dataCreatedAt": "string",
        "dataModifiedAt": "string",
        "description": "string",
        "modifiedAt": "string",
        "name": "string",
        "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "version": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    }

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
     - Forbidden
   * - 404
     - Not found