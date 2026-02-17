from OpenMiChroM.ChromDynamics import MiChroM


def build_simulation(config, chromseq_path, seed: int):
    """
    Build MiChroM object and add forces.
    Does NOT run simulation.
    """

    sim = MiChroM(
        temperature=config.temperature,
        timeStep=config.timeStep
    )

    sim.setup(
        platform=config.platform,
        precision=config.precision,
        integrator=config.integrator,
        seed=seed
    )

    # Create initial structure
    structure = sim.createSpringSpiral(
        ChromSeq=chromseq_path,
        isRing=False
    )

    sim.loadStructure(structure, center=True)

    # Bonded forces
    sim.addFENEBonds(kFb=config.kFb)
    sim.addAngles(kA=config.kA)
    sim.addRepulsiveSoftCore(eCut=config.eCut)

    # Nonbonded forces
    sim.addTypetoType(mu=config.mu, rc=config.rc)
    sim.addIdealChromosome(
        mu=config.mu,
        rc=config.rc,
        dinit=config.dinit,
        dend=config.dend
    )

    return sim
