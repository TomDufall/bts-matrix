# bts-matrix
Backstage have recently bought a DVI matrixer which has no physical buttons on it, unlike our existing VGA matrixes. While we have a remote control to control it, this isn't ideal in a live show environment and isn't the easiest or quickest interface either.

This project aims to create a web-based interface that can run on a local computer and communicate with the matrix over serial, allowing for easy control. It should also be possible to communicate with our VGA matrixes using this system. This will make it easy to control matrixes that aren't immediately to hand, whether they be under the table or on the other side of the venue.

The project consists of two main parts:
1) An abstract Matrix interface, allowing for control of matrixes using python functions. A model-specific implementation of the interface will convert the python functions to serial communication to achieve the desired effect.
2) A web-based GUI to control matrixes graphically.

Currently, the Matrix interface is being worked on, and an interface and implementation for the DVI matrix exists for core routing functions such as patching an input to an output. This will be tested with the matrix itself around the end of Jan 2019. The next step is to create an interface for established and recalling preset scenes, after which work will begin on the web-based GUI,
