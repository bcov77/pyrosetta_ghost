#!/usr/bin/env python

import sys

a = sys.argv[1]
print "try:"
print "    m = pyrosetta.rosetta.protocols.simple_moves.%s"%a
print "except AttributeError:"
print "    pyrosetta.rosetta.protocols.simple_moves.%s = pyrosetta.rosetta.protocols.minimization_packing.%s"%(a, a)
print ""
print "try:"
print "    m = rosetta.protocols.simple_moves.%s"%a
print "except AttributeError:"
print "    rosetta.protocols.simple_moves.%s = rosetta.protocols.minimization_packing.%s"%(a, a)
print ""
print "try:"
print "    m = protocols.simple_moves.%s"%a
print "except AttributeError:"
print "    protocols.simple_moves.%s = protocols.minimization_packing.%s"%(a, a)
print ""
print ""