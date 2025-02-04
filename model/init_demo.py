"""
init.py

Starting script to run NetPyNE-based A1 model.


Usage:
    python init.py # Run simulation, optionally plot a raster


MPI usage:
    mpiexec -n 4 nrniv -python -mpi init.py


Contributors: ericaygriffith@gmail.com, salvadordura@gmail.com
"""
#in VSC, terminal -> cd to filepath
#import matplotlib; matplotlib.use('Agg')  # to avoid graphics error in servers
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use('Agg')
from netpyne import sim

cfg, netParams = sim.readCmdLineArgs(simConfigDefault='cfg_demo.py', netParamsDefault='netParams.py')

sim.createSimulateAnalyze(netParams, cfg)

sim.initialize(
    simConfig = cfg, 	
    netParams = netParams)  				# create network object and set cfg and net params
sim.net.createPops()               			# instantiate network populations
sim.net.createCells()              			# instantiate network cells based on defined populations
sim.net.connectCells()            			# create connections between cells based on params
sim.net.addStims() 							# add network stimulation
sim.setupRecording()              			# setup variables to record for each cell (spikes, V traces, etc)
sim.runSim()                      			# run parallel Neuron simulation  
sim.gatherData()                  			# gather spiking data and cell info from each node

# distributed saving (to avoid errors with large output data)
#sim.saveDataInNodes()
#sim.gatherDataFromFiles()

sim.saveData()  

sim.analysis.plotData()         			# plot spike raster etc
plt.savefig('demo_raster_22.05.png')