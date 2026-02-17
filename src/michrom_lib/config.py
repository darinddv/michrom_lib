from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class SimulationConfig:
    """
    Core simulation configuration.

    This object contains ONLY parameters that define the experiment.
    It does not contain filesystem paths or runtime state.
    """

    # ---- Identity ----
    run_id: str

    # ---- Polymer ----
    n_beads: int
    default_type: str = "A1"

    # ---- Platform ----
    platform: str = "cpu"
    precision: str = "mixed"
    integrator: str = "langevin"

    # ---- Thermodynamics ----
    temperature: float = 1.0
    timeStep: float = 0.01

    # ---- Bonded forces ----
    kFb: float = 30.0
    kA: float = 2.0
    eCut: float = 4.0

    # ---- Nonbonded forces ----
    mu: float = 3.22
    rc: float = 1.78
    dinit: int = 3
    dend: int = 500

    # ---- Collapse force ----
    kR: float = 5e-3
    nRad: float = 15.0

    # ---- Collapse stage ----
    collapse_block: int = 300
    collapse_blocks: int = 500

    # ---- Production stage ----
    prod_block: int = 500
    prod_blocks: int = 200

    # ---- Replicas ----
    n_replicas: int = 1
    seed_base: int = 1000

    def to_dict(self):
        return asdict(self)
