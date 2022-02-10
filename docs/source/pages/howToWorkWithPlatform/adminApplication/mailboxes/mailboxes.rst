=========
Mailboxes
=========

.. toctree::

   delete_mailbox_behaviour.rst

---------

Mailboxes page it's a part of admin panel interface. 
This page allows:

1. Manage current mailbox(es);

2. Create new mailbox(es);

3. Remove user(s) from mailbox(es);

4. Delete mailbox(es);

To open mailboxes page navigate to https://staging.whitedoc.space/admin/mailboxes

.. image:: pic_mailboxes/mailboxesMainView.png
   :width: 600
   :align: center

Add new mailbox
===============

1. Click on the button "Add new mailbox"

.. image:: pic_mailboxes/mailboxesAddNewMailbox.png
   :width: 600
   :align: center

2. Modal window of the mailbox creation opens. Enter a name of the mailbox

.. image:: pic_mailboxes/mailboxesEnterMailboxName.png
   :width: 600
   :align: center

3. Click on the button "Create" (the state of the "Create" button will change after name enters)

.. image:: pic_mailboxes/mailboxesCreateMailbox.png
   :width: 600
   :align: center

4. After successful mailbox creation will show message in the right corner of the page and mailbox will show in the list of mailboxes

.. image:: pic_mailboxes/mailboxesSuccessfulCreation.png
   :width: 600
   :align: center

Check users assigned to mailbox
===============================

To check the users which assigned to the particular mailbox click on the link with number in the column "Users". After this action redirect will happen to the page Users https://staging.whitedoc.space/admin/users with perdefined filter by Mailbox.

Edit mailbox
============

Edition interface allows update name of the mailbox, add and remove aliases of the mailbox, copy the mailboxs UUID, unassign all users who has permissions to the mailbox and delete mailbox.

To open edition form of the mailbox, just click on the settings icon

.. image:: pic_mailboxes/mailboxesOpenEditionForm.png
   :width: 600
   :align: center

Edit mailbox name
=================

Name field has length validation:

1. Min value - 1 symbol
2. Max value - 255 symbols

To edit name just focus the name, change the name and click on "Save changes" button

.. image:: pic_mailboxes/mailboxesNameUpdate.png
   :width: 600
   :align: center

After successful edition of the mailbox the notification message will show at the right corner of the page

.. image:: pic_mailboxes/mailboxesChangesSaved.png
   :width: 600
   :align: center

Copy mailbox UUID
=================

To copy the mailbox UUID click on the copying icon. After successful copying the notification message will be shown at the right corener of the page.

.. image:: pic_mailboxes/mailboxesCopyingUuid.png
   :width: 600
   :align: center

Add/Remove alias(es) for mailbox
================================

For the particular mailbox aliases couldn't be duplicated only unique values accepts. 

To add alias(es) to the mailbox

1. Click on the aliases area of the page 

.. image:: pic_mailboxes/mailboxesFocusOnAliasArea.png
   :width: 600
   :align: center

2. Enter the alias and press "Enter", "." or "," button on keyboard to add alias to the list, after that click on "Save changes" button

.. image:: pic_mailboxes/mailboxesTypingAliasName.png
   :width: 600
   :align: center

.. image:: pic_mailboxes/mailboxesFinishTypingOfTheAlias.png
   :width: 600
   :align: center

To remove alias(es) from the mailbox, click on remove icon of the alias and click on "Save changes" button

.. image:: pic_mailboxes/mailboxesDeletionButton.png
   :width: 600
   :align: center

After successful edition of the mailbox the notification message will show at the right corner of the page

.. image:: pic_mailboxes/mailboxesChangesSaved.png
   :width: 600
   :align: center

Danger zone
===========

To unassign all users from mailbox or delete mailbox switch to "Danger Zone" tab by click on "Danger Zone" heading

.. image:: pic_mailboxes/mailboxesDangerZone.png
   :width: 600
   :align: center

.. image:: pic_mailboxes/mailboxesDangerZoneView.png
   :width: 600
   :align: center

Unassgin users from mailbox
===========================

1. To unassign all users from mailbox (remove all permissions to the particular mailbox from the all users who has it except the user who do the action) click on the button "Deactivate"

2. Confirm the decision and users will be unassigned



Delete mailbox
==============

1. To delete mailbox click on "Delete" button

2. Enter the mailbox in upper case to the field in the modal window which opens after click on "Delete" button

3. Confirm the decision and mailbox will be deleted

.. warning:: **Please note!** `Behaviour of mailbox after deletion <delete_mailbox_behaviour.html>`_

.. include:: delete_mailbox_behaviour.rst



How to generate report by mailboxes?
====================================

.. toctree::

If you want to get xlsx file with report by mailboxes you have to do the following:

1. Open platform

2. Got to Admin Panel

3. Open tab 'Mailboxes' and select all necessary records

4. Click on button with document icon (button called "Generate report")

5. After click you will see the message that report will be send to you email after generation

6. Follow to email address

7. Open email you got

8. Click on button "Download"

Now you can open the file on your computer
