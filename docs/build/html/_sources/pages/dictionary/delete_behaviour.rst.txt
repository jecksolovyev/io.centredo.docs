Behaviour of dictionary field after deleting a dictionary column or a dictionary
================================================================================
**Template**

When dictionary or dictionary column are deleted - such template will be invalid(need to select new dictionary or dictionary column in dictionary field at this template).

**Envelope**

When dictionary or dictionary column are deleted - dictionary field in processing envelopes will be disabled and envelope with such
field will be expired automatically after expiration date, except case when was specified allow custom value attribute.
In such case dictionary field will work as text field and user can enter text value to dictionary field, without binding to column values.