==============
Search mailbox
==============

.. list-table::
   :widths: 10 90

   * - Method
     - GET
   * - URL
     - ``/api/v1/mailbox/search``
   * - Authorization
     - Bearer {token}
   * - content-type
     - application/json
   * - mailboxUuid
     - {uuid}
   * - q
     - text, email or UUID

For search mailbox you can use mailbox alias, user email address or contact name.