#!/usr/bin/env python
"""
Utility functions for loading and displaying parameters in formatted tables.
"""

from typing import Dict, List

from tabulate import tabulate


def load_parameters(
    file_name: str, section_name: str = "parameters"
) -> Dict[str, float]:
    """
    Loads parameters from a TOML file and section.
    """
    from os.path import dirname, join
    from tomllib import load

    with open(join(dirname(__file__), file_name), "rb") as f:
        config = load(f)

    return config.get(section_name, {})


def print_table(
    title: str,
    headers: List[str],
    data: List[List[str]],
    floatfmt: str = "g",
):
    """
    Prints a formatted table with a title.
    """
    print(f"{title}:")
    print(
        tabulate(
            data, headers=headers, tablefmt="grid", numalign="right", floatfmt=floatfmt
        )
    )


def display_parameters_table(params: Dict[str, float]):
    """
    Displays physical parameters in a formatted table.
    """
    param_metadata = {
        "Tres": ("Initial reservoir Temperature", "K"),
        "Cm": ("Rock matrix heat capacity", "J/(m³K)"),
        "Qr": ("Enthalpy of the mobile fuel at Tres", "J/mol"),
        "Er": ("Activation Energy", "J/mol"),
        "kp": ("Frequency factor for the reaction", "1/s"),
        "R": ("Gas constant", "J/(mol·K)"),
        "φ": ("Porosity", "-"),
        "ρo": ("Average molar density of oil", "mol/m³"),
        "co": ("Molar heat capacity of oil", "J/(mol·K)"),
        "u": ("Darcy velocity of oil and gas mixture", "m/s"),
        "ug": ("Relative Darcy velocity of gas", "m/s"),
        "uo": ("Relative Darcy velocity of oil", "m/s"),
        "ρg": ("Average molar density of gas", "mol/m³"),
        "ρres": ("Average initial molar density of oil", "mol/m³"),
        "Lres": ("Reservoir length", "m"),
        "SoR": ("Oil saturation on the right", "-"),
        "SyL": ("Gas saturation on the left", "-"),
    }

    table_data = []
    for symbol, value in params.items():
        quantity, unit = param_metadata.get(symbol, ("Unknown", "Unknown"))
        table_data.append([symbol, quantity, f"{value:g}", unit])

    headers = ["Symbol", "Physical Quantity", "Value", "Unit (SI)"]
    print_table("Physical Parameters", headers, table_data)


def display_derived_parameters(model):
    """
    Displays derived dimensionless parameters from the model.
    """
    derived_params = {
        "a1": model.a1,
        "a2": model.a2,
        "a3": model.a3,
        "b1": model.b1,
        "b2": model.b2,
        "b3": model.b3,
        "β": model.β,
        "Tast": model.Tast,
        "c": model.c,
        "c/a1": model.c / model.a1,
    }

    table_data = [[symbol, f"{value:g}"] for symbol, value in derived_params.items()]
    headers = ["Symbol", "Value"]
    print_table("Derived Dimensionless Parameters", headers, table_data)

    f_params = {
        "m": model.m,
        "ε": model.ε,
        "θ0": model.θ0,
        "q": model.q,
    }

    f_table_data = [[symbol, f"{value:g}"] for symbol, value in f_params.items()]
    print_table("Dimensionless Parameters for f(θ)", headers, f_table_data)


def display_key_values(model, fprime_roots, fprimeprime_root, θM, θ3):
    """
    Displays key calculated values in a formatted table.
    """
    key_values = {
        "θ1": fprime_roots[0],
        "θ2": fprime_roots[1],
        "θ*": fprimeprime_root,
        "f(θ1)": model.f(fprime_roots[0]),
        "f(θ2)": model.f(fprime_roots[1]),
        "1/q": 1 / model.q if model.q != 0 else float("inf"),
        "θM": θM,
        "θ3": θ3,
    }

    table_data = [[symbol, value] for symbol, value in key_values.items()]
    headers = ["Symbol", "Value"]
    print_table("Summary of Key Values", headers, table_data, floatfmt=".12f")
