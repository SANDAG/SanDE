[![Build Status](https://travis-ci.org/SANDAG/SanDE.svg?branch=master)](https://travis-ci.org/SANDAG/SanDE)
[![Coverage Status](https://coveralls.io/repos/github/SANDAG/SanDE/badge.svg?branch=master)](https://coveralls.io/github/SANDAG/SanDE?branch=master)

# SANDAG San Diego Demographic and Economic (SanDE) Model

## Demographic Model
The demographic model is essentially a cohort-component model that takes a base population stratified by demographic characteristics, applies the pre-computed rates, which govern the demographic transitions, and creates a projection of the future population of a region (in our case, San Diego county). 

## Economic Model
The economic model uses population data obtained from the demographic model, and a set of pre-computed rates to derive labor force, employment, jobs, and total wages for the region. Just like with population, jobs and income are projected via a sequence of interrelated steps. 