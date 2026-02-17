import os
import json


def get_project_root(base_dir: str) -> str:
    """
    Returns root simulation directory inside base_dir.
    """
    root = os.path.join(base_dir, "michrom_simulations")
    os.makedirs(root, exist_ok=True)
    return root


def get_run_directory(base_dir: str, run_id: str) -> str:
    root = get_project_root(base_dir)
    run_dir = os.path.join(root, run_id)
    os.makedirs(run_dir, exist_ok=True)
    return run_dir


def get_replica_directory(base_dir: str, run_id: str, replica_id: int) -> str:
    run_dir = get_run_directory(base_dir, run_id)
    rep_dir = os.path.join(run_dir, f"replica_{replica_id:03d}")
    os.makedirs(rep_dir, exist_ok=True)
    return rep_dir


def save_config(config, base_dir: str):
    run_dir = get_run_directory(base_dir, config.run_id)
    path = os.path.join(run_dir, "config.json")

    with open(path, "w") as f:
        json.dump(config.to_dict(), f, indent=4)
