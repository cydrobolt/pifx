.. PIFX documentation master file, created by
   sphinx-quickstart on Thu Dec 17 19:05:24 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. raw:: html


    <div style='text-align: center'>
        <img src='_static/pifx.png' style='width:300px' />
        <h3>Developer Documentation</h3>
    </div>

=============================

To use PIFX, initiate an instance of the PIFX class with your API token to use its functions.

.. code-block:: python

    import pifx

    p = pifx.PIFX(api_key='API_KEY_GOES_HERE')

    p.toggle_power() # toggle all lights
    p.toggle_power('label:Bedroom') # toggle light with label "Master Bedroom"
    p.set_state(color='blue', brightness='0.85') # set brightness to 85% and color to blue
    p.pulse_lights(color='red', duration=2.5) # pulse lights for 2.5 seconds

PIFX Usage Documentation:

.. toctree::
   :maxdepth: 2

.. automodule:: pifx
.. autoclass:: PIFX
    :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
