===============================
Server Configuration Properties
===============================

.. toctree::

Global Properties
=================

| **app.name** - The name of the platform
| **app.theme** - The UI theme of the platform (Red or Blue)

User Properties (app.user)
==========================

| **validation-code-hours-lifetime** - The life time of the validation code in email
| **invitation-hours-lifetime** - The life time of invitation to the account
| **seconds-between-validations** - To prevent many requests and many emails
| **profile-phone**:boolean - Enable required phone on registration
| **profile-phone-default-region** - Default phone region (UA,FR,GB)
| **email-validation-code-length** - The number of characters for validation code in e-mail

Locale Properties (app.locales)
===============================
| **supported** - The list of supported locales (en, ru, uk)
| **defaultLocale** - The default locale of the platform (for invitations)
| **defaultCountry** - The default country of the platform (if no coordinates in header)
| **defaultAsLanguage** - The default locale will be taken as language in browser (geolocation and language of browser don't matter then)
| **timezone** - The default time zone of the platform (for user creation, dates in email and pdf)

Password Policy (app.user.password-policy)
==========================================

| **min-length** - Enforce minimum password length
| **max-length** - Enforce maximum password length
| **uppercase** - Require uppercase letters
| **lowercase** - Require lowercase letters
| **digit** - Require digits
| **special-symbol** - Require at least one special character (! @ # $ % ^ & * ( ) _ + - = [ ] { } |
| **repeat-character** - Do not allow repeating characters
| **allow-whitespace**:boolean - Allow whitespace in password
| **prevent-common-passwords**:boolean - Do not allow forbidden passwords (see BannedPassword db table)
| **prevent-common-words**:boolean - Do not allow forbidden words in password (see BannedPasswordWord db table)
| **expiration-days** - Password will be expired after days
| **notify-before-days** - Send password expiration notification before expiration days
| **prevent-reuse-months** - Do not allow reuse of passwords during period of months
| **prevent-reuse-count** - Do not allow reuse of a recent number of passwords

Session Policy (app.user.session-policy)
========================================

| **session-hours** - Keep session during idle period
| **single-session**:boolean - Enforce single session for one user
| **single-ip-session**:boolean - Enforce single user session per IP
| **max-login-attempts** - Maximum login attempts before locking
| **max-attempts-timeout-minutes** - Lock time after multiple login attempts
| **allowed-ips**:array - The list of allowed IPs
| **blocked-ips**:array - The list of blocked IPs

| **FYI**
| Each property can be set via ENVIRONMENT property by replacing '.' with '_' and in upper case, see examples:
| APP_NAME=WhiteDoc
| APP_USER_PASSWORD-POLICY.UPPERCASE=2