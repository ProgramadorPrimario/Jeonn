import numpy as np

class Neuron:
    
    def __init__(self, n_input):
        self.weight = np.random.randn(n_input)
        self.bias = np.random.randn()
        self.output = 0
        self.inputs = None
        self.dweight = np.zeros_like(self.weight)
        self.dbias = 0
        
    
    def activate(self, x):
        return 1/(1 + np.exp(-x))
    
    def derivate_active(self, x):
        return x * (1 -x)
    
    def forward(self, inputs):
        self.inputs = inputs
        weighted_sum = np.dot(inputs, self.weight) + self.bias
        output = self.activate(weighted_sum)
        return self.output
    
if __name__== "__main__":
    neuron = Neuron(3)
    inputs = np.array([1, 2, 3])
    output = neuron.forward(inputs)
    
    print("Salida u output de la neurona: ", output) 
    
    
    
"""
section .data
    msg db 'Hola', 0xA
    len equ $ - msg

section .text
    global _start

_start:
    ; Imprimir el mensaje
    mov eax, 0xFFFFFFFF
    push len
    push msg
    push 0xFFFFFFFF   ; stdout
    call [__imp__GetStdHandle@4]
    mov ebx, eax
    push 0
    push 0
    push len
    push msg
    push ebx
    call [__imp__WriteFile@20]

    ; Salir del programa
    push 0
    call [__imp__ExitProcess@4]
"""