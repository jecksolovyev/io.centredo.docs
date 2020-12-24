==================
Envelope Structure
==================

The structure of the envelope may change depending on what operation is performed with envelope.

#. Fill/Send (request)
#. Read (response)


Fill/Send
=========
When customer send or fill envelope in request body he should provide all information about envelope and fill all field which assigned to him.

.. code::

    {"data":"
    <envelope templateUuid=\"500afafd-711e-471a-a18f-24a89cd4ede3\" status=\"DRAFT\" templateVersion=\"143a2a4b-325e-4c05-a4c1-52f44e21b745\">
        <state>
            <message/>
        </state>
        <info>
            <subject>TEST ENVELOPE</subject>
            <message>TEST ENVELOPE</message>
            <expire afterDays=\"30\" notifyIn=\"1\"/>
        </info>
        <flow>
            <roles>
                <role id=\"fd8cb669-db1d-41e1-8f6c-2ad3f8fa981a\" mailboxUuid=\"dc8ebcaa-2699-416d-afda-2c72d4b65622\"/>
                <role id=\"3f29b3a8-3baa-4218-80b1-5a0bb85af247\" mailboxUuid=\"1186bd77-08af-4e75-ba3d-5874d7cf51fa\"/>
                <role id=\"348c486d-2901-4ecd-be0c-9a7e6c2ae2a2\" mailboxUuid=\"2db6de67-c1a2-48b3-974b-064bea704512\"/>
            </roles>
        </flow>
        <documents>
            <document id=\"ef247568-559a-4ec1-9ecc-6b44c9fb8215\">
                <field name=\"TEST template 1\" value=\"Тестовое значение\">Тестовое значение</field>
            </document>
            <document id=\"43d47e65-011d-4890-9eaf-c1c6d860b3b2\">
                <field name=\"990f11c1-48de-4ac8-8479-a5989d5f08dc\" value=\"1ee585cf-106e-421f-8621-ffe1a89b05ec\">test.txt</field>
            </document>
        </documents>
    </envelope>"}


Envelope consists of two blocks:

1. Envelope information block.


.. code:: json

    {"envelope":{"uuid":"b7754a70-dcf3-4f99-a0fa-7816611a4832",
    "receivedAt":"2020-12-11T12:47:50.991Z",
    "labels":[],"total":2,
    "completed":1}}

.. csv-table::
  :file: envelopeStructure.csv
  :widths:  10, 10


2. Data block

.. code::

    "data":"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
    <envelope templateUuid=\"500afafd-711e-471a-a18f-24a89cd4ede3\" templateVersion=\"63151ef6-05df-47a1-83b1-b3c747c3214b\" created=\"2020-12-11T12:47:50.929Z\">
        <state>
            <status>SENT</status>
            <date>2020-12-11T12:47:51.203Z</date>
            <roleId>fd8cb669-db1d-41e1-8f6c-2ad3f8fa981a</roleId>
        </state>
        <info>
            <subject>TEST ENVELOPE</subject>
            <message>TEST ENVELOPE</message>
            <expire afterDays=\"30\" afterDateTime=\"2021-01-10T12:47:51.171Z\" notifyIn=\"1\"/>
        </info>
        <documents>
            <document id=\"ef247568-559a-4ec1-9ecc-6b44c9fb8215\">
                <field name=\"TEST template 1\" value=\"TEST ENVELOPE\">TEST ENVELOPE</field>
            </document>
            <document id=\"1bb895fc-ab36-47e8-802e-5b39fc02db64\">
			<field name=\"a1c7eaad-dc3a-4332-a17d-c82bffeea499\" value=\"27509b61-baa2-4a4e-9909-4d2f32597410\">test.txt</field>
		</document>
        </documents>
        <flow>
            <roles>
                <role id=\"fd8cb669-db1d-41e1-8f6c-2ad3f8fa981a\" mailboxUuid=\"dc8ebcaa-2699-416d-afda-2c72d4b65622\" active=\"false\" completed=\"true\"/>
                <role id=\"3f29b3a8-3baa-4218-80b1-5a0bb85af247\" mailboxUuid=\"3b570b34-335c-4ec2-9307-9a9c9b2900a0\" active=\"true\" completed=\"false\"/>
            </roles>
        </flow>
    </envelope>"

.. csv-table::
  :file: envelopeStructureData.csv
  :widths:  10, 10
