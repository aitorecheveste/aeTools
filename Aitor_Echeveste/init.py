# python
import os
# nuke
import nuke



dirname = os.path.dirname(os.path.abspath(__file__))
nuke.pluginAddPath(os.path.join(dirname, 'Aitor_Echeveste'))



dirname, filename = os.path.split(os.path.abspath(__file__))

for root, dirs, files in os.walk(dirname):
    nuke.pluginAddPath(root)


