#!/bin/bash

yay --noconfirm --needed -Syu python-clawpack
# paru --noconfirm --needed -Syu python-clawpack
sudo pacman --noconfirm --needed -Syu gcc-fortran git python-matplotlib
export CLAW=$HOME/Documents/clawpack
git clone --filter=blob:none \
    --recurse-submodules \
    --depth=1 \
    --branch v5.13.1 \
    git@github.com:clawpack/clawpack.git $CLAW

# Ejemplos de Clawpack Classic en Fortran
cd $CLAW/classic/examples/advection_1d_example1
make .plots
cd $CLAW/classic/examples/advection_2d_annulus
make .plots
cd $CLAW/classic/examples/euler_1d_wcblast
make .plots
cd $CLAW/classic/examples/acoustics_1d_example1
make .plots
cd $CLAW/classic/examples/acoustics_1d_heterogeneous
make .plots
cd $CLAW/classic/examples/acoustics_2d_radial
make .plots
cd $CLAW/classic/examples/acoustics_3d_heterogeneous
make .plots

# Ejemplos de ARMClaw Classic en Fortran
cd $CLAW/amrclaw/examples/advection_1d_example1
make .plots
cd $CLAW/amrclaw/examples/advection_2d_annulus
make .plots
cd $CLAW/amrclaw/examples/advection_2d_flagregions
make .plots
cd $CLAW/amrclaw/examples/advection_2d_inflow
make .plots
cd $CLAW/amrclaw/examples/advection_2d_square
make .plots
cd $CLAW/amrclaw/examples/advection_2d_swirl
make .plots
cd $CLAW/amrclaw/examples/burgers_2d_square
make .plots
cd $CLAW/amrclaw/examples/burgers_3d_cubedata
make .plots
cd $CLAW/amrclaw/examples/euler_1d_wcblast
make .plots
cd $CLAW/amrclaw/examples/euler_2d_quadrants
make .plots
cd $CLAW/amrclaw/examples/euler_3d_radial
make .plots
