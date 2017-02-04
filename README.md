<img src="files/pifx.png" width="300">

[![PyPI](https://img.shields.io/pypi/v/pifx.svg)]()
[![](https://travis-ci.org/cydrobolt/pifx.svg)](https://travis-ci.org/cydrobolt/pifx)

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

p.toggle_power() # toggle all lights
p.toggle_power('label:Bedroom') # toggle light with label "Master Bedroom"

p.set_state(color='blue', brightness='0.85') # set brightness to 85% and color to blue
p.pulse_lights(color='red', duration=2.5) # pulse lights for 2.5 seconds
```

Read [the docs](http://pifx.readthedocs.org/en/latest/) for full usage instructions.

### Hacking on PIFX

Running tests:
 - `pip install nose`
 - `nosetests`

Contributing:
 - We appreciate contributions from all users.
 - Fork the project, add your changes, and make a pull request.
 - Thank you!

### Other information

PIFX is an open source library not affiliated or endorsed by LIFX ®

```
 Copyright © 2015 Chaoyi Zha <me@cydrobolt.com>

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
```
