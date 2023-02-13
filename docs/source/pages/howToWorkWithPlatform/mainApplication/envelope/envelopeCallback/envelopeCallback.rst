.. _envelopeCallback:

==================
Envelope callbacks
==================

.. toctree::

Creating a callback record
==========================

You can set up callbacks for envelopes in order to recieve envelope notifications outside of our platform and email. This is done via API. To create new callback record You should use next POST request:

URL: {{platform address}}/api/v1/envelope/callback/add

Headers: authorization: Bearer {{token}}, content-type: application/json, mailbox: {{mailboxUUID}}

Body:

{
    "filter": {},
    "url": "URL where callbacks are sent",
    "retries": 10,
    "timeout": 60000,
    "successCode": 200,
    "login": "string",
    "password": "string"
}

Retrieving list of callbacks
============================

To see list of callback records You need to run following GET request:

URL: {{platform address}}/api/v1/envelope/callback/list

Headers: authorization: Bearer {{token}}, mailbox: {{mailboxUUID}}

Deleting a callback
===================

To remove a callback record You need to run following DEL request:

URL: {{platform address}}/api/v1/envelope/callback/{{callbackUUID}}/remove

Headers: authorization: Bearer {{token}}, mailbox: {{mailboxUUID}}