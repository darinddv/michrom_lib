import os


def create_chromseq_file(rep_dir: str, n_beads: int, default_type: str) -> str:
    """
    Creates a simple ChromSeq file with uniform bead types.
    """

    path = os.path.join(rep_dir, "chromseq.txt")

    with open(path, "w") as f:
        for i in range(1, n_beads + 1):
            f.write(f"{i} {default_type}\n")

    return path
