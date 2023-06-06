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

1. Template path. This property allow you configure template storing location across your mailbox
2. Template name and description. These fields are mandatory to save a template
3. Template access level. Property which allows you set access level of the template according to your needs. Detailed about access level :ref:`here <templateAccessLevel>`
4. Subject and message of envelopes created from this template. If set on template level, it's impossible to change them on envelope level later

.. note:: Advanced subject properties can be opened with properties button in Subject field. From ther you can configure dynamic envelope auto-subject for each envelope which will include data from specified dynamics field in the envelope.

5. Envelope expiration property allows you to configure expiration period of envelopes created from template. If set on template level, it's impossible to change it on envelope level later
6. Envelope delegation property denies or allows delegation of the actions with envelope. If set on template level, it's impossible to change it on envelope level later
7. Envelope sending and sharing emails property denies or allows possibility to attach documents to envelope completion email or possibility to share envelope. If set on template level, it's impossible to change it on envelope level later
8. Template cover. Preview of the template that will be visible mailboxes which have access to template. Can use custom inage or dynamicly generate preview of first page of the template