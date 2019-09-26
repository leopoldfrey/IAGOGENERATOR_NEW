# -*- coding: utf-8 -*-
import sys, os
from textgenrnn import textgenrnn
from threading import Thread
from pyosc import Server
from pyosc import Client

class GenThread(Thread):
    def __init__(self, num=1, temp=1, osc_client=None):
        Thread.__init__(self)
        self.num = num
        self.temp = temp
        self.osc_client = osc_client
        
    def run(self):
        path = os.getcwd()
        textgen = textgenrnn(weights_path=path+'/coexistence_weights.hdf5', vocab_path=path+'/coexistence_vocab.json', config_path=path+'/coexistence_config.json')
        result = textgen.generate(self.num, return_as_list=True, temperature=self.temp, progress=False)
        thetext = ' '.join([x for x in result if x != '<eos>'])
        thetext = thetext.strip('<eos>').replace("(", " ").replace(")", " ").strip(';')
        print(thetext)
        self.osc_client.send('/generator/result',thetext)

class Generator:

    def __init__(self, osc_server_port=5006, osc_client_host='127.0.0.1', osc_client_port=5005):
        self.osc_server = Server('127.0.0.1', osc_server_port, self.callback)
        self.osc_client = Client(osc_client_host, osc_client_port)
        
        print("Generator Ready")
        
    def generate(self, num=1, temp=1):
        thd = GenThread(num, temp, self.osc_client);
        thd.start();
    
    def callback(self, address, *args):
        if(address == '/exit'):
            print("--- EXIT ---")
            self.osc_server.stop()
            sys.exit()
        elif(address == '/generate'):
            if(len(args) >= 2):
                self.generate(args[0], temp=args[1])
            else:
                self.generate(1, 1)
            
        else:
            print("callback : "+str(address))
            for x in range(0,len(args)):
                print("     " + str(args[x]))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        Generator();
    elif len(sys.argv) == 4:
        Generator(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    else:
        print('usage: %s <osc-server-port> <osc-client-host> <osc-client-port>')
        