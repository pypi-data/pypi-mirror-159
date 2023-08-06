# SOAR Communication Library New Client

Procedures for SOAR TCS and some other instruments communications.

This library implements a TCP/IP socket following the SOAR standard messaging protocol, this is 4 bytes to define the message length followed by the message itself using a big-endian and ASCII coding.

The command protocol is client/server with immediate response. A response should never take longer than 1500 mS.