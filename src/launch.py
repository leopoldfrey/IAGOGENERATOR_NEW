import os
from textgenrnn import textgenrnn

textgen = textgenrnn(weights_path=os.getcwd()+'/coexistence_weights.hdf5', 
                        vocab_path=os.getcwd()+'/coexistence_vocab.json',
                        config_path=os.getcwd()+'/coexistence_config.json')

print(textgen.generate(5, return_as_list=True, temperature=1.0, progress=False))
print(textgen.generate(5, return_as_list=True, temperature=1.0, progress=False))
print(textgen.generate(5, return_as_list=True, temperature=1.0, progress=False))
print(textgen.generate(5, return_as_list=True, temperature=1.0, progress=False))
        