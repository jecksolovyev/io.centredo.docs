======================
Common API error codes
======================

.. toctree::

400 - Bad request (if request data is invalid and doesn’t correspond to API documentation. Also can contain detailed issue description).
401 - Unauthorized (if auth token is invalid, incorrect or expired).
402 - Payment Required (if billing deny some functionality because of no payment or tariff restriction).
403 - Forbidden (if particular entity doesn’t have access or permissions to requested entity. Also can contain detailed issue description).
404 - Not found (if requested entity doesn’t exist or is deleted (in case of not soft deletion)).
409 - Conflict (very rare case, appears if two entities has conflicts but usually we have retries and customer doesn’t see this error).
410 - Entity gone (if requested entity deleted (soft deletion), as example in case if template which processed was deleted).
422 - Unprocessable entity (if requested entity can’t be processed, as example in case of approve or reject envelope second time).
425 - Too early (if request has been sent too early, as example appears in case if request could be sent with respective period of time but was sent earlier).
429 - Too many requests (if you send too many requests to respective endpoint and exceed limits of the request).