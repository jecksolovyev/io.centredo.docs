==================
Envelope Structure
==================

.. code:: xml

    {"envelope":{"uuid":"b7754a70-dcf3-4f99-a0fa-7816611a4832","data":"

    <?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
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
        </documents>
        <flow>
            <roles>
                <role id=\"fd8cb669-db1d-41e1-8f6c-2ad3f8fa981a\" mailboxUuid=\"dc8ebcaa-2699-416d-afda-2c72d4b65622\" active=\"false\" completed=\"true\"/>
                <role id=\"3f29b3a8-3baa-4218-80b1-5a0bb85af247\" mailboxUuid=\"3b570b34-335c-4ec2-9307-9a9c9b2900a0\" active=\"true\" completed=\"false\"/>
            </roles>
        </flow>
    </envelope>","receivedAt":"2020-12-11T12:47:50.991Z","labels":[],"total":2,"completed":1}


The envelope consists of two blocks:

1. Envelope information block.

.. code:: json

    {"envelope":{"uuid":"b7754a70-dcf3-4f99-a0fa-7816611a4832",
    "receivedAt":"2020-12-11T12:47:50.991Z",
    "labels":[],"total":2,
    "completed":1
    }


2. Data block

.. csv-table::
  :file: envelopeStructureData.csv
  :widths:  10, 10