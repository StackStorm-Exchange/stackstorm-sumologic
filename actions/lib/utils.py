def find_by_field(cs, field, keyword, exact_match):
    res = []
    for c in cs:
        if exact_match:
            if field == 'id':
                keyword = int(keyword)
            if field in c and keyword == c[field]:
                res.append(c)
        else:
            if field in c and keyword in c[field]:
                res.append(c)
    return res
