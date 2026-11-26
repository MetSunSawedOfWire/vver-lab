# VVER-Lab: Reactor Physics & Core Modeling

Computational laboratory for neutron-physical modeling and thermal-hydraulic analysis of **VVER-1200** pressurized water reactors. Built from scratch using modern Python engineering practices, vectorized numerics, and high-performance computing tools.

## Project Objectives
* **Neutronics & Core Physics:** Implementation of four-factor formula (\(k_\infty\)), 1D/2D multigroup diffusion solvers, xenon-135 transient dynamics, and Monte Carlo neutron transport.
* **Engineering Software Practices:** Strict type hinting (`typing`), immutable physical data structures (`dataclasses`), automated unit testing (`pytest`), and profiling (`cProfile`, `timeit`).
* **High-Performance Computing:** Transition from pure Python to vectorized `NumPy` arrays, JIT-compilation (`Numba`), and compiled extensions.

---

## Repository Structure

```text
vver-lab/
├── nuclear_data.py        # Immutable database of thermal neutron cross-sections (U-235, U-238, H-1, B-10)
├── soon...  # Unit tests for macroscopic cross-sections and physical constraints
└── README.md              # Project documentation and roadmap progress
```

---

## Roadmap 

- [x] **Week 1:** Environment setup, and VVER-1200 core architecture fundamentals.
- [x] **Week 2:** Engineering Python (`dataclasses`, `typing`, `pytest`) & `nuclear_data.py` module.
- [ ] **Week 3:** Vectorized $k_\infty$ calculator (`NumPy` broadcasting) & performance profiling (`timeit`, `cProfile`).
- [ ] **Phase 2:** 1D/2D Neutron Diffusion Solver & Criticality search.
- [ ] **Phase 3:** Xenon-135 poisoning dynamics & power maneuvering simulation.
- [ ] **Phase 4:** Monte Carlo neutron transport & `Numba` acceleration.

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com
cd vver-lab
```

### 2. Set up virtual environment & install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest mypy numpy
```

### 3. Run unit tests
```bash
pytest
```

---

## Data Sources
Thermal neutron microscopic cross-sections ($E = 0.0253\text{ eV}$) used in `nuclear_data.py` are referenced against standard evaluated nuclear data libraries (**ENDF/B-VIII.0**).
