# PIFX
A Python library for the LIFX cloud HTTP API

### Installing PIFX

Install PIFX using `pip`: 
 - `pip install pifx`

Install PIFX from source: 
 - `git clone https://github.com/cydrobolt/pifx.git`
 - `cd pifx`
 - `python setup.py install`

### Using PIFX

Create an API key
 - Head to https://cloud.lifx.com/settings
 - Generate a new personal API token

Importing `PIFX` in your Python file:
 - `from pifx import PIFX`

Creating a PIFX instance:

 - `p = PIFX('API_KEY_GOES_HERE')`

Performing PIFX actions:
```python
import pifx

p = pifx.PIFX(api_key='API_KEY_GOES_HERE')

p.toggle_lights() # toggle all lights`
p.set_state(color='blue', brightness='0.85') # set brightness to 85% and color to blue
p.pulse_lights(color='red', duration=2.5) # pulse lights for 2.5 seconds
```

Read [the docs](https://pifx.rtfd.org) for full usage instructions.

### Hacking on PIFX

Running tests: 
 - `pip install nose`
 - `nosetests`

Contributing:
 - We appreciate contributions from all users.
 - Fork the project, add your changes, and make a pull request.
 - Thank you!
