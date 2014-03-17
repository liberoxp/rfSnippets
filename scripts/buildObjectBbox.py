# -*- coding: utf-8 -*-

"""This module defines a function to build bounding box.

   This module defines a function to a build bounding box object node
   for the given object node. User can transform this bbox node for 
   some purposes.

   Usage: 
       Import this module or open this script directly at Batch Script panel.

       target = scene.getObject('object_name')
       bbox = buildObjectBbox(target)

   Requirements:
     
       RealFlow 2013 (This module has only been tested on this version
                      , but should work as well on other versions.)
"""

def buildObjectBbox(targetObj=None, bboxName='bbox'):
    """ Build bounding box object. """

    if targetObj.getType()!=2:
        scene.message('[buildBbox] Warning! Target node is not Object type. Exit building process.')
        return None

    # Get bounding box info of target object.
    scene.message('[buildBbox] Gathering target bounding box info.')
    bbox = targetObj.getBoundingBox()
    p1 = bbox[0]
    p2 = bbox[1]
    x1, y1, z1 = p1.getZ(), p1.getY(), p1.getX() # TODO axis order in x-y-z will give incorrect result.
    x2, y2, z2 = p2.getZ(), p2.getY(), p2.getX()
    msg = '    Min Point: %s, %s, %s' % (x1, y1, z1)
    scene.message(msg)
    msg = '    Max Point: %s, %s, %s' % (x2, y2, z2)
    scene.message(msg)

    # Setup bounding box object vertexs.
    scene.message('[buildBbox] Preparing vertex data.')
    vtxs = []
    appendVertex(vtxs, [x1, y1, z1]) 
    appendVertex(vtxs, [x1, y1, z2])
    appendVertex(vtxs, [x2, y1, z2])
    appendVertex(vtxs, [x2, y1, z1])
    appendVertex(vtxs, [x1, y2, z1])
    appendVertex(vtxs, [x1, y2, z2])
    appendVertex(vtxs, [x2, y2, z2])
    appendVertex(vtxs, [x2, y2, z1])

    # Setup bounding box object faces.
    scene.message('[buildBbox] Preparing face data.')
    faces = [
        Face.new(0, 2, 1), Face.new(0, 3, 2),
        Face.new(4, 5, 6), Face.new(4, 6, 7),
        Face.new(0, 1, 5), Face.new(0, 5, 4),
        Face.new(1, 2, 6), Face.new(1, 6, 5),
        Face.new(2, 3, 7), Face.new(2, 7, 6),
        Face.new(3, 0, 4), Face.new(3, 4, 7),
    ]

    # Create bounding box object.
    scene.message('[buildBbox] Creating bounding box object.')
    bboxObj = scene.addObject(bboxName, vtxs, faces)
    bboxObj.setName(bboxName)

    scene.message('[buildBbox] Bounding box object has been built.')
    return bboxObj

def appendVertex(vtxs=[], pos=[0, 0, 0]):
    """ Append vertex object to given list and position. """

    vtxs.append(Vertex.new(Vector.new(pos[0], pos[1], pos[2])))

