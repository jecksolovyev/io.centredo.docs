===================================
Send envelope without authorisation
===================================

User is able to send envelope without authorisation. To use this functionality user has to do get special link (create link as authorised user or receive link from somebody).

Flow of the initiation envelope without authorisation
=====================================================

1. Create template with public access, filled in envelope subject and all roles except sender
2. Generate special link, which unathorised users can use
3. Follow the link without authorisation
4. Fill in all required fields assigned to sender role
5. Send envelope and follow the instructions
6. If user already registered on platform Log in if not leave email address to Send envelope

How to create share template link?
==================================

1. Create a template
2. Fill in envelope subject and fill in all roles in the flow with mailboxes
3. Set template access level to public

.. note:: If template uses dictionary access level of each dictionary used in template should be public or official access level.

4. Save template
5. Follow to template list
6. Open particular template menu and select option "Get link"

.. image:: pic_sendEnvelopeAsGuest/getLinkOption.png
   :width: 400
   :align: center

7. Generate new share template link

.. image:: pic_sendEnvelopeAsGuest/getLinkModal.png
   :width: 400
   :align: center

8. Copy link and send it to anybody who wants to initiate envelope with shared template

.. note:: In same window you can find Embed code - it can be used to integrate envelope creation process to 3rd party services via iframe. Please note that you can add redirect url to the embed code, this page will open in a new browser tab after envelope is sent.

You are able to revoke current link and code, just click on "Revoke link" button. This action removes possibility to create envelopes using shared template link and code. Also you are able to create new template shared link and code by click on "Generate new link". Link and cdoe are unique every time and revoked ones can not be recovered.

How to send envelope without authorisation (for guests)?
========================================================

To send envelope without authorisation user has to have template shared link or embedded iframe.

1. Follow the template shared link (or to the iframe). User observes limited functionality of envelope functionality (fill in fields, sign documents)
2. Fill in all required fields and signatures (button "Edit" changes to "Send")

.. image:: pic_sendEnvelopeAsGuest/simpleEnvView.png
   :width: 400
   :align: center

3. Click on "Send" button
4. Enter your email (user with this email shouldn't be created)

.. image:: pic_sendEnvelopeAsGuest/enterEmail.png
   :width: 400
   :align: center

5. Confirm envelope send. Success page will be displayed as soon as envelope will be sent according to the flow

.. image:: pic_sendEnvelopeAsGuest/successPage.png
   :width: 400
   :align: center

How to send envelope without authorisation (for registered users)?
==================================================================

To send envelope without authorisation user has to have template shared link or embedded iframe.

1. Follow the template shared link
2. Fill in all required fields and signatures (button "Edit" changes to "Send")

.. image:: pic_sendEnvelopeAsGuest/simpleEnvView.png
   :width: 400
   :align: center

3. Click on "Send" button.

.. note:: If you are already logged in in other browser tab and have autodeposit mailbox enabled, it will automatically be used and envelope will be sent after this step. If you do not have autodeposit mailbox enabled, you will be prompted to select one of your mailboxes.

.. image:: pic_sendEnvelopeAsGuest/chooseMailbox.png
   :width: 400
   :align: center

4. Enter your email (user with this email should be registered on platform)

.. image:: pic_sendEnvelopeAsGuest/enterEmail.png
   :width: 400
   :align: center

5. Enter valid credentials and sign in

.. image:: pic_sendEnvelopeAsGuest/authForm.png
   :width: 400
   :align: center

.. note:: If you do not have autodeposit mailbox enabled, you will be prompted to select one.

.. image:: pic_sendEnvelopeAsGuest/chooseMailbox.png
   :width: 400
   :align: center

6. Success page will be displayed as soon as envelope will be sent according to the flow

.. image:: pic_sendEnvelopeAsGuest/successPage.png
   :width: 400
   :align: center