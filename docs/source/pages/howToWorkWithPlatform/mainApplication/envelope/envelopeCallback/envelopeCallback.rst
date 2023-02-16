.. _envelopeCallback:

==================
Envelope callbacks
==================

Envelope callback is functionality which allows to receive notification to respective URL in case of envelope appearance in mailbox and according to configured filters.
You can set up callbacks for mailbox in order to receive envelope notifications outside of our platform. This is done via API.

If callback configured, link to receive callbacks reachable and envelope is triggered callback received than system send callback to respective link with following JSON data.

.. toctree::

    simpleCallbackExample.rst

**JSON Callback data**

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

**Description of the JSON data**

+-----------------+------------------------------------------------------------------------------------------------------+
| uuid            | Envelope UUID which triggered callback on platform                                                   |
+-----------------+------------------------------------------------------------------------------------------------------+
| label           | List of label UUIDs which assigned to particular envelope                                            |
+-----------------+------------------------------------------------------------------------------------------------------+
| status          | Status of the envelope. Most expected statuses are WAITING, COMPLETED, EXPIRED, CANCELLED            |
+-----------------+------------------------------------------------------------------------------------------------------+
| subject         | Envelope subject                                                                                     |
+-----------------+------------------------------------------------------------------------------------------------------+
| receiveDate     | Envelope receiving date. Retrieves in UNIX time                                                      |
+-----------------+------------------------------------------------------------------------------------------------------+
| expireDate      | Expiration date of the envelope. Retrieves in UNIX time                                              |
+-----------------+------------------------------------------------------------------------------------------------------+
| template        | UUID of the template from which envelope has been created                                            |
+-----------------+------------------------------------------------------------------------------------------------------+
| sender          | Envelope sender UUID. Mailbox initiated envelope processing flow                                     |
+-----------------+------------------------------------------------------------------------------------------------------+



**List of API methods**

.. toctree::

    methods/createCallback.rst
    methods/listCallbacks.rst
    methods/deleteCallback.rst

Create a callback record
========================

To create new callback record You should use next request:

+-----------+-----------------------------------+---------------------------------------------------------------------------------------------+
|**Method** |       **Request URL**             |                                            **Description**                                  |
+===========+===================================+=============================================================================================+
| POST      | ``/api/v1/envelope/callback/add`` | `Callback creation method and description with examples <methods/createCallback.html>`__    |
+-----------+-----------------------------------+---------------------------------------------------------------------------------------------+


Retrieve list of callbacks
==========================

To see list of callback records for mailbox You should use next request:

+-----------+-----------------------------------+---------------------------------------------------------------------------------------------+
|**Method** |       **Request URL**             |                                            **Description**                                  |
+===========+===================================+=============================================================================================+
| GET       | ``/api/v1/envelope/callback/list``| `View callbacks related to particular mailbox <methods/listCallbacks.html>`__               |
+-----------+-----------------------------------+---------------------------------------------------------------------------------------------+

Delete a callback
=================

To delete a callback record You should use next request:

+-----------+--------------------------------------------------------+---------------------------------------------------------------------------------------------+
|**Method** |       **Request URL**                                  |                                            **Description**                                  |
+===========+========================================================+=============================================================================================+
| DELETE    | ``/api/v1/envelope/callback/{{callbackUUID}}/remove``  | `Delete callback from specific mailbox <methods/deleteCallback.html>`__                     |
+-----------+--------------------------------------------------------+---------------------------------------------------------------------------------------------+


