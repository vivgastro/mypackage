# ADACS best coding practice workshop

Author: Vivek Gupta
Date: 2023-03-20

This is a example repository that allows for some analysis of sky catalogs

## Goal of the package is as follows:

With the following requirements, we quickly pulled together some code that works.

- Stars should have randomized sky positions around the Andromeda galaxy
- Positions should fall within 1 degree of the central location
- Each star should have a unique ID
- The star ID and position should be saved in a csv file to be analyzed by other programs

Here is the directory structure

.
├── README.md          <- Description of this project
├── bin                <- Your compiled code can be stored here (not tracked by git)
├── config             <- Configuration files, e.g., for sphinx or for your model if needed
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final data sets for analysis.
│   └── raw            <- The original, immutable data dump.
├── docs               <- Documentation, e.g., sphinx or reference papers (not tracked by git)
├── env                <- Python environment specific to this project
├── notebooks          <- Jupyter or R notebooks
├── reports            <- For a manuscript source, e.g., LaTeX, Markdown, etc., or any project reports
│   └── figures        <- Figures for the manuscript or reports
└── src                <- Source code for this project
    ├── external       <- Any external source code, e.g., pull other git projects libraries
    └── tools          <- Any helper scripts go here
