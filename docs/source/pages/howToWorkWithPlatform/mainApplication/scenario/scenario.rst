========
Scenario
========

.. toctree::

    scenarioManagement/scenarioManagement.rst
    scenarioManagement/scenarioRun.rst

Scenario functionality allows to create chains of the envelopes and transmit data from one envelope to antoher if needed.
    
Scenario list and scenario concept
==================================

Scenario includes the following information: name, description, uuid and steps of the scenario.

Steps include name, source and destination (where source and destination include template uuid and template version uuid) and conversion rule.

.. warning:: **Please note! First step of the scenario doesn\'t contain source. It contains only destination**

How to manage scenario you can find follow the :ref:`link <scenario-management>`.

How to run scenario you can find follow the :ref:`link <scenario-run>`.