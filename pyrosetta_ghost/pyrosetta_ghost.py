

import pyrosetta
from pyrosetta import *
from pyrosetta.rosetta import *

try:
    m = pyrosetta.rosetta.protocols.simple_moves.MinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.MinMover = pyrosetta.rosetta.protocols.minimization_packing.MinMover

try:
    m = rosetta.protocols.simple_moves.MinMover
except AttributeError:
    rosetta.protocols.simple_moves.MinMover = rosetta.protocols.minimization_packing.MinMover

try:
    m = protocols.simple_moves.MinMover
except AttributeError:
    protocols.simple_moves.MinMover = protocols.minimization_packing.MinMover

try:
    m = pyrosetta.rosetta.protocols.simple_moves.BoltzmannRotamerMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.BoltzmannRotamerMover = pyrosetta.rosetta.protocols.minimization_packing.BoltzmannRotamerMover

try:
    m = rosetta.protocols.simple_moves.BoltzmannRotamerMover
except AttributeError:
    rosetta.protocols.simple_moves.BoltzmannRotamerMover = rosetta.protocols.minimization_packing.BoltzmannRotamerMover

try:
    m = protocols.simple_moves.BoltzmannRotamerMover
except AttributeError:
    protocols.simple_moves.BoltzmannRotamerMover = protocols.minimization_packing.BoltzmannRotamerMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.EvolutionaryDynamicsMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.EvolutionaryDynamicsMover = pyrosetta.rosetta.protocols.minimization_packing.EvolutionaryDynamicsMover

try:
    m = rosetta.protocols.simple_moves.EvolutionaryDynamicsMover
except AttributeError:
    rosetta.protocols.simple_moves.EvolutionaryDynamicsMover = rosetta.protocols.minimization_packing.EvolutionaryDynamicsMover

try:
    m = protocols.simple_moves.EvolutionaryDynamicsMover
except AttributeError:
    protocols.simple_moves.EvolutionaryDynamicsMover = protocols.minimization_packing.EvolutionaryDynamicsMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.ExtendedPoseMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.ExtendedPoseMover = pyrosetta.rosetta.protocols.minimization_packing.ExtendedPoseMover

try:
    m = rosetta.protocols.simple_moves.ExtendedPoseMover
except AttributeError:
    rosetta.protocols.simple_moves.ExtendedPoseMover = rosetta.protocols.minimization_packing.ExtendedPoseMover

try:
    m = protocols.simple_moves.ExtendedPoseMover
except AttributeError:
    protocols.simple_moves.ExtendedPoseMover = protocols.minimization_packing.ExtendedPoseMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.ExtendedPoseMoverCreator
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.ExtendedPoseMoverCreator = pyrosetta.rosetta.protocols.minimization_packing.ExtendedPoseMoverCreator

try:
    m = rosetta.protocols.simple_moves.ExtendedPoseMoverCreator
except AttributeError:
    rosetta.protocols.simple_moves.ExtendedPoseMoverCreator = rosetta.protocols.minimization_packing.ExtendedPoseMoverCreator

try:
    m = protocols.simple_moves.ExtendedPoseMoverCreator
except AttributeError:
    protocols.simple_moves.ExtendedPoseMoverCreator = protocols.minimization_packing.ExtendedPoseMoverCreator


try:
    m = pyrosetta.rosetta.protocols.simple_moves.GreenPacker
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.GreenPacker = pyrosetta.rosetta.protocols.minimization_packing.GreenPacker

try:
    m = rosetta.protocols.simple_moves.GreenPacker
except AttributeError:
    rosetta.protocols.simple_moves.GreenPacker = rosetta.protocols.minimization_packing.GreenPacker

try:
    m = protocols.simple_moves.GreenPacker
except AttributeError:
    protocols.simple_moves.GreenPacker = protocols.minimization_packing.GreenPacker


try:
    m = pyrosetta.rosetta.protocols.simple_moves.MakePolyXMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.MakePolyXMover = pyrosetta.rosetta.protocols.minimization_packing.MakePolyXMover

try:
    m = rosetta.protocols.simple_moves.MakePolyXMover
except AttributeError:
    rosetta.protocols.simple_moves.MakePolyXMover = rosetta.protocols.minimization_packing.MakePolyXMover

try:
    m = protocols.simple_moves.MakePolyXMover
except AttributeError:
    protocols.simple_moves.MakePolyXMover = protocols.minimization_packing.MakePolyXMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.MinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.MinMover = pyrosetta.rosetta.protocols.minimization_packing.MinMover

try:
    m = rosetta.protocols.simple_moves.MinMover
except AttributeError:
    rosetta.protocols.simple_moves.MinMover = rosetta.protocols.minimization_packing.MinMover

try:
    m = protocols.simple_moves.MinMover
except AttributeError:
    protocols.simple_moves.MinMover = protocols.minimization_packing.MinMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.MinPackMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.MinPackMover = pyrosetta.rosetta.protocols.minimization_packing.MinPackMover

try:
    m = rosetta.protocols.simple_moves.MinPackMover
except AttributeError:
    rosetta.protocols.simple_moves.MinPackMover = rosetta.protocols.minimization_packing.MinPackMover

try:
    m = protocols.simple_moves.MinPackMover
except AttributeError:
    protocols.simple_moves.MinPackMover = protocols.minimization_packing.MinPackMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.PackRotamersMoverLazy
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.PackRotamersMoverLazy = pyrosetta.rosetta.protocols.minimization_packing.PackRotamersMoverLazy

try:
    m = rosetta.protocols.simple_moves.PackRotamersMoverLazy
except AttributeError:
    rosetta.protocols.simple_moves.PackRotamersMoverLazy = rosetta.protocols.minimization_packing.PackRotamersMoverLazy

try:
    m = protocols.simple_moves.PackRotamersMoverLazy
except AttributeError:
    protocols.simple_moves.PackRotamersMoverLazy = protocols.minimization_packing.PackRotamersMoverLazy


try:
    m = pyrosetta.rosetta.protocols.simple_moves.PeptideStapleMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.PeptideStapleMover = pyrosetta.rosetta.protocols.minimization_packing.PeptideStapleMover

try:
    m = rosetta.protocols.simple_moves.PeptideStapleMover
except AttributeError:
    rosetta.protocols.simple_moves.PeptideStapleMover = rosetta.protocols.minimization_packing.PeptideStapleMover

try:
    m = protocols.simple_moves.PeptideStapleMover
except AttributeError:
    protocols.simple_moves.PeptideStapleMover = protocols.minimization_packing.PeptideStapleMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.PertMinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.PertMinMover = pyrosetta.rosetta.protocols.minimization_packing.PertMinMover

try:
    m = rosetta.protocols.simple_moves.PertMinMover
except AttributeError:
    rosetta.protocols.simple_moves.PertMinMover = rosetta.protocols.minimization_packing.PertMinMover

try:
    m = protocols.simple_moves.PertMinMover
except AttributeError:
    protocols.simple_moves.PertMinMover = protocols.minimization_packing.PertMinMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.RepackSidechainsMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.RepackSidechainsMover = pyrosetta.rosetta.protocols.minimization_packing.RepackSidechainsMover

try:
    m = rosetta.protocols.simple_moves.RepackSidechainsMover
except AttributeError:
    rosetta.protocols.simple_moves.RepackSidechainsMover = rosetta.protocols.minimization_packing.RepackSidechainsMover

try:
    m = protocols.simple_moves.RepackSidechainsMover
except AttributeError:
    protocols.simple_moves.RepackSidechainsMover = protocols.minimization_packing.RepackSidechainsMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.RotamerTrialsMinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.RotamerTrialsMinMover = pyrosetta.rosetta.protocols.minimization_packing.RotamerTrialsMinMover

try:
    m = rosetta.protocols.simple_moves.RotamerTrialsMinMover
except AttributeError:
    rosetta.protocols.simple_moves.RotamerTrialsMinMover = rosetta.protocols.minimization_packing.RotamerTrialsMinMover

try:
    m = protocols.simple_moves.RotamerTrialsMinMover
except AttributeError:
    protocols.simple_moves.RotamerTrialsMinMover = protocols.minimization_packing.RotamerTrialsMinMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.RotamerTrialsMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.RotamerTrialsMover = pyrosetta.rosetta.protocols.minimization_packing.RotamerTrialsMover

try:
    m = rosetta.protocols.simple_moves.RotamerTrialsMover
except AttributeError:
    rosetta.protocols.simple_moves.RotamerTrialsMover = rosetta.protocols.minimization_packing.RotamerTrialsMover

try:
    m = protocols.simple_moves.RotamerTrialsMover
except AttributeError:
    protocols.simple_moves.RotamerTrialsMover = protocols.minimization_packing.RotamerTrialsMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.RotamerizeMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.RotamerizeMover = pyrosetta.rosetta.protocols.minimization_packing.RotamerizeMover

try:
    m = rosetta.protocols.simple_moves.RotamerizeMover
except AttributeError:
    rosetta.protocols.simple_moves.RotamerizeMover = rosetta.protocols.minimization_packing.RotamerizeMover

try:
    m = protocols.simple_moves.RotamerizeMover
except AttributeError:
    protocols.simple_moves.RotamerizeMover = protocols.minimization_packing.RotamerizeMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.SaneMinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.SaneMinMover = pyrosetta.rosetta.protocols.minimization_packing.SaneMinMover

try:
    m = rosetta.protocols.simple_moves.SaneMinMover
except AttributeError:
    rosetta.protocols.simple_moves.SaneMinMover = rosetta.protocols.minimization_packing.SaneMinMover

try:
    m = protocols.simple_moves.SaneMinMover
except AttributeError:
    protocols.simple_moves.SaneMinMover = protocols.minimization_packing.SaneMinMover


try:
    m = pyrosetta.rosetta.protocols.simple_moves.TaskAwareMinMover
except AttributeError:
    pyrosetta.rosetta.protocols.simple_moves.TaskAwareMinMover = pyrosetta.rosetta.protocols.minimization_packing.TaskAwareMinMover

try:
    m = rosetta.protocols.simple_moves.TaskAwareMinMover
except AttributeError:
    rosetta.protocols.simple_moves.TaskAwareMinMover = rosetta.protocols.minimization_packing.TaskAwareMinMover

try:
    m = protocols.simple_moves.TaskAwareMinMover
except AttributeError:
    protocols.simple_moves.TaskAwareMinMover = protocols.minimization_packing.TaskAwareMinMover




