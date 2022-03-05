import pandas as pd
import sys

d = pd.read_csv('notebooks/custody_by_nationality_year.csv')
countries = pd.read_csv('country_lookup.csv')

# merge with country lookup file to get regions
d = pd.merge(d, countries, how='left', left_on='NAT_NAME', right_on='country')

# subsets data by specified year/region
def breakdown(year, region):
    temp = d[d['region'] == region]
    if year != 'ALL':
        temp = temp[temp['year'] == year]
    if temp.shape[0] == 0:
        print('empty dataframe. check the year and region')
        sys.exit()

    nc = temp['N_criminal'].sum()
    dc = temp['D_criminal'].sum()
    rc = temp['R_criminal'].sum()
    nn = temp['N_noncriminal'].sum()
    dn = temp['D_noncriminal'].sum()
    rn =   temp['R_noncriminal'].sum()

    total = nc + dc + rc + nn + dn + rn
    detained = dc + rc + dn + rn

    return [year, region, total, detained, nc, dc, rc, nn, dn, rn]


regions = ['AFRICA', 'CARIBBEAN', 'CENTRAL AMERICA', 'SOUTH AMERICA',
           'NORTH AMERICA', 'ASIA', 'EUROPE', 'OCEANIA', 'OTHERS']
years = list(range(2003, 2015))
years.append('ALL')

final = []

for y in years:
    for r in regions:
        l = breakdown(y, r)
        final.append(l)

cols = ['year', 'region', 'total', 'detained', 'nc', 'dc', 'rc', 'nn', 'dn', 'rn']
final = pd.DataFrame(final, columns=cols)

year_totals = []
for y in years:
    temp = final[final['year'] == y]
    total = temp['total'].sum()
    detained = temp['detained'].sum()
    year_totals.append([y, total, detained])

year_cols = ['year', 'total_year', 'detained_year']
year_totals = pd.DataFrame(year_totals, columns=year_cols)

final = pd.merge(final, year_totals, how='left', on='year')

final['pct_criminal_detained'] = (final['dc'] + final['rc']) / (final['dc'] + final['rc'] + final['nc'])
final['pct_noncriminal_detained'] = (final['dn'] + final['rn']) / (final['dn'] + final['rn'] + final['nn'])
final['pct_detained'] = final['detained'] / final['total']
final['pct_all_proceedings'] = final['total'] / final['total_year']
final['pct_all_detained'] = final['detained'] / final['detained_year']

final.to_csv('region_year_breakdown.csv', index=False)