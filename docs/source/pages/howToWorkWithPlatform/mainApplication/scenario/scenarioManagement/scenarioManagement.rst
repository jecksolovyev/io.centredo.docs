.. _scenario-management:

======================
How to manage scenario
======================

Scenario includes the following information: name, description, uuid and steps of the scenario. Steps include name, source and destination (where source and destination include template uuid and template version uuid) and conversion rule.

.. toctree::

How to create scenario?
=======================

To create scenario you have to click on button "New scenario" on the scenario list. And after that fill in required details.

.. note:: First step of the scenario does not contain source. It contains only destination.

Scenario creation form presented below:

.. image:: ../pic_scenario/scenario-create.png
   :width: 600
   :align: center

**1 - Scenario main info form**

|    1.1 Scenario name. (required)
|    1.2 Scenario description. (required)
|    1.3 Scenario uuid(always disabled, with copy icon btn)
|    1.4 Access level select. (required)
|    1.5 Cancel button (go to list)
|    1.6 Save button (save scenario form changes). (disabled if scenario form invalid or at least one step not saved now)

**2 - Step expanded panel with step form**

|    2.1 Scenario step name. (required)
|    2.2 Scenario destination template uuid. (required)
|    2.3 Scenario destination template version. (required)
|    2.4 Scenario step conversation rule. (required)
|    2.5 Scenario step condition. (if true display field for condition rule). (required).
|    2.6 Scenario step form actions.

**3 - Scenario step add button**  

How to configure particular step?
=================================

1. Click on "+" button near "Scenario steps" title. After that new form will appear
2. Set the name of the scenario step
3. Fill the destination with template uuid and template version uuid of template you need    
4. You have to enter xslt conversion rule which will create envelope after run. How to create xslt conversion rule you can find by the following link
5. Click on "Save" icon in the right top corner of the step

.. note:: The latest template version uuid automatically applies in the field after template uuid entered

To create second, third and the rest of the following steps you have to do similar steps as above, but you will need to fill new field "source". Source it's two field with template uuid and template version uuid of the previous step of the scenario.

How to edit scenario?
=====================

1. Open scenario list
2. Click on three dots in the right corner of the scenario you need to edit
3. Click on "Edit" option from the list
4. Add your changes if needed and save scenario

**Description of the scenario edit form below**

.. image:: ../pic_scenario/scenario-edit.png
   :width: 600
   :align: center

| 1. Condition for step
| 2. Condition xslt field.(if true display field for condition rule). (required)
| 3. Step form action buttons
|     3.1 Save step button. (if edit step mode. disabled if step form invalid)
|     3.2 Edit step button. (if no edit step mode)
|     3.3 Delete step button. (first step cannot delete)
| 4. Step form action buttons
|     4.1 Delete scenario button
|     4.2 Clone scenario button
|     4.3 Save scenario button

How to edit scenario step?
==========================

If you need edit scenario step you have to click on "edit" button (pencil icon) on the scenario step you have to edit, add changes and click on "Save" button in the top right corner of the edited scenario step. After that click on "Save" scenario button.

How to clone scenario?
======================

1. Open scenario list
2. Click on three dots in the right corner of the scenario you need to edit
3. Click on "Clone" option from the list
4. If scenario cloned successfully you will get respective message and will see cloned scenario in the list

How to delete scenario?
=======================

1. Open scenario list
2. Click on three dots in the right corner of the scenario you need to edit
3. Click on "Delete" option from the list
4. If scenario deletes successfully you will get respective message and scenario disappear from the list

What is option send envelope immediately after step run?
=========================================================

If you want to send envelope after step run, mark the respective checkbox.

.. note:: To send envelope you have to fill all required fields in the envelope for Sender role and you have to set all recipient and signer mailboxes or emails in the flow

If you any required data is missed on the step (at the conversion rule) you will get an error while saving scenario.


What is condition and how to use it?
====================================

On the platform presented two types of the conditions:

1. Condition based on some fields, to create different branches of the script, for example, if in the act of completed work the amount of the service is more than 1000, then give the opportunity to launch one branch of the script, if more then another
2. Condition that create several envelopes based on the values in the source. But at the same time, if the values are "Yes", then create envelope (s) 1, and if the value is "No", then create envelope(s)

Condition is optional and may or may not be in the request or could be null.

**Additional logic**

If after checking the execution "condition" = false, then check the next steps, if all steps are false, then run the step in order in which condition = null. If there are no conditions, then we run the next steps with the null parameter condition and respective source value. If several steps meet the conditions, then the user in the envelope will display several buttons for starting different steps (in the rest, several steps will be received in the response).

Simple condition
================

Condition is a XSLT map which will be applied to the source envelope of the step. A simple condition has to return "true" or "false" in xml format:

.. code:: xml

    <result>
        true
    </result>

A condition XSLT example:

.. code:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="/">
            <result>
                <xsl:choose>
                    <xsl:when test="envelope/documents/document[@id='document_id']/field[@name='field_name'] &gt; 0">
                        true
                    </xsl:when>
                    <xsl:otherwise>
                        false
                    </xsl:otherwise>
                </xsl:choose>
            </result>
        </xsl:template>
    </xsl:stylesheet>

One to Many condition
=====================

This type of condition can be applied ONLY to a table inside a document. Condition has to return "true" or "false" for every row in the table in the following format:

.. code:: xml

    <result>
      <rows>
        <row index='0'>true<row>
        <row index='1'>false<row>
        <row index='2'>false<row>
        <row index='3'>true<row>
      </rows>
    </result>

Index attribute has to match index attribute in "fieldset" node. A condition XSLT example:

.. code:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="/">
            <result>
                <rows>
                    <xsl:for-each select="envelope/documents/document[@id='document_id']/fieldgroup[@name='table_name']/fieldset">
                        <row index="{@index}">
                            <xsl:choose>
                                <xsl:when test="field[@name='field_name']='Yes'">
                                  true
                                </xsl:when>
                                <xsl:otherwise>
                                    false
                                </xsl:otherwise>
                            </xsl:choose>
                        </row>
                    </xsl:for-each>
                </rows>
            </result>
        </xsl:template>
    </xsl:stylesheet>

For every row where result = "true" a new envelope will be created. To provide "xslt" map with a proper row index, this map has to be modified accordingly. The following parameter has to be added:

.. code:: xml

    <xsl:param name="row_index"/>

And it can be used in following way:

.. code:: xml

    <field name="field_name">
        <xsl:value-of select="envelope/documents/document[@id='document_id']/fieldgroup[@name='table_name']/
            fieldset[@index=$row_index]/field[@name='field_name']/@value"/>
    </field>