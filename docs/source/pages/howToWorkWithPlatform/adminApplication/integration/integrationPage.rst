================
Integration page
================

Each customers who want to turn on integration can do that on  `integration page </admin/integrations/list>`_.
On this page customer can turned integration for all mailboxes in same account one by one. When customer open this page
and he has mailbox all field will be pre-filled(except: "Notify by email")

.. image:: pic_integrationPage/integrationPage_1.png
   :width: 1000
   :align: center

Manage integration(2)
=====================

In manage integration block (2) customer can customize integration properties:

#. mailbox for integration
#. connection protocol
#. email address

If customer has more than one mailbox in this account he can change mailbox for integration in first field selection.
In second field selection customer will provide connection protocol, depends on this selection will be changed connection details(3)
block.
In the third field customer can provide email address where will be send all notification which related to integrations. Also this email will be use in second default rule.

Connection details(3)
=====================

Data in connection details (3) block is automatically generated for connection protocols FTPS and SFTP except password, it will be generated after save button click, credential from this block should be used for connect to ftp server. Customer can copy each parameter by clicking on copy button.
Customer can't change any parameters except password for FTPS and SFTP. To change password customer should click on reset button, after that we will generate new password.

For AS2 protocol only Self URL and Self certificate will be created, the rest of the fields need to be filled in.

Default rules(4)
================

#. Get incoming envelope on the Website and put the copy to the FTPS, SFTP or AS2 (depends on protocol you chose)
#. Get incoming envelope on the Website and send notification email
#. Autoreject incoming envelopes

If incoming documents doesn't fit to any conversion rules or customer doesn't create any rules to documents will be apply one of the default rules.
Customer can select only one of three default rules. When customer select 3 rule he can provide reject reason and all incoming document will be rejected with this reason.

Conversion rules list(5)
========================

By default conversion rule list is empty. To create new rule just click on "Add new rule" button, after that you will be redirected to conversion rule creation form.
All new rules will be shown on this list. User can turn on/turn off each rules from this list.
Each existed conversion rules can be updated, deleted or cloned, for that customer should open this rule by click on rule name.

When customer finish setting integration and he want to turn on integration he should move toggle (1) to the right position and click on Save(7) button.


