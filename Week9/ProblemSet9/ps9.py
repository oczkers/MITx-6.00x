# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b_precompiled_27 import *


#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005

    delays = [300, 150, 75, 0]
    results = []

    for delay in delays:
        for i in range(numTrials):
            virusList = []
            virusPop = 0
            for n in range(numViruses):
                virusList.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
            my_patient = TreatedPatient(virusList, maxPop)

            for step in range(delay + 150):
                if step == delay:
                    my_patient.addPrescription('guttagonol')
                virusPop = my_patient.update()
            results.append(virusPop)

    toPlot = []
    for i in range(0, len(results), numTrials):
        toPlot.append(results[i:i+numTrials])
    #print toPlot

    for i, _ in enumerate(delays):
        pylab.subplot(2, 2, i+1)
        pylab.hist(toPlot[i])
    pylab.show()


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    first_drug = 150
    second_drug = 300
    steps = first_drug + second_drug
    total_vs = [0 for i in steps]
    resis_vs = list(total_vs)
    results = list(total_vs)

    for trial in range(numTrials):
        viruses = []
        for i in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        patient = TreatedPatient(viruses, maxPop)

        for step in range(steps):
            if step == first_drug:
                patient.addPrescription('guttagonol')
            elif step == second_drug:
                patient.addPrescription('grimpex')
            patient.update()
            total_vs[step] += patient.getTotalPop()
            resis_vs[step] += patient.getResistPop(['guttagonol'])
            resis_vs[step] += patient.getResistPop(['grimpex'])

        results.append(patient.getTotalPop())

    pylab.hist(results, 9)
    pylab.show()
