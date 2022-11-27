import pandas as pd
import pycountry

# Creates a pandas series of the 3-character country codes of the given countries
def get3countryCode(names):
    # Store the country codes that are found in a dictionary to speed up the function
    code_map = dict()
    
    res = []
    for name in names:
        try:
            try:
                code = code_map[name]
            except KeyError:
                code = pycountry.countries.search_fuzzy(name)[0].alpha_3
                code_map[name] = code
                
            res.append(code)
        except LookupError:
            res.append(None)
    
    return pd.Series(res)
