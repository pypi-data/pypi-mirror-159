import gradio as gr
import socket
import random

def _portConnection(port : int):
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
            
    result = s.connect_ex(("localhost", port))
    if result == 0: return True
    return False

def _determinePort():
    while True:
        randPort=random.randint(2000, 9000)
        if not _portConnection(randPort):
            return randPort

def register(inputs, outputs):
    def register_gradio(func):
        def wrap(self, *args, **kwargs):            
            try:
                self.registered_gradio_functons
            except AttributeError:
                print("✨Initializing Class Functions...✨")
                self.registered_gradio_functons = dict()

            fn_name = func.__name__ 
            if fn_name in self.registered_gradio_functons: 
                result = func(self, *args, **kwargs)
                return result
            else:
                self.registered_gradio_functons[fn_name] = dict(inputs=inputs, outputs=outputs)
                return None
        return wrap
    return register_gradio
    
 

def gradio_compile(cls):

    class Wrapper:
        def __init__(self) -> None:
            self.cls = cls()


        def get_func(self):
            return [func for func in dir(self.cls) if not func.startswith("__") and type(getattr(self.cls, func, None)) == type(self.get_func) ]
    
        def compile(self, **kwargs):
            print("Just putting on the finishing touches... 🔧🧰")
            for func in self.get_func():
                this = getattr(self.cls, func, None)
                if this.__name__ == "wrap":
                    this()

            demos = []
            names= []
            for func, param in self.get_registered_gradio_functons().items():
                print(param)
                
                demos.append(gr.Interface(fn=getattr(self.cls, func, None),
                                          inputs=param['inputs'],
                                          outputs=param['outputs'],
                                          live=kwargs['live'] if "live" in kwargs else False,
                                          allow_flagging=kwargs['flagging'] if "flagging" in kwargs else 'never',
                                          theme='default'))
                names.append(func)
            print("Happy Visualizing... 🚀")
            return gr.TabbedInterface(demos, names)
            
        def get_registered_gradio_functons(self):
            try:
                self.cls.registered_gradio_functons
            except AttributeError:
                return None
            return self.cls.registered_gradio_functons
            
        def run(self, **kwargs):

            port= kwargs["port"] if "port" in kwargs else _determinePort()  
            self.compile(live=kwargs['live'] if "live" in kwargs else False,
                                    allow_flagging=kwargs['flagging'] if "flagging" in kwargs else 'never',).launch(server_port=port) 
    return Wrapper