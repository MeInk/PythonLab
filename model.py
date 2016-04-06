def weight(inputWeight):
    """
    This function check rightness of weight that you write
    :param inputWeight:weight that you write
    :return:weight
    """
    while(True):
        if (inputWeight>160 or inputWeight<=0):
            inputWeight=input()
        else:return inputWeight



def height(inputHeight):
    """
    This function check rightness of height that you write
    :param inputHeight:height that you write
    :return:height
    """
    while(True):
        if (inputHeight>250 or inputHeight<=0):
            inputHeight=input()
        else:return inputHeight


def age(inputAge):
    """
    This function check rightness of age that you write
    :param inputAge:age that you write
    :return:age
    """
    while(True):
       if (inputAge>110 or inputAge<=0):
           inputAge=input()

       else: return inputAge


def chooseNumberOfT(number):
    """
    In this function you choose how often you do physical exercises
    :param number:Number of your week train
    :return:factor that depends on your week trains
    """
    if (number == 1):
        factor = 1.2
    elif (number == 2):
        factor = 1.375
    elif (number == 3):
        factor = 1.4625
    elif (number == 4):
        factor = 1.550
    elif (number == 5):
        factor = 1.6375
    elif (number == 6):
        factor = 1.725
    elif (number == 7):
        factor = 1

    return factor


def calculation(Weight, Height, Age, Factor):
    """

    :param weight:your weight
    :param height:your height
    :param age:your age
    :param factor:factor that depends on your week trains
    :return:callories that your must get every day
    """
    nCallories = (int)((10 * Weight + 6.25 * Height - 5 * Age - 161) * Factor)
    return nCallories
