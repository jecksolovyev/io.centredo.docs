.. _scenario-management:

======================
How to manage scenario
======================

.. toctree::

To manage scenarion you have to follow scenatio page which you can find at the left side menu with respective icon and tooltip or follow the directly.

You can create, edit, clone and delete scenarios.

How to create scenario?
=======================

To create scenario you have to open scenario page and click on button "New scenario". 
After you clicked on button above you have to fill in required data before you save scenario:

1. Name

2. Description

3. Steps of the scenario (steps also include required data, such as step name, source and destination, conversion rule)

As soon as you filled in required data you can save template.

How to configure particular step?
=================================

You can configure steps of the scenario and each step will run new one envelope.

To configure the first step of scenario you have to click on "+" button near "Scenario steps" title. After that new form will appear and you will be able to:

1. Set the name of the scenario step.

2. Fill the destination with template uuid and template version uuid of template you need.
    
.. warning:: **The latest template version uuid automatically applies in the field after tempalte uuid entered**

3. You have to enter xslt conversion rule which will create envelope after run. How to create xslt conversion rule you can find by the following link.

4. Click on "Save" icon in the right top corner of the step.

To create second, third and the rest of the following steps you have to do similar steps as above, but you will need to fill new field "source". Source it's two field with tempalte uuid and template version uuid of the previous step of the scenario.

How to edit scenario?
=====================

If you need to edit scenario you have to do the following:

1. Open scenario list

2. Click on three dots in the right corner of the scenario you need to edit

3. Click on "Edit" option from the list

4. Add your changes if needed and save scenario

How to edit scenario step?
==========================

If you need edit scenario step you have to click on "edit" button (pencil icon) on the scenario step you have to edit, add changes and click on "Save" button in the top right corner of the edited scenario step. 
After that click on "Save" sceanrio button.

How to clone scenario?
======================

If you need to clone any scenario you have to do the following:

1. Open scenario list

2. Click on three dots in the right corner of the scenario you need to edit

3. Click on "Clone" option from the list

If scenario cloned successfuly you will get respective message and will see cloned scenario in the list.

How to delete sceanrio?
=======================

If you need to delete any scenario you have to do the following:

1. Open scenario list

2. Click on three dots in the right corner of the scenario you need to edit

3. Click on "Delete" option from the list

If scenario deletes successfuly you will get respective message and scenario disapper from the list.
