"""Example of yaml for the PDB id: x0161 and 6lu7 (not yet implemented).
"""
r_x0161 = """
main:
  type: GA
  njobs: 2
  seed_smiles: COC(=O)C=1C=CC(=CC1)S(=O)(=O)N
  costfunc: Cost
  costfunc_kwargs:
    vina_executable: vina
    receptor_path: x0161.pdbqt
    boxcenter:
      - 12.11
      - 1.84
      - 23.56
    boxsize:
      - 22.5
      - 22.5
      - 22.5
    exhaustiveness: 4
    ncores: 6
    num_modes: 1
  crem_db_path: /home/ale/GITLAB/bi_crem_database/replacements02_sc2.5.db
  maxiter: 2
  popsize: 2
  beta: 0.001
  pc: 1
  get_similar: False
  mutate_crem_kwargs:
    radius: 3
    min_size: 1
    max_size: 8
    min_inc: -5
    max_inc: 3
    ncores: 12
"""
r_6lu7 = None