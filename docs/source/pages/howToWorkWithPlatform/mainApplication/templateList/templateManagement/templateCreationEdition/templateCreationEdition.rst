===================
What is a template?
===================

Template is an entity which can contain one or more documents inside and is used to create envelopes.

How to create template?
=======================

1. Open template list
2. Click on "New template" button
3. Fill in template subject and description in "Template" tab of right side menu
4. Configure processing flow of the template. More info on this topic can be found :ref:`here <processing-flow>`
5. Fill document with desired content and add new documents if needed
6. Click on the "Save" button to save template

How to edit template?
=====================

1. Open template list
2. Click on template options icon near template you want to edit
3. Select "Edit" option from the list to open template editor
4. Now you can make you changes. To save you changes click on button "Save" on the template editor page

.. _templatePropertyTemplate:

Template properties
===================

On template configuration page you can set some template properties, such as template name, description, access level and more. On screenshot below you can find template properties description

.. image:: pic_templateCreationEdition/templateProperties.png
   :width: 300
   :align: center

1. Version info - appears after template is saved. Here you can find UUIDs of template, it's current version and owner mailbox
2. Template path - this property allows you to configure template storing location across your mailboxes
3. Template name and description - these fields are mandatory to save a template
4. Template Access - property which allows you to set access level of the template according to your needs. You can read more about this functionality :ref:`here <templateAccessLevel>`
5. Envelope Properties - subject and message of envelopes created from a template. If set on template level, it's impossible to change it on envelope level later

.. note:: Advanced subject properties can be opened with properties button in Subject field. You can configure dynamic envelope auto-subject for each envelope which will include data from specified dynamic fields in the envelope. More info on this topic can be found :ref:`here <autoSubject>`.

6. Envelope expiry day - allows you to configure expiration period of envelopes created from template. If set on template level, it's impossible to change it on envelope level later
7. Envelope delegation - allows or denies delegation of the envelope. If set on template level, it's impossible to change it on envelope level later
8. Envelope sending and sharing - this property allows or denies possibility to attach documents to the envelope completion email notification or possibility to share the envelope. If set on template level, it's impossible to change it on envelope level later
9. Template cover - preview of the template that will be visible mailboxes which have access to template. Can use custom image or dynamically generate preview of first page of the template
10. Configure envelope archive files - this feature allows you to configure an envelope archive that can be downloaded upon completion of the envelope. You can read more about this functionality :ref:`here <archiveConfiguration>`