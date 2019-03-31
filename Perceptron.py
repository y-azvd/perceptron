import numpy as np
import matplotlib.pyplot as plt
from readfile import readForPerceptron

class Perceptron():
	"""
	docstring for Perceptron
	"""
	##
	## @brief      Constructs the object.
	##
	## @param      self                     The simplified model for a neuron
	## @param      features                 The features
	## @param      featuresClassifications  The features classifications
	## @param      weights                  The weights
	##
	def __init__(self, features, featuresClassifications, weights=[]):
		# size of one input/array/feature/vector
		self.__dimension = len(features[0])
		self.__numberOfFeatures = len(features)
		self.__features = features
		self.__featuresClassifications = featuresClassifications

		if len(weights) == 0:
			# -.5 is the interval adjustment so its symmetrical around 0
			self.__weights = np.random.rand(self.__dimension) -.5
		else:
			self.__weights = weights
		self.__learningRate = .1
		self.__correctness = .7


	##
	## @brief      Sets the weights interval.
	##
	## @param      self          The object
	## @param      amplitude     The amplitude
	## @param      displacement  The displacement
	##
	## @return     { description_of_the_return_value }
	##
	def setWeightsInterval(self, amplitude, displacement):
		self.__weights = self.__weights*amplitude + displacement


	##
	## @brief      Sets the learning rate.
	##
	## @param      self          The object
	## @param      learningRate  The learning rate
	##
	## @return     { description_of_the_return_value }
	##
	def setLearningRate(self, learningRate):
		self.__learningRate = learningRate


	##
	## @brief      Sets the correctness.
	##
	## @param      self         The object
	## @param      correctness  The correctness
	##
	## @return     { description_of_the_return_value }
	##
	def setCorrectness(self, correctness):
		self.__correctness = correctness


	##
	## @brief      Gets the weights.
	##
	## @param      self  The object
	##
	## @return     The weights.
	##
	def getWeights(self):
		return self.__weights


	##
	## @brief      Gets the weights.
	##
	## @param      self  The object
	##
	## @return     The weights.
	##
	def getFeatures(self):
		return self.__features

	##
	## @brief      binary sigmoid function. Maps y to 0 or 1.
	##
	## @param      self  The object
	## @param      y     { parameter_description }
	##
	## @return     0 or 1
	##
	def __binarySigmoid(self, y):
		if y > 0:
			return 1
		return 0


	##
	## @brief      { function_description }
	##
	## @param      self         The object
	## @param      iethFeature  The ieth feature
	##
	## @return     { description_of_the_return_value }
	##
	def __updateWeights(self, iethFeatureIndex):
		# print '+++++++++++++++++++++++++++++++++++++++++'
		iethFeature = self.__features[iethFeatureIndex]
		# print 'iethFeature, ', iethFeature
		dotProduct = np.dot(iethFeature, self.__weights)
		# print 'dotProduct, ', dotProduct
		result  = self.__binarySigmoid(dotProduct)
		# print 'result, ', result
		desired = self.__featuresClassifications[iethFeatureIndex]
		# print 'desired, ', desired

		error = desired - result
		# print 'error, ', error
		# print 'learningRate, ', self.__learningRate
		# print 'iethFeature, ', iethFeature
		correction = error*self.__learningRate*iethFeature
		# print 'correction, ', correction

		# print 'weights, ', self.__weights
		self.__weights += correction
		# print 'weights, ', self.__weights


	##
	## @brief      { function_description }
	##
	## @param      self            The object
	## @param      numberOfEpochs  The number of epochs
	##
	## @return     { description_of_the_return_value }
	##
	def learn(self, times):
		numberOfEpochs = times*len(self.__features)
		# for iethEpoch in range(numberOfEpochs):
		for iethEpoch in range(numberOfEpochs):
			iethFeatureIndex = iethEpoch % self.__numberOfFeatures
			self.__updateWeights(iethFeatureIndex)
		print len(self.__features)


	##
	## @brief      { function_description }
	##
	## @param      self  The object
	##
	## @return     { description_of_the_return_value }
	##
	def show(self):
		print '-----------------------'
		print self.__features
		print self.__featuresClassifications
		print self.__weights
		print '-----------------------'

	

features, featuresClassifications = readForPerceptron('and2.csv', np.int)
weights  = np.asarray([-.0863252, 0.0121697, 0.0324714])

perceptron = Perceptron(features, featuresClassifications)

perceptron.setLearningRate(.5)
perceptron.setWeightsInterval(2, 0)
perceptron.learn(500)

newWeights = perceptron.getWeights()
perceptron.show()

Xs = features[:, 0]
Ys = features[:, 1]

t = np.arange(0, 1.5, .001)
print t

def function(t):
	return (-t*newWeights[0] - newWeights[-1])/newWeights[1]

plt.plot(Xs, Ys, 'o')
plt.plot(t, function(t))
plt.show()

