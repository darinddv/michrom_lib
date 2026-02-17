import os
from .paths import get_replica_directory, save_config
from .chromseq import create_chromseq_file
from .build import build_simulation


def run_replica(base_dir: str, config, replica_id: int):

    rep_dir = get_replica_directory(base_dir, config.run_id, replica_id)

    # Save config once
    if replica_id == 0:
        save_config(config, base_dir)

    chromseq_path = create_chromseq_file(
        rep_dir,
        config.n_beads,
        config.default_type
    )

    #seed = config.seed_base + replica_id

    sim = build_simulation(config, 
                           chromseq_path, 
                           #seed
                          )

    sim.saveFolder(rep_dir)

    # ---- Collapse Stage ----
    sim.addFlatBottomHarmonic(kR=config.kR, nRad=config.nRad)
    sim.createSimulation()

    sim.run(
        nsteps=config.collapse_block * config.collapse_blocks,
        checkSystem=True,
        report=True,
        blockSize=config.collapse_block
    )

    sim.removeFlatBottomHarmonic()

    # ---- Production Stage ----
    sim.createReporters(
        statistics=True,
        traj=True,
        outputName="traj",
        trajFormat="cndb",
        energyComponents=True,
        interval=config.prod_block
    )

    for _ in range(config.prod_blocks):
        sim.run(config.prod_block)

    return rep_dir

