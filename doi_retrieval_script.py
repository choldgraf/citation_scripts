#!/usr/bin/env python

import json
from search_and_DOI_utilities import search_plos, plos_dois

SEARCH_JOURNAL = "PLOS ONE"
MAX_PAPERS = 200000
extra_parameters = {'journal': 'PLOS ONE'}

search_results = search_plos('*', extra_parameters=extra_parameters, rows=MAX_PAPERS)
print "Retrieving " + str(len(search_results)) + " DOIs from PLOS ONE..."
dois = plos_dois(search_results)
# jdois = json.dumps(dois)
doifile = open("20k_pone_dois.json", "w")
json.dump(dois, doifile)
doifile.close()
