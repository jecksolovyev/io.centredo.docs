**Send Envelope**
=================

.. toctree::


.. csv-table::
  :file: evnelopeSend.csv
  :widths:  10, 41

For create and send envelope customer should know based on what template will be created envelope.

**sendEnvelopeDto**
===================

.. code-block:: JSON

    {
	"data":"<envelope>
	templateUuid=\"56cacd6a-ffe7-4b77-9c0c-f928d9a18cb5\" 
	status=\"DRAFT\" 
	templateVersion=\"ab0d11cb-ebdd-42bd-a581-ddca1bb9b585\">
	<state>
		<message/>
	</state>
	<info>
		<subject>Envelope subject</subject>
		<message>Envelope message</message>
		<expire afterDays=\"30\" notifyIn=\"1\"/>
	</info>
	<flow>
		<roles>
			<role id=\"23f20eec-adad-4325-b553-1bde4be29198\" mailboxUuid=\"9baec31c-e940-4894-b6d1-52033e1af66e\"/>
			<role id=\"b811f2b6-1656-42aa-9420-a9b8addb0246\" mailboxUuid=\"42c95245-30c1-46ef-bd5b-a9a111deec10\"/>
		</roles>
	</flow>
	<documents>
		<document id=\"4a61f258-fd9d-406c-b47e-81c90d4e5c47\">
			<field name=\"date field\">2020-12-02T10:20:10.846Z</field>
		</document>
	</documents>
    </envelope>"
	}

**RESPONSE**
In response we got envelope uuid:


.. code-block:: JSON

    {"uuid":"89499ba2-287d-404c-87b0-342dc5b01b6a"}

Customer can check envelope status by this uuid.