           __________________________________________________

                DATA PACKAGE FOR 'LASER-INDUCED SURFACE
               MODIFICATION OF C/PEKK FOR CO-CURING WITH
                                C/EPOXY'
           __________________________________________________


                               2026-05-28


General information
===================

  This data package supports the research presented in the publication
  "Laser-induced surface modification of C/PEKK for co-curing with
  C/epoxy". The study investigates a laser-based surface treatment
  designed to locally amorphize the surface of Carbon Fiber reinforced
  Polyetherketoneketone (C/PEKK) composites. This modification aims to
  enhance the co-curing strength with Carbon/epoxy systems by
  suppressing surface crystallinity and promoting better interface
  formation.

  This dataset contains:
  - *Thermal Analysis Data*: DSC and Flash DSC traces used to
     characterize the crystallization kinetics and determine critical
     cooling rates of the C/PEKK composite.
  - *Laser Heating Profiles*: Surface temperature measurements recorded
     via thermal imaging during the static laser heating.
  - *Element Characterization*: SEM-EDX line scans and reference images
     tracking chemical markers (Bromine) to evaluate the depth and
     effect of the laser treatment.
  - *Mechanical Testing*: Load-displacement data from mandrel peel tests
     comparing reference, laser-treated, and treated + annealed coupons
     to quantify bond performance.
  - *Microscopy & Fractography*: High-resolution images (Polarized,
     Ion-beam, and SEM) of the composite microstructure, the bond
     interface, and the resulting fracture surfaces.
  - *Analysis Scripts*: Python scripts and requirements for processing
     the clean data and reproducing the figures in the associated
     publication.


Authors & Affiliations
~~~~~~~~~~~~~~~~~~~~~~

  - Ivaylo Lazarov, University of Twente
  - Liran Katz, ThermoPlastic composites Research Center
  - Joran Geschiere, ThermoPlastic composites Research Center
  - Nick Helthuis, University of Twente
  - Wouter Grouve, University of Twente


Correspondence
~~~~~~~~~~~~~~

  - Wouter Grouve (w.j.b.grouve@utwente.nl)


License
~~~~~~~

  The journal article as well as this dataset are published under a CC
  BY license. See `LICENSE.txt' file in this repository.


Citation
~~~~~~~~

  In case you use this data, please cite the original article:

  ,----
  | @article{Lazarov2026,
  |   author    = {},
  |   title     = {},
  |   journal   = {},
  |   year      = {},
  |   volume    = {},
  |   month     = {},
  |   pages     = {},
  |   issn      = {},
  |   publisher = {}}
  `----

  as well as this dataset:

  ,----
  | @article{Lazarov2026_data,
  |   author    = {Lazarov, I.V. and Katz, L. and Geschiere, I.J. and
  |                Helthuis, N.G.J. and Grouve, W.J.B.},
  |   title     = {Data package for "Laser-induced surface modification of
  |                C/PEKK for co-curing with C/epoxy"},
  |   year      = {2025},
  |   doi       = {ADD DOI},
  |   publisher = {4TU.ResearchData},
  |   copyright = {CC:BY 4.0}}
  `----


Funding and acknowledgments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

  The authors gratefully acknowledge the financial and technical support
  from the industrial and academic members of the ThermoPlastic
  Composites Research Center (TPRC). We are also particularly grateful
  to dr.ir. Laurent Warnet, who suggested using a laser to reduce the
  surface crystallinity--an idea that ultimately proved crucial in this
  work.


Dataset
=======

  The data is organized in the following folders:
  - `raw': All raw measurement data as well as the original microscopy
    images.
  - `clean': The cleaned data used to generate the graphs in the
    original publication. The data is stored in `CSV' files with clear
    column names.
  - `python': The code used to generate the graphs.
  - `images': The images as used in the original publication.


Differential scanning calorimetry (dsc)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  The dsc data can be found in the folder `dsc' and is organized in
  three subfolders:
  - `conventional': standard DSC data to determine the critical cooling
    rate
  - `flash-dsc': Flash DSC data to determine the critical cooling rate
  - `laser-sample': dsc trace of surface sample from laser-treated
    laminate

  The `raw' data is provided in the proprietary machine format, while
  the cleaned data is provided as CSV files with clear column names. The
  filenames in the `clean/dsc/conventional' folder are structured as
  follows:

  `SXX-YYK-per-min.csv',

  with `XX' the sample number and `YY' the cooling rate in K/min. In
  addition, two other files are included, namely
  `isothermal-155C-2hrs.csv' and `isothermal-177C-2hrs.csv' with the
  data of the isothermal crystallization experiments at 155 and 177 °C,
  respectively.

  The `clean/dsc/flash-dsc' filenames are structured as:

  `XXXK-per-s.csv',

  with `XXX' the cooling rate in K/s.


Laser heating
~~~~~~~~~~~~~

  The maximum surface temperature during laser heating, as measured by
  the thermal camera, is provided in `clean/static-laser-heating'. The
  data is stored directly as `csv' data and is therefore not available
  in the `raw' folder. The filenames are structured as:

  `XXXW-YYYYms.csv',

  where `XXX' indicates the laser power and `YYYY' the pulse duration.


SEM-EDX
~~~~~~~

  The SEM-EDX data can be found in the folder `edx'. The `raw' data is
  provided in a Microsoft Word file with a graph indicating the element
  count along a predefined path that is indicated in the associated
  `tiff' image. The `clean' data provides the Bromine count along the
  path, with the same `tiff' image stored there for reference too.


Mandrel peel data
~~~~~~~~~~~~~~~~~

  The mandrel peel test results are provided in the folder `peel'. The
  data is labelled (`reference', `treated', `treated+annealed') with the
  last integer (1-5) indicating the sample number.


Confocal imaging
~~~~~~~~~~~~~~~~

  The confocal height profile data is provided in the folder `confocal'.
  The data is labelled (`reference', `treated', `treated+annealed') with
  the last integer (1-5) indicating the sample number. The files include
  height profiles, including resolution and acquisition information, in
  `csv' format and an overview image in `bmp' format. Moreover, the raw
  data in proprietary `vk3' format is providedin the `raw' data folder.


Code
====

  The data analysis and visualization were performed using Python 3.12.
  The source scripts are located in the `python/' folder. To reproduce
  the figures, it is recommended to use a virtual environment.

  You can install the required dependencies using `pip':

  ,----
  | pip install -r python/requirements.txt
  `----

  Once the dependencies are installed, the scripts should be executed
  from the `python/' directory to ensure the relative data paths are
  correct:

  ,----
  | cd python
  | python3 plot-peel-results.py
  `----
