import math
import random

from .matrix import Matrix


class NeuralNet():

    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        self.input_nodes = Matrix(1, input_size)
        self.w1 = Matrix(init=[[random.random()] * hidden_size for _ in range(input_size)])
        self.hidden_nodes = Matrix(1, hidden_size)
        self.w2 = Matrix(init=[[random.random()] * output_size for _ in range(hidden_size)])
        self.output_nodes = Matrix(1, output_size)
        self.output = None

    def predict(self, x):
        self.feed(x)
        return self.sigmoid(self.output_nodes).array[0]

    def feed(self, input_):
        assert len(input_) == self.input_nodes.xsize

        for index, val in enumerate(input_):
            self.input_nodes[0, index] = val

        self.hidden_nodes = self.input_nodes * self.w1
        self.output_nodes = self.sigmoid(self.hidden_nodes) * self.w2
        self.output = self.sigmoid(self.output_nodes)

    def train(self, xs, ys):
        xs = Matrix(init=xs)
        hidden_nodes = xs * self.w1  # multiple
        output_nodes = self.sigmoid(hidden_nodes) * self.w2

    @staticmethod
    def sigmoid(xs: Matrix):
        newmat = Matrix(init=[
            [1 / (1 + math.exp(-xs[y, x])) for x in range(xs.xsize)]
            for y in range(xs.ysize)
        ])
        return newmat

    @staticmethod
    def dsigmoid(y: Matrix):
        return y * (1 - y)