"""
https://www.kode24.no/guider/the-best-way-to-learn-deep-learning/71003527

Simple neural network
"""


def simple_neural_netowrk(input, weight, goal_prediction, train):
    for i in range(train):
        prediction = input * weight


        """
        Squared root error is used to always get a positive number to work with
        """
        error = (prediction - goal_prediction) ** 2

        """Delta is a measurement of the differation between the true prediction and NN prediction
        For example if the true prediction is 1.0 and the NN prediction is 0.85, the delta is negative 0.15"""
        delta = prediction - goal_prediction


        """
        Weight_Delta is a value of how much the a weight caused the network to miss, this value
        will help us understand and reduce the amount we missed
        """
        weight_delta = delta * input

        """
        Before updating the weight we multiply with alpah, this is to set the pace the NN learn on
        """
        alpah = 3
        weight -= weight_delta * alpah
    print('Error: ',error, ' Prediction: ', prediction)


simple_neural_netowrk(0.3,0.1,0.7, 10)