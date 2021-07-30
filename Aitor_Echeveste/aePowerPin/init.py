####Integrate aePowerPin in the Tracker
def OnTrackerCreate():
	import aePowerPinFun; aePowerPinFun.creation()
nuke.addOnCreate(OnTrackerCreate , nodeClass="Tracker4")

#####Integrate aePowerPin in the Planar Tracker
def OnPlanarCreate(): 
	import aePowerPinFun; aePowerPinFun.creation_planar()
nuke.addOnCreate(OnPlanarCreate , nodeClass="Roto")