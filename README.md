pub-key
=======

A Public-Key Cryptographic Standard Converter using **OpenSSL**. 

This converter is disigned to assist people in converting there SSL 
Certificates that you get from an Certificate Authority into usuable objects, 
that can be used by most modert webservers or browsers. 

Generaly when you create a CSR the CA will send you informaion in one of 3 
formats.

1. PEM or Plain Text 
2. PKCS7 a bundle of your certificate chain and ID certificate
3. PKCS12 a bundle of your certificate chain and ID certificate an possibly a 
key if it was created for you. 

Below is are the optional components (denoted by \*) that PCKS12 and PKCS 7 
types may contain: 

    PKCS7               PKCS12
       +-----------------+
     * |    CA Cert      | *
     * |    IM Cert      | *
       +-----------------+
       +-----------------+
     * | Identity Cert   | *
       |      Private Key| *
       +-----------------+

To use any combination of these certificates in your web sever you will likely 
need to convet your certifices into one or more of these individual types, or 
use exsisting information (such as a key) to create the PKCS12 type you may 
want to use. 

While **OpenSSL** provides you options to do this remembering all of the 
options is cumbersom and error prone. This script is used to simplfy the 
process. 
