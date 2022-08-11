f = "table_enum"

names = {"information_schema" : [], "sys":[], "quotedb":[], "performance_schema":[], "mysql":[]}

with open(f, "r") as tables:
    tabs = tables.read().split(",")
    for t in tabs:
        t = t.strip()
        for n in names.keys():
            if t.startswith(n):
                names[n].append(t.strip(n))
                break
    
    for n in names.keys():
        open(f"enum_{n}", "w").write("\n".join(names[n]))
