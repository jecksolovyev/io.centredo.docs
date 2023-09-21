Dictionary field behavior after dictionary or dictionary column deletion
========================================================================

**Template**

When dictionary or dictionary column is deleted, such template will become invalid (new dictionary or dictionary column should be selected in dictionary field properties).

**Envelope**

When dictionary or dictionary column is deleted, dictionary field will be disabled in processing envelopes and envelope with such field will be expired automatically after expiration date. Exception is case where custom value are allowed. In such case dictionary field will work as text field and custom text value can be entered in it.