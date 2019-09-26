# Text Generator

Poetry Generation Module for Iagotchi-Bot Project

## Setup

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What dependencies you need to install the generator. 

* Python 3.6
* Keras
* Scikit-learn

```
Give examples
```

### Installing

Install all required packages


```
pip3.7 install -r requirements.txt
```


## Usage

### Train new model
For training new model, you  must specify the source file path and the name of the new 
model in the *paramters.json* file. See the parameters file for additional configurations
needed to train the model. The default values in the file except the source and model name
are sufficient to obtain an efficient model.

The script train.py is used for training new model. It needs the parameters.json file as 
an argument as in the following command line:

```
python3.7 train.py  --parametersfile parameters-coex.json
```

At the end, the script produces three files needed for the text generation phase:
vocabulary file (model_name_vocab.json), config file (model_name_config.json) and
weights file (model_name_weights.hdf5). 

### Generate texts

```
python3.7 generate.py --config coexistence_config.json --vocab coexistence_vocab.json --model coexistence_weights.hdf5 --n 5 --temperature 0.5
```

## Built With

* [TextGenRNN](https://github.com/minimaxir/textgenrnn) -  text-generating neural 
network of any size and complexity on any text dataset
