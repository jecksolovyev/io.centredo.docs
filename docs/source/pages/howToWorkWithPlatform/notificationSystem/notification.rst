===================
Notification system
===================

.. toctree::

Notifications system using for provide customers information about different activities in accounts/mailboxes where customers has access:

* New envelope
* Envelope reached final status(complete, rejected, expired)
* New invites to account/mailbox
* Users accepted or declined your invites to account/mailbox
* Role completed actions on the particular step in the envelope
* Domains
* Integration
* Dictionary

To watch at notifications you should click on bell in the upper right corner. By default bell without notification will be grey,
when user get new notification bell will be shown with badge. Badge shows quantity of the notifications you have, if you have more than 9  notifications
in badge shown "9+". After you click on bell will be open window with notifications, sorted by date.

**All notifications are divided into three types:**

* For users
    * New invites to account/mailbox
    * Domain verified or verification expired
* For account
    * User declined invites to account/mailbox
    * Integration notification(error with outbox/inbox file)
* For mailbox
    * New envelope
    * Envelope reached final status(complete, rejected, expired)
    * Dictionary uploaded or not on platform

Each notification consists of an icon+link+text+time of receipt.

All customers who have an access to same account/mailbox observe all notifications for these elements. If one of the
customers who has access clicks on a notification he will be redirected to the corresponding page of our application and
this notification changes state to read and will be hidden for all of the customers.

**All redirects depends on notification type:**

* User notification(invites to account/mailbox) - redirect to user profile on invites tab
* Account notification(users declined your invite to account/mailbox) - redirect to admin panel on users tab
* Account notification(user accept your invite to account/mailbox) - redirect to admin panel on users tab with filtered data for this user
* Mailbox notification(new envelope or envelope reached final status) - redirect to correspond envelope page
* Dictionary notification(uploaded or not on platform) - redirect to dictionary page
* Domain notification(domain verified or verification expired) - redirect to admin panel on account setting on domain tab


**The Notification tab**

You can turn notifications on or off on the Notifications tab in the User Profile menu.
There are divided into four logically structured blocks:

* Account
* Mailbox
* Envelope
* Dictionary

and by two criteria:

* by e-mail
* in the system

By default, all notifications are turned on.

You can uncheck the box next to any type of notification and they will not be sent to you by e-mail or will not arrive in the system (bell in the upper right corner).











