
#to run: just -f ~/ldmx-sw/justfile fire cosmic_config_particlegun.py 
#New name convetions have been implemented


from LDMX.Framework import ldmxcfg
p = ldmxcfg.Process('cosmics')

import LDMX.Ecal.ecal_hardcoded_conditions #New name change
import LDMX.Hcal.hcal_geometry 
import LDMX.Ecal.ecal_geometry 
import LDMX.Hcal.hcal_hardcoded_conditions

# import processor templates
#import LDMX.Ecal.digi as ecal_digi
import LDMX.Hcal.digi as hcal_digi
import LDMX.Hcal.hcal_geometry

from datetime import datetime
current_date = datetime.now().strftime("%Y%m%d")  # Added current date to the filename
output_string = "cosmicEvents/cosmic_events_" + current_date + ".root"

import time

start = time.time()

p.output_files = [output_string]
p.run = 1
p.log_frequency = 1
p.term_log_level = 1

from LDMX.SimCore import simulator

sim = simulator.simulator('lhe_cosmics_simulation')
sim.setDetector( 'ldmx-cosmic-hcal-prototype' )


import os,sys
print(os.listdir())
from LDMX.SimCore import generators


myParticleGun = generators.gun( "myParticleGun" )
#What particle.
myParticleGun.particle = 'mu+'
#Energy of particle.
myParticleGun.energy = 10.
#Position from where to shoot the particle.
myParticleGun.position = [25., 722. , 25.]
myParticleGun.time = 0.
#In what direction to shoot the particle.
myParticleGun.direction = [0., -1., 0.]

sim.generators = [ myParticleGun ]

p.max_events = 10000

#p.sequence = [ sim , hcal_digi.HcalDigiProducer(), hcal_digi.HcalRecProducer()]
p.sequence = [ sim , hcal_digi.HcalSimpleDigiAndRecProducer()]
