# Data and Analysis: Immigration Detention by Nationality

Forked from https://github.com/BuzzFeedNews/2015-08-immigrant-detention

This repository contains the data and code supporting several passages in the BuzzFeed News article, "[Vast Disparities By Nationality In Immigration Jailings](http://www.buzzfeed.com/davidnoriega/vast-disparities-by-nationality-in-immigration-jailings)," published August 25, 2015.

## Setup
- Run `pip install -r requirements.txt` to install the necessary packages (recommended to use a virtual environment)
- Because the raw data occupies 5.3 gigabytes of storage, this repository contains a compressed version of it. To decompress the data, run `make data` from this repository's root directory.

## Data

The analyses below use data from the Department of Justice's "CASE" database, maintained by the Executive Office of Immigration Review (EOIR). The database,  which tracks immigration proceedings, was obtained by BuzzFeed News through a Freedom of Information Request. The data cover all cases whose records were created or updated between Jan. 1, 2000 and Jan. 15, 2015.

## Original Analysis

__For a code-free overview, [read this general methodology](methodology.md).__