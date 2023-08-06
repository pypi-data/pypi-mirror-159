# ponte

A mini-library to process arrays to .json files and viceversa. Developed to pass arrays between Python and C++ through the use of json DOK files.

## Installation

```ruby
pip install ponte
```

## Contributors

- [Andrew Garcia](https://github.com/andrewrgarcia) - creator and maintainer

## Contributing

1. Fork it (<https://github.com/your-github-user/tensorscout/fork>)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## Usage Example

For full application, i.e. passing array structures between Python and C++ code, see [bridge](https://github.com/andrewrgarcia/bridge)

```ruby
import ponte as bridge
import numpy as np

'CREATE A 1-D VECTOR'
X = np.random.choice([0,1,2,3],10,p=[0.7,0.1,0.1,0.1])
'pack vector to .json file'
bridge.tojson('sample.json',X)

'PROCESS JSON FILE BACK TO VECTOR'
array_form = bridge.jsonload('sample.json')
'print vector'
print('array:\n',array_form)

'''
array to DOK:
{
	"map": [
		[1],
		[4],
		[5],
		[8],
		[9]
	],
	"value": [2, 3, 2, 2, 2],
	"odims": [10]
}

DOK to array:
[0. 2. 0. 0. 3. 2. 0. 0. 2. 2.]
'''
```
