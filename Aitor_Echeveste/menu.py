# AITOR ECHEVESTE TOOLS

toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Aitor Echeveste", icon="AitorEchevesteNukeLogo.png")

# Latest tools
m.addCommand("aeVolumeRays", "nuke.createNode(\"aeVolumeRays\")", icon="aeVolumeRays_icon.png")
m.addCommand("aeAutoMorph", "nuke.createNode(\"aeAutoMorph\")")

# Matte / cleanup
m.addCommand("aeBrokenEdges", "nuke.createNode(\"aeBrokenEdges\")", icon="BrokenEdges_icon.png")
m.addCommand("aeFiller", "nuke.createNode(\"aeFiller\")", icon="aeFiller_icon.png")
m.addCommand("aeBrokenShapes", "nuke.createNode(\"aeBrokenShapes\")", icon="BrokenShapes_icon.png")

# Tracking / transforms / motion
m.addCommand("aePowerPin", "nuke.createNode(\"aePowerPin\")", icon="aePowerPin_icon.png")
m.addCommand("aeTransform", "nuke.createNode(\"aeTransform\")", icon="aeTransform_icon.png")
m.addCommand("aeMotionBlur", "nuke.createNode(\"aeMotionBlur\")", icon="aeMotionBlur_icon.png")
m.addCommand("iSTMap", "nuke.createNode(\"iSTMap\")", icon="iSTMap_icon.png")

# Lighting / integration
m.addCommand("aeRelight2D", "nuke.createNode(\"aeRelight2D\")", icon="aeReLight2D_icon.png")
m.addCommand("aeShadows", "nuke.createNode(\"aeShadows\")", icon="aeShadows_icon.png")
m.addCommand("aeDirtCG", "nuke.createNode(\"aeDirtCG\")", icon="aeDirtCG_icon.png")
m.addCommand("aeRefracTHOR", "nuke.createNode(\"aeRefracTHOR\")", icon="aeRefracTHOR_icon.png")
m.addCommand("aeAnamorphic", "nuke.createNode(\"aeAnamorphic\")", icon="aeAnamorphic_icon.png")

# 3D utilities
m.addCommand("aePrefMaker", "nuke.createNode(\"aePrefMaker\")", icon="aePrefMaker_icon.png")
m.addCommand("aeUVChart", "nuke.createNode(\"aeUVChart\")", icon="aeUVChart_icon.png")
