.. _password-policy:

===============
Password policy
===============

.. toctree::

You're able to configure password and session policy for all users with verified domains in your account. You can make it more strict than default system configuration.
To do that follow next instructions.

How to change password or session policy?
=========================================

1. First of all verify any domain. It's necessary to do, because without users with verified domains rules won't work.

2. Open /admin/account-settings?activeTab=password-policy page

3. Make rule stricter than default system rule and save changes

After actions above password or session policy will be applied for any user with email from verified domain.

How to make password policy stricter?
=====================================

There are a lot of password policy and session policy options:

1. Minimum password length. It means that minimal quantity of symbols in password should be not less than configured, so to make this option stricter you can use value bigger or equal than default value "min-length" in configuration

2. Maximum password length. It means that maximum quantity of symbols in password shouldn't be bigger than configured, so to make this option stricter you can user value lower or equal than default value "max-length" in configuration

3. Require uppercase letters. It means that password should contain at least N uppercase letters where N is value "uppercase" in configuration. To make it stricter use value bigger or equal as in configuration. But don't use quantity of symbols bigger than maximum available length of password

4. Require lowercase letters. It means that password should contain at least N lowercase letters where N is value "lowercase" in configuration. To make it stricter use value bigger or equal as in configuration. But don't use quantity of symbols bigger than maximum available length of password

5. Require numeric value. It means that password should contain at least N numeric symbols where N is value "digit" in configuration. To make it stricter use value bigger or equal as in configuration. But don't use quantity of symbols bigger than maximum available length of password

6. Require at least one special character ! @ # $ % ^ & * ( ) _ + - = [] {} |. It means that password should contain at least N special characters where N is value "special-symbol" in configuration. To make it stricter use value bigger or equal as in configuration. But don't use quantity of symbols bigger than maximum available length of password

7. Do not allow repeat. It means that password shouldn't contain repeated symbols. So if in configuration is "Don't allow repeat" value 3, you can't use three repeated characters ("111", "aaa" or etc.). To make this option stricter use lower or equal value "repeat-character" as in configuration

8. Allow whitespace in password. This option allows or disallows to use whitespaces in password

9. Do not allow the use of forbidden passwords. This option allows or disallows to use forbidden passwords

10. Do not allow the use of forbidden words. This option allows or disallows to use forbidden words in password

11. Enable password expiration. This is option which responsible for password expiration. If you want to make stricter rules set value lower than value "expiration-days" in configuration

12. Send password expiration notification. This is option which responsible for quantity of days for password expiration notification. To make it stricter set value "notify-before-days" lower than in configuration

13. Do not allow reuse of passwords. Option which is responsible for period of time which password can't be re-used. To make it stricter set value "prevent-reuse-months" bigger than in configuration

14. Do not allow reuse of recent. Option which is responsible for quantity of previous password which can't be re-used. To make it stricter set value "prevent-reuse-count" bigger than in configuration

How to make session policy stricter?
====================================

1. Keep session during idle period. Option which is responsible for time while session is active in idle. To make it stricter set value "session-hours" lower than in configuration

2. Single session for one user. Option which allows or disallows single browser session

3. Single user session per IP. Option which allows or disallows single IP session

4. Maximum login attempts before locking. Option which is responsible for quantity of incorrect password user enters before locking. To make it stricter set value "max-login-attempts" lower than in configuration

5. Lock time after multiple login attempts. Option which is responsible for period of time on which user will be locked. To make it set value "max-attempts-timeout-minutes" bigger than in configuration

6. The list of allowed IPs. The list of IP addresses from which users are able to log in on platform

7. The list of blocked IPs. The list of IP addresses from which users aren't able to log in on platform
