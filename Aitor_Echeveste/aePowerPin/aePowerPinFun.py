# aePowerPin v1.0
# 
#
# Aitor Echeveste - 2020
#

import nuke, nukescripts



def creation ():
    node = nuke.thisNode()
    tab = nuke.Tab_Knob('button', 'button')
    tab.setVisible(False)
    tab.setFlag(0x0000000000000400)
    node.addKnob(tab)
    

    m = nuke.PyScript_Knob("createPPinUseCurrentFrameBaked","createPPinUseCurrentFrameBaked","import aePowerPinFun\naePowerPinFun.createPPinUseReferenceFrameBaked()")
    node.addKnob(m)
    
    m = nuke.PyScript_Knob("createPPinUseReferenceFrameBaked","createPPinUseReferenceFrameBaked","import aePowerPinFun\naePowerPinFun.createPPinUseReferenceFrameBaked()")
    node.addKnob(m)
    
    
    n = nuke.thisNode()
    k = n['cornerPinOptions']
    list = k.values()
    list.append('aePowerPin (use current frame)')
    list.append('aePowerPin (use transform ref frame)')
    
    print list
    k.setValues(list)
    print k.values()
    
    kk = n['createCornerPin']
    
    kk.setValue(
    """
tracker = nuke.thisNode() 
cornerPinOption = tracker.knob("cornerPinOptions").getValue() 
if cornerPinOption == 0: 
	tracker.knob("createPinUseCurrentFrame").execute() 
elif cornerPinOption == 1: 
	tracker.knob("createPinUseReferenceFrame").execute() 
elif cornerPinOption == 2: 
	tracker.knob("createPinUseCurrentFrameBaked").execute() 
elif cornerPinOption == 3: 
	tracker.knob("createPinUseReferenceFrameBaked").execute() 
elif cornerPinOption == 4: 
	tracker.knob("createTransformStabilize").execute() 
elif cornerPinOption == 5: 
	tracker.knob("createTransformMatchMove").execute() 
elif cornerPinOption == 6: 
	tracker.knob("createTransformStabilizeBaked").execute() 
elif cornerPinOption == 7: 
	tracker.knob("createTransformMatchMoveBaked").execute() 
elif cornerPinOption == 8: 
	tracker.knob("createPPinUseCurrentFrameBaked").execute() 
elif cornerPinOption == 9: 
	tracker.knob("createPPinUseReferenceFrameBaked").execute()
    """
    )



def createPPinUseReferenceFrameBaked():
    def fourCornersOfAConvexPoly(t): 
      tracker = nuke.thisNode() 
      k = tracker['selected_tracks'] 
      tracks = tracker['tracks'] 
      sa = k.getText().split(',') 
      if len(sa) != 4: 
        idx = [] 
        return idx 
      i = [int(sa[0]), int(sa[1]), int(sa[2]), int(sa[3])] 
      nCols = 31
      xCol = 2
      yCol = 3
      x = [tracks.getValueAt(t, i[0]*nCols+xCol), tracks.getValueAt(t, i[1]*nCols+xCol), tracks.getValueAt(t, i[2]*nCols+xCol), tracks.getValueAt(t, i[3]*nCols+xCol)] 
      y = [tracks.getValueAt(t, i[0]*nCols+yCol), tracks.getValueAt(t, i[1]*nCols+yCol), tracks.getValueAt(t, i[2]*nCols+yCol), tracks.getValueAt(t, i[3]*nCols+yCol)] 
      import math 
      mx = sum(x) / 4 
      my = sum(y) / 4 
      x = [x[0] - mx, x[1] - mx, x[2] - mx, x[3] - mx] 
      y = [y[0] - my, y[1] - my, y[2] - my, y[3] - my] 
      a = [math.pi + math.atan2(y[0],x[0]), math.pi + math.atan2(y[1],x[1]), math.pi + math.atan2(y[2],x[2]), math.pi + math.atan2(y[3],x[3])] 
      idx = sorted(range(len(i)),key=a.__getitem__) 
      idx = [i[idx[0]], i[idx[1]], i[idx[2]], i[idx[3]] ] 
      return idx 
    
    tracker = nuke.thisNode() 
    curframe = tracker['reference_frame'].getValue() 
    idx = fourCornersOfAConvexPoly(curframe) 
    if len(idx) != 4: 
      nuke.critical('aePowerPin export needs exactly 4 tracks selected.') 
    else: 
      x = tracker.xpos() 
      y = tracker.ypos() 
      w = tracker.screenWidth() 
      h = tracker.screenHeight() 
      m = int(x + w/2) 
      numviews = len( nuke.views() ) 
      root = nuke.root()
      root.begin()  
      pin =  nuke.nodes.aePowerPin() 
      pin.setInput(0,None) 
      pin.setXYpos(int(x+50), int(y+50)) 
      root.end()
      toKnobs = ["to1", "to2", "to3", "to4"] 
      fromKnobs =["from1", "from2", "from3", "from4"] 
      for i in range(len(idx)): 
        k = tracker['tracks'] 
        xIdx = idx[i] * 31 + 2
        yIdx = idx[i] * 31 + 3
        p = pin[toKnobs[i]] 
        p.setAnimated(0) 
        p.setAnimated(1) 
        for Idx in range(k.getNumKeys(xIdx)): 
          t = k.getKeyTime(Idx, xIdx) 
          p.setValueAt(k.getValueAt(t,xIdx), t, 0) 
        for Idx in range(k.getNumKeys(yIdx)): 
          t = k.getKeyTime(Idx, yIdx) 
          p.setValueAt(k.getValueAt(t,yIdx), t, 1) 
    
        p = pin[fromKnobs[i]] 
        p.setValue(k.getValueAt(curframe,xIdx),0) 
        p.setValue(k.getValueAt(curframe,yIdx),1) 
    
    tracker.knob("cornerPinOptions").setValue(0)
    #  pin.knob("label").setValue("using reference frame") 
    










def createPPinUseCurrentFrameBaked():
    
    def fourCornersOfAConvexPoly(t): 
      tracker = nuke.thisNode() 
      k = tracker['selected_tracks'] 
      tracks = tracker['tracks'] 
      sa = k.getText().split(',') 
      if len(sa) != 4: 
        idx = [] 
        return idx 
      i = [int(sa[0]), int(sa[1]), int(sa[2]), int(sa[3])] 
      nCols = 31
      xCol = 2
      yCol = 3
      x = [tracks.getValueAt(t, i[0]*nCols+xCol), tracks.getValueAt(t, i[1]*nCols+xCol), tracks.getValueAt(t, i[2]*nCols+xCol), tracks.getValueAt(t, i[3]*nCols+xCol)] 
      y = [tracks.getValueAt(t, i[0]*nCols+yCol), tracks.getValueAt(t, i[1]*nCols+yCol), tracks.getValueAt(t, i[2]*nCols+yCol), tracks.getValueAt(t, i[3]*nCols+yCol)] 
      import math 
      mx = sum(x) / 4 
      my = sum(y) / 4 
      x = [x[0] - mx, x[1] - mx, x[2] - mx, x[3] - mx] 
      y = [y[0] - my, y[1] - my, y[2] - my, y[3] - my] 
      a = [math.pi + math.atan2(y[0],x[0]), math.pi + math.atan2(y[1],x[1]), math.pi + math.atan2(y[2],x[2]), math.pi + math.atan2(y[3],x[3])] 
      idx = sorted(range(len(i)),key=a.__getitem__) 
      idx = [i[idx[0]], i[idx[1]], i[idx[2]], i[idx[3]] ] 
      return idx 
    
    tracker = nuke.thisNode() 
    curframe = nuke.frame() 
    idx = fourCornersOfAConvexPoly(curframe) 
    if len(idx) != 4: 
      nuke.critical('aePowerPin export needs exactly 4 tracks selected.') 
    else: 
      root = nuke.root()
      root.begin()
      x = tracker.xpos() 
      y = tracker.ypos() 
      w = tracker.screenWidth() 
      h = tracker.screenHeight() 
      m = int(x + w/2) 
      numviews = len( nuke.views() ) 
      pin =  nuke.nodes.aePowerPin() 
      pin.setInput(0,None) 
      pin.setXYpos(int(x+50), int(y+50)) 
      toKnobs = ["to1", "to2", "to3", "to4"] 
      fromKnobs =["from1", "from2", "from3", "from4"] 
      root.end()
      for i in range(len(idx)): 
        k = tracker['tracks'] 
        xIdx = idx[i] * 31 + 2
        yIdx = idx[i] * 31 + 3
        p = pin[toKnobs[i]] 
        p.setAnimated(0) 
        p.setAnimated(1) 
        for tIdx in range(k.getNumKeys(xIdx)): 
          t = k.getKeyTime(tIdx, xIdx) 
          p.setValueAt(k.getValueAt(t,xIdx), t, 0) 
        for tIdx in range(k.getNumKeys(yIdx)): 
          t = k.getKeyTime(tIdx, yIdx) 
          p.setValueAt(k.getValueAt(t,yIdx), t, 1) 
    
        p = pin[fromKnobs[i]] 
        p.setValue(k.getValueAt(curframe,xIdx),0) 
        p.setValue(k.getValueAt(curframe,yIdx),1) 
    tracker.knob('cornerPinOptions').setValue(0)
    
    #  pin.knob("label").setValue("using reference frame") 




#######################################################################################################




def creation_planar():
    node = nuke.thisNode()
    tab = nuke.Tab_Knob('button', 'button')
    tab.setVisible(False)
    tab.setFlag(0x0000000000000400)
    node.addKnob(tab)
    
    node.knob('export_menu').setValue(0)

    m = nuke.PyScript_Knob("createPowerRelative","createPowerRelative","import aePowerPinFun\naePowerPinFun.createPowerRelative()")
    node.addKnob(m)
    
    m = nuke.PyScript_Knob("createPowerAbsolute","createPowerAbsolute","import aePowerPinFun\naePowerPinFun.createPowerAbsolute()")
    node.addKnob(m)
    
    m = nuke.PyScript_Knob("createPowerStabilize","createPowerStabilize","import aePowerPinFun\naePowerPinFun.createPowerStabilize()")
    node.addKnob(m)

    n = nuke.thisNode()
    k = n['export_menu']
    list = k.values()
    list.append('aePowerPin (relative)')
    list.append('aePowerPin (absolute)')
    list.append('aePowerPin (stabilize)')

    print list
    k.setValues(list)
    print k.values()

    kk = n['export_button']

    kk.setValue(
    """
ptracker = nuke.thisNode() 
cornerPinOption = ptracker.knob("export_menu").getValue() 
linkOutput = ptracker.knob("link_output").getValue() 
if cornerPinOption == 0: 
  if linkOutput == 1: 
    ptracker.knob("create_pin_relative").execute() 
  else: 
    ptracker.knob("create_pin_relative_baked").execute() 
elif cornerPinOption == 1: 
  if linkOutput == 1: 
    ptracker.knob("create_pin_absolute").execute() 
  else: 
    ptracker.knob("create_pin_absolute_baked").execute() 
elif cornerPinOption == 2: 
  if linkOutput == 1: 
    ptracker.knob("create_pin_stabilize").execute() 
  else: 
    ptracker.knob("create_pin_stabilize_baked").execute() 
elif cornerPinOption == 3: 
  if linkOutput == 1: 
    ptracker.knob("create_tracker").execute() 
  else: 
    ptracker.knob("create_tracker_baked").execute() 

elif cornerPinOption == 4: 
    ptracker.knob("createPowerRelative").execute() 
elif cornerPinOption == 5: 
    ptracker.knob("createPowerAbsolute").execute() 
elif cornerPinOption == 6: 
    ptracker.knob("createPowerStabilize").execute() 

    """
    )






def createPowerRelative():
    
    ptracker = nuke.thisNode()
    x = ptracker.xpos() 
    y = ptracker.ypos() 
    w = ptracker.screenWidth() 
    h = ptracker.screenHeight() 
    m = int(x + w/2) 
    numviews = len( nuke.views() ) 
    
    root = nuke.root()
    root.begin()
    pin = nuke.nodes.aePowerPin() 
    pin.setInput(0,None) 
    pin.setXYpos(x+50, y + 50) 
    root.end()
    inKnobs = ["pt1", "pt2", "pt3", "pt4"] 
    outKnobs = ["to1", "to2", "to3", "to4"] 
    for i in range(len(inKnobs)): 
      k = ptracker[inKnobs[i]] 
      p = pin[outKnobs[i]] 
      p.setAnimated(0) 
      p.setAnimated(1) 
      for Idx in range(k.getNumKeys()): 
        t = k.getKeyTime(Idx) 
        p.setValueAt(k.getValueAt(t,0), t, 0) 
        p.setValueAt(k.getValueAt(t,1), t, 1) 
    referenceFrame = ptracker.knob("reference_frame").getValue() 
    pin["from1"].setValue(ptracker.knob("pt1").getValueAt(referenceFrame,0),0) 
    pin["from1"].setValue(ptracker.knob("pt1").getValueAt(referenceFrame,1),1) 
    pin["from2"].setValue(ptracker.knob("pt2").getValueAt(referenceFrame,0),0) 
    pin["from2"].setValue(ptracker.knob("pt2").getValueAt(referenceFrame,1),1) 
    pin["from3"].setValue(ptracker.knob("pt3").getValueAt(referenceFrame,0),0) 
    pin["from3"].setValue(ptracker.knob("pt3").getValueAt(referenceFrame,1),1) 
    pin["from4"].setValue(ptracker.knob("pt4").getValueAt(referenceFrame,0),0) 
    pin["from4"].setValue(ptracker.knob("pt4").getValueAt(referenceFrame,1),1) 
    pin["label"].setValue("relative, baked") 
    



def createPowerAbsolute():
    
    ptracker = nuke.thisNode()
    root = nuke.root()
    root.begin()
    pin = nuke.nodes.aePowerPin() 
    root.end()
    x = ptracker.xpos() 
    y = ptracker.ypos() 
    w = ptracker.screenWidth() 
    h = ptracker.screenHeight() 
    m = int(x + w/2) 
    numviews = len( nuke.views() ) 
    connectNode = None 
    try: 
      connectNode = ptracker.input(0) 
    except: 
      pass 
    try: 
      connectNode = nuke.selectedNode() 
    except: 
      pass 
    
    if not connectNode == None: 
      pin.setInput(0,None) 
      pin.setXYpos(x+50, y + 50) 
    
      width = connectNode.width() 
      height = connectNode.height() 
    
      inKnobs = ["pt1", "pt2", "pt3", "pt4"] 
      outKnobs = ["to1", "to2", "to3", "to4"] 
      for i in range(len(inKnobs)): 
        k = ptracker[inKnobs[i]] 
        p = pin[outKnobs[i]] 
        p.setAnimated(0) 
        p.setAnimated(1) 
        for Idx in range(k.getNumKeys()): 
          t = k.getKeyTime(Idx) 
          p.setValueAt(k.getValueAt(t,0), t, 0) 
          p.setValueAt(k.getValueAt(t,1), t, 1) 
    
      pin.knob("from1").setValue(0,0) 
      pin.knob("from1").setValue(0,1) 
      pin.knob("from2").setValue(width,0) 
      pin.knob("from2").setValue(0,1) 
      pin.knob("from3").setValue(width,0) 
      pin.knob("from3").setValue(height,1) 
      pin.knob("from4").setValue(0,0) 
      pin.knob("from4").setValue(height,1) 
      pin["label"].setValue("absolute, baked") 



def createPowerStabilize():
    
    ptracker = nuke.thisNode() 
    x = ptracker.xpos() 
    y = ptracker.ypos() 
    w = ptracker.screenWidth() 
    h = ptracker.screenHeight() 
    m = int(x + w/2) 
    
    root = nuke.root()
    root.begin()
    pin = nuke.nodes.aePowerPin() 
    pin.setInput(0,None) 
    pin.setXYpos(x+50, y + 50) 
    root.end()
    inKnobs = ["pt1", "pt2", "pt3", "pt4"] 
    outKnobs = ["to1", "to2", "to3", "to4"] 
    for i in range(len(inKnobs)): 
      k = ptracker[inKnobs[i]] 
      p = pin[outKnobs[i]] 
      p.setAnimated(0) 
      p.setAnimated(1) 
      for Idx in range(k.getNumKeys()): 
        t = k.getKeyTime(Idx) 
        p.setValueAt(k.getValueAt(t,0), t, 0) 
        p.setValueAt(k.getValueAt(t,1), t, 1) 
    referenceFrame = ptracker.knob("reference_frame").getValue() 
    pin["from1"].setValue(ptracker.knob("pt1").getValueAt(referenceFrame,0),0) 
    pin["from1"].setValue(ptracker.knob("pt1").getValueAt(referenceFrame,1),1) 
    pin["from2"].setValue(ptracker.knob("pt2").getValueAt(referenceFrame,0),0) 
    pin["from2"].setValue(ptracker.knob("pt2").getValueAt(referenceFrame,1),1) 
    pin["from3"].setValue(ptracker.knob("pt3").getValueAt(referenceFrame,0),0) 
    pin["from3"].setValue(ptracker.knob("pt3").getValueAt(referenceFrame,1),1) 
    pin["from4"].setValue(ptracker.knob("pt4").getValueAt(referenceFrame,0),0) 
    pin["from4"].setValue(ptracker.knob("pt4").getValueAt(referenceFrame,1),1) 
    
    try: 
      connectNode = ptracker.input(0) 
    except: 
      connectNode = None 
    try: 
      connectNode = ptracker 
    except: 
      pass 
    
    if not connectNode == None: 
    	pin.setInput(0,None) 
    	pin.setXYpos(m + 50, y+50) 
    	pin["inv"].setValue(True) 
    	pin["label"].setValue("stabilize, baked") 
