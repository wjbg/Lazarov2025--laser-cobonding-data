           __________________________________________________

                DATA PACKAGE FOR 'LASER-INDUCED SURFACE
               MODIFICATION OF C/PEKK FOR CO-BONDING WITH
                                C/EPOXY'
           __________________________________________________


                               2026-01-01


General information
===================

  Insert generic information, e.g. a reference to the publication that
  the data belong to.

  This dataset contains:
  - Add contents


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
  BY license. See `LICENSE.txt` file in this repository.


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
  |                C/PEKK for co-bonding with C/epoxy"},
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
  - `raw`: All raw measurement data as well as the original microscopy
    images.
  - `clean`: The cleaned data used to generate the graphs in the
    original publication. The data is stored in `CSV` files with clear
    column names.
  - `python`: The code used to generate the graphs.
  - `images`: The images as used in the original publication.


Differential scanning calorimetry (DSC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  The DSC data can be found in the folder `DSC` and is organized in
  three subfolders:
  - `conventional`: standard DSC data to determine the critical cooling
    rate
  - `flash-dsc`: Flash DSC data to determine the critical cooling rate
  - `laser-sample`: dsc trace of surface sample from laser-treated
    laminate

  The `raw` data is provided in the proprietary machine format, while
  the cleaned data is provided as CSV files with clear column names. The
  filenames in the `clean/dsc/conventional` folder are structured as
  follows:

  `SXX-YYK-per-min.csv`,

  with `XX` the sample number and `YY` the cooling rate in K/min. The
  `clean/dsc/flash-dsc` filenames are structured as:

  `XXXK-per-s.csv`,

  with `XXX` the cooling rate in K/s.


Laser heating
~~~~~~~~~~~~~

  The maximum surface temperature during laser heating, as measured by
  the thermal camera, is provided in `clean/static-laser-heating`. The
  data is stored directly as `csv` data and is therefore not available
  in the `raw` folder. The filenames are structured as:

  `XXXW-YYYYms.csv`,

  where `XXX` indicates the laser power and `YYYY` the pulse duration.


SEM-EDX
~~~~~~~

  The SEM-EDX data can be found in the folder `edx`. The `raw` data is
  provided in a Microsoft Word file with an graph indicating the element
  count along a predifined path that is indicated in the associated
  `tiff` image. The `clean` data provides the Bromium count along the
  path, with the same `tiff` image stored there for reference too.


Mandrel peel data
~~~~~~~~~~~~~~~~~

  The mandrel peel test results are provided in the foler `peel`. The
  data is clearly labelled (`reference`, `treated`, `treated+annealed`)
  with the last integer (1-5) indicating the sample number.


Code
====

  Mention which software (including version) was used to analyze the
  data and that the scripts can be found in the folder `python`.
