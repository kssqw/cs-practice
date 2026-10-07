import sys
from stats import parse_record, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    valid_records = []
    error_count = 0
    for line in lines:
        if line == "":
            continue
            
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            error_count = error_count + 1
    print(len(valid_records))
    print(error_count)

    if len(valid_records) > 0:
        best = warmest_city(valid_records)
        averages = average_by_city(valid_records)
        print("%.1f" % averages[best])
    else:
        print("0.0")

if __name__ == "__main__":
    main()