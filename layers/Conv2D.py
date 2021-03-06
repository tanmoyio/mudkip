import numpy as np



class Conv2D:
    def __init__(self,units,input_shape=None,kernel_size=(3,3),stride=2,activation=None):
        self.input_array = None
        self.kernel_size = kernel_size
        self.units = units
        self.stride = stride
        self.weights = []
        self.result = []
        self.name = "Conv2D"
        self.input_shape = input_shape
        self.output_shape = None
        self.number_of_params = units * kernel_size[0] * kernel_size[1]
        self.activation = activation
        self.dw = []



    def init_weights(self):
        self.weights = np.random.uniform(low=-1.0, high=1.0, size=(self.units, self.kernel_size[0], self.kernel_size[1]))



    def normalize(self,input_array):
        return (input_array/(np.amax(input_array)+np.amin(input_array)))

    

    def calculate(self): 
        i, j, row, col = 0, 0, 0, 0
        sum_conv = 0
        self.dw = []
        if len(self.input_array.shape) ==2:
            self.input_array = np.expand_dims(self.input_array, axis = 2)
        while i<= self.input_array.shape[0] and i+self.kernel_size[0] <= self.input_array.shape[0]:
            while j<= self.input_array.shape[1] and j+self.kernel_size[1] <= self.input_array.shape[1]:
                for weight in self.weights:
                    sum_conv = np.sum([np.multiply(slice_mat[i:i+self.kernel_size[0], j:j+self.kernel_size[1]],weight) for slice_mat in self.input_array.reshape(self.input_array.shape[::-1])])
                    self.result.append(sum_conv)
                    sum_conv = 0
                self.dw.append([q for p in self.input_array[i:i+self.kernel_size[0],j:j+self.kernel_size[1],:] for q in p])
                j = j + self.stride
                if i == 0:
                    col = col + 1
            i = i + self.stride
            j = 0
            row = row + 1
        self.dw = np.array(self.dw)
        self.result = np.array(self.result).reshape(row,col,self.units)
        self.result = self.normalize(self.result)
        if self.activation != None:
            self.result = self.activation.calculate(self.result)
        temp_result = self.result
        self.result = []
        self.output_shape = temp_result.shape
        return temp_result
        


