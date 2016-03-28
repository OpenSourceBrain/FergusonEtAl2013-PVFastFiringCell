### NeuroML2/LEMS version of model 

The model defined in the Python Brian scripts has been converted to a LEMS ComponentType defintion: [IzhikevichFerguson.xml](https://github.com/OpenSourceBrain/FergusonEtAl2013-PVFastFiringCell/blob/master/NeuroML2/IzhikevichFerguson.xml).

Note this is different from the existing [Izhikevich model definition in NeuroML2](https://neuroml.org/NeuroML2CoreTypes/Cells.html#izhikevichCell), as outlined in [Ferguson et al. 2013](http://journal.frontiersin.org/article/10.3389/fncom.2013.00144/abstract):

> The model has a fast variable representing the membrane potential, V (mV), 
and a slow “recovery” current given by the variable u (pA).
In order to capture the spike width at threshold, we slightly modified the 
Izhikevich model by using a different “k” parameter above
and below the spike threshold (khigh and klow respectively).

A LEMS file ([LEMS_PVBC.xml](https://github.com/OpenSourceBrain/FergusonEtAl2013-PVFastFiringCell/blob/master/NeuroML2/LEMS_PVBC.xml)) creates a network with a single cell:

	<izhikevichFergusonCell id="PVBC" v0 = "-65mV" C="90 pF" vr = "-60.6 mV"
                        vpeak = "2.5 mV" c = "-70 mV" klow = "1.7 nS_per_mV" khigh = "14 nS_per_mV"
                        a = "0.1 per_ms" d = "0.1 pA" vt = "-43.1 mV" b = "-0.1 nS"/>
                            
applies currents as specified in the Python scripts and runs a simulation with the cells:

![](https://raw.githubusercontent.com/OpenSourceBrain/FergusonEtAl2013-PVFastFiringCell/master/NeuroML2/PVBC.png)
  
This model can be run locally using [jNeuroML](https://github.com/NeuroML/jNeuroML):
  
    git clone https://github.com/OpenSourceBrain/FergusonEtAl2013-PVFastFiringCell.git
    cd FergusonEtAl2013-PVFastFiringCell/NeuroML2
    jnml LEMS_TwoCells.xml
    
or using [pyNeuroML](https://github.com/NeuroML/pyNeuroML):
  
    git clone https://github.com/OpenSourceBrain/FergusonEtAl2013-PVFastFiringCell.git
    cd FergusonEtAl2013-PVFastFiringCell/NeuroML2
    pynml LEMS_TwoCells.xml
  
  

