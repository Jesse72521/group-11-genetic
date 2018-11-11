import string
import random

INDIVIDUAL_LENGTH = 8

# This function will create a string of digits 'length'
# digits long.
def randomword(length):
    letters = []
    for i in range(0, INDIVIDUAL_LENGTH):
        letters.append(str(random.randint(1,8)))
    return ''.join(letters)


# This returns a score equal to the number of elements that are 
# in order. (Perfect score would be 8 on the optimal string of "12345678")
def fitnessCalc(_population):
    wordScores = []
    for x in range(0, len(_population)):
        wordScores.append(0)
        for i in range(0,INDIVIDUAL_LENGTH):
            # these two lines below are if i'm just trying to get a string of '1's
            # if _population[x][i] == '1':
            #     wordScores[x] = wordScores[x] + 20
            if _population[x][i] == str(i+1):
                wordScores[x] = wordScores[x] + 20
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
            if newPopFitnessScores[x] >= 160:
                fitEnough = True
                print("individual found at index " +str(x) + ": " + str(newPopulation[x]))
                print("final population results after " + str(reproductionCount) + " reproduction cycles: " )
                for x in newPopulation:
                    print(str(x))

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
    # random mutation (20% of the time on this setup)
    if(random.randint(0,9) < 2):
        returnIndividual[random.randint(0,7)] = str(random.randint(1,8))
    return ''.join(returnIndividual)


population = []
for i in range (0,16):
    population.append(randomword(INDIVIDUAL_LENGTH))

print("starting population members:")
for x in population:
    print(str(x))



wordScores = fitnessCalc(population)

# for x in wordScores:
#     print(x)

geneticAlgorithm(population, fitnessCalc)



