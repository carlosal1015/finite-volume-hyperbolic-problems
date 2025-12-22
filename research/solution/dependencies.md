Name            : python-numpy-mkl
Version         : 2.3.4-1
Description     : Scientific tools for Python, compiled with Intel MKL
Architecture    : x86_64
URL             : https://numpy.org
Licenses        : BSD-3-Clause
Groups          : None
Provides        : python-numpy=2.3.4
Depends On      : python  intel-oneapi-mkl
Optional Deps   : python-threadpoolctl: for show_runtime() support [installed]
Required By     : carma  inkscape  paraview  petsc  python-adjusttext  python-bmipy  python-cftime  python-contourpy  python-fipy  python-h5py-openmpi  python-ipympl  python-jax
                  python-jaxlib  python-matplotlib  python-meshio  python-ml-dtypes  python-mpi4jax  python-netcdf4  python-numba  python-numexpr  python-numpy-stl
                  python-opt_einsum  python-pandas  python-patsy  python-pyevtk  python-pytables  python-pyweno-git  python-scikit-learn  python-scipy-mkl  python-statsmodels
                  python-uvw  python-xarray  usd
Optional For    : adios2  openvdb  pastix  pdal  python-array-api-compat  python-hypothesis  python-joblib  python-rapidfuzz  python-tabulate  sundials  superlu_dist
Conflicts With  : python-numpy
Replaces        : None
Installed Size  : 46.99 MiB
Packager        : Unknown Packager
Build Date      : Thu 16 Oct 2025 08:20:38 AM -05
Install Date    : Thu 16 Oct 2025 08:32:21 PM -05
Install Reason  : Explicitly installed
Install Script  : No
Validated By    : SHA-256 Sum  Signature

Name            : python-scipy-mkl
Version         : 1.16.3-1
Description     : SciPy is open-source software for mathematics, science, and engineering.
Architecture    : x86_64
URL             : http://www.scipy.org/
Licenses        : BSD
Groups          : None
Provides        : python-scipy
Depends On      : intel-oneapi-mkl  python-numpy  python-pooch
Optional Deps   : python-pillow: for image saving module [installed]
Required By     : python-adjusttext  python-fipy  python-jax  python-jaxlib  python-landlab  python-numerate-git  python-py-pde  python-pyamg  python-pymole-git
                  python-scikit-learn  python-scikit-umfpack  python-statsmodels
Optional For    : fast_matrix_market  pastix  python-clawpack  python-fonttools  python-numba  python-pandas  python-patsy  python-seaborn  python-xarray  superlu_dist
Conflicts With  : python-scipy
Replaces        : None
Installed Size  : 110.59 MiB
Packager        : Unknown Packager
Build Date      : Sun 02 Nov 2025 02:04:56 PM -05
Install Date    : Mon 03 Nov 2025 12:11:04 PM -05
Install Reason  : Explicitly installed
Install Script  : No
Validated By    : SHA-256 Sum  Signature

Name            : python-matplotlib
Version         : 3.10.8-1
Description     : A python plotting library, making publication quality plots
Architecture    : x86_64
URL             : https://matplotlib.org
Licenses        : PSF-2.0
Groups          : None
Provides        : None
Depends On      : gcc-libs  glibc  freetype2  python  python-contourpy  python-cycler  python-dateutil  python-fonttools  python-kiwisolver  python-numpy  python-packaging
                  python-pillow  python-pyparsing  qhull
Optional Deps   : tk: Tk{Agg,Cairo} backends [installed]
                  pyside6: alternative for Qt6{Agg,Cairo} backends [installed]
                  python-pyqt5: Qt5{Agg,Cairo} backends [installed]
                  python-pyqt6: Qt6{Agg,Cairo} backends [installed]
                  python-gobject: for GTK{3,4}{Agg,Cairo} backend [installed]
                  python-wxpython: WX{Agg,Cairo} backend [installed]
                  python-cairo: {GTK{3,4},Qt{5,6},Tk,WX}Cairo backends [installed]
                  python-cairocffi: alternative for Cairo backends
                  python-tornado: WebAgg backend [installed]
                  ffmpeg: for saving movies [installed]
                  imagemagick: for saving animated gifs [installed]
                  ghostscript: usetex dependencies [installed]
                  texlive-binextra: usetex dependencies [installed]
                  texlive-fontsrecommended: usetex dependencies [installed]
                  texlive-latexrecommended: usetex usage with pdflatex [installed]
                  python-certifi: https support [installed]
Required By     : python-adjusttext  python-clawpack  python-cmocean  python-fipy  python-ipympl  python-landlab  python-matspy  python-numerate-git  python-py-pde  python-pyfonts
                  python-pyro-hydro  python-seaborn
Optional For    : jupyter-metakernel  paraview  python-contourpy  python-fonttools  python-matplotlib-inline  python-pandas  python-scikit-learn  python-statsmodels  python-xarray
                  sundials  vtk
Conflicts With  : None
Replaces        : None
Installed Size  : 28.71 MiB
Packager        : Jakub Klinkovský <lahwaacz@archlinux.org>
Build Date      : Thu 13 Nov 2025 12:59:26 PM -05
Install Date    : Thu 13 Nov 2025 10:57:39 PM -05
Install Reason  : Installed as a dependency for another package
Install Script  : No
Validated By    : Signature

Version         : 0.9.0-5
Description     : Pretty-print tabular data in Python, a library and a command-line utility.
Architecture    : any
URL             : https://github.com/astanin/python-tabulate
Licenses        : MIT
Groups          : None
Provides        : None
Depends On      : python
Optional Deps   : python-numpy: NumPy array support [installed]
                  python-pandas: pandas.DataFrame support [installed]
                  python-wcwidth: wide-character support [installed]
Required By     : None
Optional For    : python-pandas
Conflicts With  : None
Replaces        : None
Installed Size  : 341.19 KiB
Packager        : Jelle van der Waa <jelle@archlinux.org>
Build Date      : Tue 26 Nov 2024 06:16:03 AM -05
Install Date    : Fri 12 Sep 2025 11:14:09 AM -05
Install Reason  : Explicitly installed
Install Script  : No
Validated By    : Signature

Name            : python-pandas
Version         : 2.3.1-1
Description     : High-performance, easy-to-use data structures and data analysis tools for Python
Architecture    : x86_64
URL             : https://pandas.pydata.org/
Licenses        : BSD-3-Clause
Groups          : None
Provides        : None
Depends On      : python-numpy  python-dateutil  python-pytz
Optional Deps   : python-pandas-datareader: pandas.io.data replacement (recommended)
                  python-numexpr: accelerating certain numerical operations (recommended) [installed]
                  python-bottleneck: accelerating certain types of nan evaluations (recommended)
                  python-matplotlib: plotting [installed]
                  python-jinja: conditional formatting with DataFrame.style [installed]
                  python-tabulate: printing in Markdown-friendly format [installed]
                  python-scipy: miscellaneous statistical functions [installed]
                  python-numba: alternative execution engine [installed]
                  python-xarray: pandas-like API for N-dimensional data [installed]
                  python-xlrd: Excel XLS input
                  python-xlwt: Excel XLS output
                  python-openpyxl: Excel XLSX input/output [installed]
                  python-xlsxwriter: alternative Excel XLSX output
                  python-beautifulsoup4: read_html function (in any case) [installed]
                  python-html5lib: read_html function (and/or python-lxml) [installed]
                  python-lxml: read_xml, to_xml and read_html function (and/or python-html5lib) [installed]
                  python-sqlalchemy: SQL database support
                  python-psycopg2: PostgreSQL engine for sqlalchemy
                  python-pymysql: MySQL engine for sqlalchemy
                  python-pytables: HDF5-based reading / writing [installed]
                  python-blosc: for msgpack compression using blosc
                  zlib: compression for msgpack [installed]
                  python-pyarrow: Parquet, ORC and feather reading/writing
                  python-fsspec: handling files aside from local and HTTP
                  python-pyqt5: read_clipboard function (only one needed) [installed]
                  python-qtpy: read_clipboard function (only one needed) [installed]
                  xclip: read_clipboard function (only one needed)
                  xsel: read_clipboard function (only one needed)
                  python-brotli: Brotli compression [installed]
                  python-snappy: Snappy compression
                  python-zstandard: Zstandard (zstd) compression [installed]
Required By     : python-jupyprint  python-landlab  python-outset  python-seaborn  python-statsmodels  python-xarray
Optional For    : paraview  python-hypothesis  python-openpyxl  python-py-pde  python-tabulate
Conflicts With  : None
Replaces        : None
Installed Size  : 108.19 MiB
Packager        : Christian Heusel <gromit@archlinux.org>
Build Date      : Tue 08 Jul 2025 05:58:48 PM -05
Install Date    : Thu 10 Jul 2025 08:20:56 AM -05
Install Reason  : Installed as a dependency for another package
Install Script  : No
Validated By    : Signature
