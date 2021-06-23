def clean_json(d):
    """recursively remove empty lists, empty dicts, or None elements from a dictionary
    and also perform strip operation for the string values"""

    def empty(x):
        return x is None or x == {} or x == [] or x == ""

    if not isinstance(d, (dict, list)):
        if isinstance(d, str):
            return d.strip()
        return d
    elif isinstance(d, list):
        return [v for v in (clean_json(v) for v in d) if not empty(v)]
    else:
        return {k: v for k, v in ((k, clean_json(v)) for k, v in d.items()) if not empty(v)}
     
    

#Using the clean_json method in lambda
#Using Pandas DataFrame
df['data_json'] = df.apply(lambda x: json.dumps(clean_json(json.loads(x['data_json'])))
