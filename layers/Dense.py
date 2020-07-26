import numpy as np



class Dense:
    def __init__(self, output_units, input_shape=None,activation=None):
        self.input_array = None
        self.units = None
        self.output_units = output_units
        self.weights = []
        self.result = 0
        self.name = "Dense"
        self.input_shape = input_shape
        self.output_shape = None
        self.number_of_params = None
        self.activation = activation


    def init_weights(self):
        self.weights = np.random.rand(self.units,self.output_units)
        self.number_of_params = self.units * self.output_units


    def normalize(self,input_array):
        return input_array/np.amax(input_array)


    def calculate(self):
        x1 = np.expand_dims(self.input_array, axis = 0)
        x2 = self.weights
        self.result = np.squeeze(np.matmul(x1,x2),axis=0)
        self.result = self.normalize(self.result)
        if self.activation != None:
            self.result = self.activation.calculate(self.result)
        self.output_shape = self.result.shape
        return self.result

