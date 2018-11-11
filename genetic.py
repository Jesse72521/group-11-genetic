import string
import random

INDIVIDUAL_LENGTH = 8
MATCH_STRING = "1234567812345678" #make sure this is the same length as INDIVIDUAL_LENGTH
POPULATION_SIZE = 16
NUMBER_OF_TICKETS_PER_CORRECT_LETTER = 1
RANDOM_PERCENTAGE = 2 # 2 = 20 percent, 6 = 60%, etc.
ALLOWED_ERROR = 6 #how "perfect" our final individual has to be (0 here would mean it must be perfect)

# the only other variable you might have to change other than the ones above
# is in the randomword function.  Right now the first letter it can select is 1
# if you want to go binary between 1's and zero's you might want to change that there
# you would also have to adjust your match string accordingly if you are chaning
# the amounts of digits per letter
DIGITS_PER_LETTER = 8





# This function will create a string of digits 'length'
# digits long.
def randomword(length):
    letters = []
    for i in range(0, INDIVIDUAL_LENGTH):
        # letters.append(str(random.randint(0,1))) # used for binary
        letters.append(str(random.randint(1,DIGITS_PER_LETTER)))
    return ''.join(letters)


# This returns a score equal to the number of elements that are 
# in order. (Perfect score would be 8 on the optimal string of "12345678")
def fitnessCalc(_population):
    wordScores = []
    for x in range(0, len(_population)):
        wordScores.append(0)
        for i in range(0,INDIVIDUAL_LENGTH):
            if _population[x][i] == MATCH_STRING[i]:
                wordScores[x] = wordScores[x] + NUMBER_OF_TICKETS_PER_CORRECT_LETTER
    return wordScores

# will randomly select two individuals (returns their indexes), this is based on the example on page
# 127.  Basically i'm cycling through the scores, and producing that many MORE
# chances per individual.  (everybody will at least get one chance, every score higher gets another chance)
# a score of 2 would give them 1 + 2 chances for a total of 3, kind of like a raffle system.
def randomSelectTwo(_fitnessScores):
    entriesList = []
    for x in range(0, len(_fitnessScores)):
        entriesList.append(x) # this will be the free one that everybody gets
        for y in range(0, _fitnessScores[x]):
            entriesList.append(x)
    randomEntryOne = random.randint(0, (len(entriesList)-1))
    randomEntryOne = entriesList[randomEntryOne]
    randomEntryTwo = randomEntryOne
    while(randomEntryTwo == randomEntryOne):
        randomEntryTwo = random.randint(0, (len(entriesList)-1))
        randomEntryTwo = entriesList[randomEntryTwo]
    return randomEntryOne, randomEntryTwo


def geneticAlgorithm(_population, _fitnessCalc):
    fitEnough = False
    testPopulation = _population
    reproductionCount = 0
    while(fitEnough is not True):
        reproductionCount += 1
        fitnessScores = _fitnessCalc(testPopulation)
        newPopulation = []
        for i in range(0,len(testPopulation)):
            indexOne, indexTwo = randomSelectTwo(fitnessScores)
            child = reproduce(testPopulation[indexOne], testPopulation[indexTwo])
            newPopulation.append(child)
        newPopFitnessScores = _fitnessCalc(newPopulation)
        testPopulation = newPopulation
        for x in range(0, len(newPopFitnessScores)):
            if newPopFitnessScores[x] >= (NUMBER_OF_TICKETS_PER_CORRECT_LETTER * (INDIVIDUAL_LENGTH - ALLOWED_ERROR)):
                fitEnough = True
                print("individual found at index " +str(x) + ": " + str(newPopulation[x]))
                print("final population results after " + str(reproductionCount) + " reproductive generations: " )

def reproduce(individual1, individual2):
    randomSliceArea = random.randint(0, len(individual1))
    if random.randint(0,9) < 5:
        returnIndividual = list(individual2)
        for i in range (0, randomSliceArea):
            returnIndividual[i] = individual1[i]
    else:
        returnIndividual = list(individual1)
        for i in range (0, randomSliceArea):
            returnIndividual[i] = individual2[i]
    if(random.randint(1,10) <= RANDOM_PERCENTAGE):
        returnIndividual[random.randint(0,INDIVIDUAL_LENGTH - 1)] = str(random.randint(1,DIGITS_PER_LETTER))
    return ''.join(returnIndividual)


population = []
for i in range (0,POPULATION_SIZE):
    population.append(randomword(INDIVIDUAL_LENGTH))

# print("starting population members:")
# for x in population:
#     print(str(x))

wordScores = fitnessCalc(population)
geneticAlgorithm(population, fitnessCalc)



