# Copilot Instructions for AI Coding Agents

## Project Overview
This project focuses on the numerical simulation of hyperbolic systems of conservation laws using the finite volume method. The main deliverables are a LaTeX report (`main.tex`) and supporting Python code (`src/main.py`).

## Key Files and Structure
- `main.tex`: Main LaTeX document for the report. Written in Spanish, includes mathematical definitions and project context.
- `src/main.py`: Python script. Currently only prints the Python version, but intended for numerical experiments or demonstrations.
- Other files: Images (`*.jpeg`), PDF references, and LaTeX build artifacts.

## Development Workflow
- **LaTeX Build**: Compile `main.tex` using a standard LaTeX toolchain (e.g., `pdflatex main.tex`).
- **Python Code**: Run scripts in `src/` with Python 3 (e.g., `python3 src/main.py`).
- **No automated tests or build scripts** are present. Add scripts to `src/` as needed for experiments or figures.

## Project Conventions
- All code and documentation should relate to the finite volume method for hyperbolic PDEs.
- LaTeX is the primary documentation format; keep code and report in sync.
- Spanish is used for the report; code and comments may be in English or Spanish.
- Place new Python scripts in `src/`.
- Use clear, self-contained scripts for numerical experiments.

## Integration Points
- Python code may generate figures or data for inclusion in the LaTeX report.
- No external dependencies are currently required, but if used, document them clearly in the script headers.

## Examples
- To add a new experiment, create `src/experiment_X.py` and reference its results in `main.tex`.
- To update the report, edit `main.tex` and recompile.

## Recommendations for AI Agents
- Maintain alignment between code outputs and report content.
- Prefer clarity and reproducibility in scripts.
- Document any new workflow or dependency in this file or in script headers.
