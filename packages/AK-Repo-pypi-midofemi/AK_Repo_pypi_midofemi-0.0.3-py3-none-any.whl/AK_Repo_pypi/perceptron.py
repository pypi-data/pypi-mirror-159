import numpy as np
import logging
from tqdm import tqdm #This package helps us to get output on our terminal vis a progress bar when doing logging. So we don't necessarily need
#To open our log for info. We can see it on the terminal
#This package goes anywhere there is a for loop in our program

class Perceptron:
  def __init__(self, eta, epochs):
    #This initialize the weights. We used random 3 for (w1,w2, w0). This is because we gonna be using 2 feature X1 and X2
    #But if you look at the note. We always need a bias w0 which make it a total of 3 weight
    #We also multiply it by 1e-4 because we want it to be very small
    self.weights = np.random.randn(3) * 1e-4 # SMALL WEIGHT INIT
    logging.info(f"initial weights before training: \n{self.weights}")
    self.eta = eta # LEARNING RATE
    self.epochs = epochs  


  def activationFunction(self, inputs, weights):
    z = np.dot(inputs, weights) # z = W * X
    return np.where(z > 0, 1, 0) # CONDITION, IF TRUE, ELSE. If Z > 0 then Z = 1. ELSE 0

  def fit(self, X, y):
    self.X = X
    self.y = y
    #This jut generate an array of bias for you. The bias here is -1
    #-np.ones(len(X), 1) = [-1,-1,-1,-1]
    X_with_bias = np.c_[self.X, -np.ones((len(self.X), 1))] # CONCATINATION
    logging.info(f"X with bias: \n{X_with_bias}")
    
    #This is our training Looop
    for epoch in tqdm(range(self.epochs), total = self.epochs, desc = "Training the model"):
      logging.info("--"*10) #Don't be confuse here. This just logging.info many dashes for you time 10. For egs: -----------------------------
      logging.info(f"for epoch: {epoch}")
      logging.info("--"*10)

      y_hat = self.activationFunction(X_with_bias, self.weights) # foward propagation
      logging.info(f"predicted value after forward pass: \n{y_hat}")
      self.error = self.y - y_hat
      logging.info(f"error: \n{self.error}")
      self.weights = self.weights + self.eta * np.dot(X_with_bias.T, self.error) # backward propagation
      logging.info(f"updated weights after epoch:\n{epoch}/{self.epochs} : \n{self.weights}")
      logging.info("#####"*10)


  def predict(self, X):
    X_with_bias = np.c_[X, -np.ones((len(X), 1))]
    return self.activationFunction(X_with_bias, self.weights)

  def total_loss(self):
    total_loss = np.sum(self.error)
    logging.info(f"total loss: {total_loss}")
    return total_loss