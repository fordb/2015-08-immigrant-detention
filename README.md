# Data and Analysis: Immigration Detention by Nationality

Forked from https://github.com/BuzzFeedNews/2015-08-immigrant-detention

This repository contains the data and code supporting several passages in the BuzzFeed News article, "[Vast Disparities By Nationality In Immigration Jailings](http://www.buzzfeed.com/davidnoriega/vast-disparities-by-nationality-in-immigration-jailings)," published August 25, 2015.

## Setup
- Run `pip install -r requirements.txt` to install the necessary packages (recommended to use a virtual environment)
- Because the raw data occupies 5.3 gigabytes of storage, this repository contains a compressed version of it. To decompress the data, run `make data` from this repository's root directory.

## How to Run
- After setup above, run each cell of the python notebook (it will take some time given the large dataset)
- 

## Methodology Changes from original forked repo
- No longer remove criminal cases (removed the filter `(cases_with_first_proceeding["CASE_TYPE"] == "RMV")` when creating the `selected_cases` dataframe)
- No longer remove unaccompanied children (removed the filter `(cases_with_first_proceeding["CASEPRIORITY_CODE"] != "UC")` when creating the `selected_cases` dataframe)
- Include all countries (not just those with fewer than 20K cases between 2003 and 2014 like in original analysis)
- They only look at cases with criminal charges. I keep those in there (removed the line `non_crim_selected_cases = selected_cases[~selected_cases["has_criminal_charge"]].copy()`)

## Data

The analyses below use data from the Department of Justice's "CASE" database, maintained by the Executive Office of Immigration Review (EOIR). The database,  which tracks immigration proceedings, was obtained by BuzzFeed News through a Freedom of Information Request. The data cover all cases whose records were created or updated between Jan. 1, 2000 and Jan. 15, 2015.

## Original Analysis

__For a code-free overview, [read this general methodology](methodology.md).__