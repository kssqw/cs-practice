import logstats

def main():
    name = input().strip()

    with open(name, "r", encoding="utf-8") as f1:
        c = logstats.count_levels(f1)
        
    with open(name, "r", encoding="utf-8") as f2:
        e = logstats.top_errors(f2, 3)
        
    vsego = 0
    for k in c:
        vsego = vsego + c[k]
        
    print(vsego)
    print(c["ERROR"])
    print(c["BROKEN"])
    rep = logstats.format_report(c, e)
    with open("report.txt", "w", encoding="utf-8") as out:
        out.write(rep)

if __name__ == "__main__":
    main()
    