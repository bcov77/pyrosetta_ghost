

import pyrosetta

try:
    m = pyrosetta.rosetta.protocols.simple_moves.MinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.MinMover = pyrosetta.rosetta.protocols.minimization_packing.MinMover

try:
    m = pyrosetta.rosetta.protocols.simple_moves.BoltzmannRotamerMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.BoltzmannRotamerMover = pyrosetta.rosetta.protocols.minimization_packing.BoltzmannRotamerMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.EvolutionaryDynamicsMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.EvolutionaryDynamicsMover = pyrosetta.rosetta.protocols.evolution.EvolutionaryDynamicsMover



try:
    m = pyrosetta.rosetta.protocols.simple_moves.ExtendedPoseMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.ExtendedPoseMover = pyrosetta.rosetta.protocols.pose_creation.ExtendedPoseMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.ExtendedPoseMoverCreator
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.ExtendedPoseMoverCreator = pyrosetta.rosetta.protocols.pose_creation.ExtendedPoseMoverCreator


try:
    m = pyrosetta.rosetta.protocols.simple_moves.GreenPacker
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.GreenPacker = pyrosetta.rosetta.protocols.minimization_packing.GreenPacker



try:
    m = pyrosetta.rosetta.protocols.simple_moves.MakePolyXMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.MakePolyXMover = pyrosetta.rosetta.protocols.pose_creation.MakePolyXMover



try:
    m = pyrosetta.rosetta.protocols.simple_moves.MinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.MinMover = pyrosetta.rosetta.protocols.minimization_packing.MinMover



try:
    m = pyrosetta.rosetta.protocols.simple_moves.MinPackMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.MinPackMover = pyrosetta.rosetta.protocols.minimization_packing.MinPackMover



try:
    m = pyrosetta.rosetta.protocols.simple_moves.PackRotamersMoverLazy
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.PackRotamersMoverLazy = pyrosetta.rosetta.protocols.minimization_packing.PackRotamersMoverLazy



try:
    m = pyrosetta.rosetta.protocols.simple_moves.PeptideStapleMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.PeptideStapleMover = pyrosetta.rosetta.protocols.minimization_packing.PeptideStapleMover



try:
    m = pyrosetta.rosetta.protocols.simple_moves.PertMinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.PertMinMover = pyrosetta.rosetta.protocols.minimization_packing.PertMinMover



try:
    m = pyrosetta.rosetta.protocols.simple_moves.RepackSidechainsMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.RepackSidechainsMover = pyrosetta.rosetta.protocols.minimization_packing.RepackSidechainsMover



try:
    m = pyrosetta.rosetta.protocols.simple_moves.RotamerTrialsMinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.RotamerTrialsMinMover = pyrosetta.rosetta.protocols.minimization_packing.RotamerTrialsMinMover



try:
    m = pyrosetta.rosetta.protocols.simple_moves.RotamerTrialsMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.RotamerTrialsMover = pyrosetta.rosetta.protocols.minimization_packing.RotamerTrialsMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.RotamerizeMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.RotamerizeMover = pyrosetta.rosetta.protocols.minimization_packing.RotamerizeMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.SaneMinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.SaneMinMover = pyrosetta.rosetta.protocols.minimization_packing.SaneMinMover

try:
    m = pyrosetta.rosetta.protocols.simple_moves.TaskAwareMinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.TaskAwareMinMover = pyrosetta.rosetta.protocols.minimization_packing.TaskAwareMinMover





