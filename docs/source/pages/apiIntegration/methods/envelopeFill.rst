=============
Fill envelope
=============

To fill envelope you should provide data to field which assigned to him by request below.

.. list-table::
   :widths: 10 90

   * - Method
     - PUT
   * - URL
     - ``/api/v1/envelope/mailbox/{uuid}/{action}``
   * - Authorization
     - Bearer {token}
   * - content-type
     - application/json
   * - Body
     - "{""data"": ""string""}"

sendEnvelopeDTO
===============

.. code-block:: JSON

    {"data":"
    <envelope templateUuid=\"500afafd-711e-471a-a18f-24a89cd4ede3\" status=\"SENT\" templateVersion=\"143a2a4b-325e-4c05-a4c1-52f44e21b745\">
        <state>
            <message/>
        </state>
        <documents>
            <document id=\"ef247568-559a-4ec1-9ecc-6b44c9fb8215\">
                <field name=\"TEST template 2\">12312</field>
            </document>
            <document id=\"43d47e65-011d-4890-9eaf-c1c6d860b3b2\"/>
        </documents>
    </envelope>","uuid":"3e8e9c87-09a1-4b5f-8f1a-2ea3049ed34e"}

All provided data will be filled to appropriated fields and when next recipient open this envelope this data will be shown.