=================
Template creation
=================

.. list-table::
   :widths: 10 90

   * - Method
     - POST
   * - URL
     - ``/api/v1/template``
   * - Authorization
     - Bearer {token}
   * - content-type
     - application/json
   * - mailboxUuid
     - {uuid}
   * - Body
     - "{""access"":""mailbox"",""categories"":[],""data"":""string""}"

**JSON Body**

.. code:: json

    {
    "access":"mailbox",
    "categories":[],
    "data":"<template>
	<info>
		<name>Template name</name>
		<description>Template description</description>
		<subject/>
		<message/>
		<expire/>
	</info>
	<documents>
		<document id=\"4a61f258-fd9d-406c-b47e-81c90d4e5c47\">
			<info>
				<title>New document</title>
			</info>
			<body>
				<div class=\"editor-div\">Structured document</div>
				<div class=\"editor-div\">This data depends on text in your documents and dynamic fields which was added to this document
					<field type=\"text\" name=\"text field\" roleId=\"b811f2b6-1656-42aa-9420-a9b8addb0246\" placeholder=\"text field\"/>
				</div>
			</body>
		</document>
	</documents>
	<flow>
		<roles>
			<role id=\"23f20eec-adad-4325-b553-1bde4be29198\" title=\"Sender\" type=\"sender\" order=\"0\"/>
			<role id=\"b811f2b6-1656-42aa-9420-a9b8addb0246\" title=\"Assignee\" type=\"assignee\" order=\"1\"/>
		</roles>
	</flow>
    </template>"
    }

Depending on your needs, you can add different types of fields `template fields <../fields/templateFields.html>`__

**RESPONSE**

.. code:: json

    {
    "uuid":"56cacd6a-ffe7-4b77-9c0c-f928d9a18cb5",
    "name":"Template name",
    "description":"Template description",
    "data":"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
    <template>
        <info>
            <name>Template name</name>
            <description>Template description</description>
            <subject></subject>
            <message></message>
            <expire/>
        </info>
        <documents>
            <document id=\"4a61f258-fd9d-406c-b47e-81c90d4e5c47\">
                <info>
                    <title>New document</title>
                </info>
                <body>
                    <div class=\"editor-div\">Structured document</div>
                    <div class=\"editor-div\">This data depends on text in your documents and dynamic fields which was added to this document
                        <field type=\"text\" name=\"text field\" roleId=\"b811f2b6-1656-42aa-9420-a9b8addb0246\" placeholder=\"text field\"/>
                    </div>
                </body>
            </document>
        </documents>
        <flow>
            <roles>
                <role id=\"23f20eec-adad-4325-b553-1bde4be29198\" title=\"Sender\" order=\"0\" type=\"sender\"/>
                <role id=\"b811f2b6-1656-42aa-9420-a9b8addb0246\" title=\"Assignee\" order=\"1\" type=\"assignee\"/>
            </roles>
        </flow>
    </template>",
    "version":"ab0d11cb-ebdd-42bd-a581-ddca1bb9b585",
    "dataCreatedAt":"2020-12-02T06:30:44.543Z",
    "dataModifiedAt":"2020-12-02T06:30:44.543Z",
    "access":"mailbox",
    "archive":false,
    "categories":[],
    "createdAt":"2020-12-02T06:30:44.503Z",
    "modifiedAt":"2020-12-02T06:30:44.503Z"
    }