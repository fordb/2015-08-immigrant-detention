# Data and Analysis: Immigration Detention by Nationality

Forked from https://github.com/BuzzFeedNews/2015-08-immigrant-detention

This repository contains the data and code supporting several passages in the BuzzFeed News article, "[Vast Disparities By Nationality In Immigration Jailings](http://www.buzzfeed.com/davidnoriega/vast-disparities-by-nationality-in-immigration-jailings)," published August 25, 2015.

## Setup
- Run `pip install -r requirements.txt` to install the necessary packages (recommended to use a virtual environment)
- Because the raw data occupies 5.3 gigabytes of storage, this repository contains a compressed version of it. To decompress the data, run `make data` from this repository's root directory.

## How to Run
- After setup above, run each cell of the python notebook (it will take some time given the large dataset). This saves a file called `custody_by_nationality_year.csv` in the `notebooks/` directory
- Run `python analysis_by_year.py`. This reads the CSV saved above into a Pandas dataframe and does further analysis on the data. This saves another CSV, `region_year_breakdown.csv`, that has the final analysis results that was used back in 2015. Note: I checked columns from the previous results and the results from this repo and they are the same.

## Methodology Changes from original forked repo
- No longer remove criminal cases (removed the filter `(cases_with_first_proceeding["CASE_TYPE"] == "RMV")` when creating the `selected_cases` dataframe)
- No longer remove unaccompanied children (removed the filter `(cases_with_first_proceeding["CASEPRIORITY_CODE"] != "UC")` when creating the `selected_cases` dataframe)
- Include all countries (not just those with fewer than 20K cases between 2003 and 2014 like in original analysis)
- They only look at cases with criminal charges. I keep those in there (removed the line `non_crim_selected_cases = selected_cases[~selected_cases["has_criminal_charge"]].copy()`)
- Removed the code for the logistic regression, not used here
- Renamed columns in the output file to be more clear
- Grouped by year
- Further analysis done in `analysis_by_year.py`

## Final Output Data Description (`region_year_breakdown.csv`)
- `year`: the year that the hearing date happened
- `region`: the region of the world, mapped from the country
- `total`: total number of cases for that region/year
- `detained`: total number of detained cases for that region/year
- `nc`: total cases that are Not detained, criminal charge for that region/year
- `dc`: total cases that are Detained, criminal charge for that region/year
- `rc`: total cases that are Detained then released, criminal charge for that region/year
- `nn`: total cases that are Not detained, no criminal charge for that region/year
- `dn`: total cases that are Detained, no criminal charge for that region/year
- `rn`: total cases that are Detained then released, no criminal charge for that region/year
- `total_year`: total cases that year across all regions that year
- `detained_year`: total number of detained cases across all regions that year
- `pct_criminal_detained`: % of criminal cases that are detained
- `pct_noncriminal_detained`: % of non-criminal cases that are detained
- `pct_detained`: % of cases that were detained for that region/year
- `pct_all_proceedings`: % of all cases for that year that were attributed to that region
- `pct_all_detained`: % of all detained cases for that year that were attributed to that region


## Data

The analyses below use data from the Department of Justice's "CASE" database, maintained by the Executive Office of Immigration Review (EOIR). The database,  which tracks immigration proceedings, was obtained by BuzzFeed News through a Freedom of Information Request. The data cover all cases whose records were created or updated between Jan. 1, 2000 and Jan. 15, 2015.

## Original Analysis

__For a code-free overview, [read this general methodology](methodology.md).__