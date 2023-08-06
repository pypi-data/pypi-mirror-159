In Progress...



We offer a simple way to encrypt data. We have 3 different ways of doing this.

Fernet - Cryptographys algorithm that contains "symmetric ciphers, message digests, and key derivation functions" (pypi.org), this is pretty basic encryption.
AES256 - It is the "current encryption standard" (idera.com), it can slow down slower processors but should be fine on most systems.
Public Key - It uses a pair of keys (public and private) to encrypt data. It encrypts the data with the public key, but the data can only be unencrypted with the private key.

This is a very simple library that I made for one of my projects, so there might be bugs. If you would like to use it have at it though.

**WARNING** Don't delete the .key files or you cant unencrypt the data that you have encrypted with that key.