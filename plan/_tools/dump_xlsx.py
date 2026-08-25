import sys, openpyxl

def dump(path, out):
    wb = openpyxl.load_workbook(path, data_only=True)
    with open(out, 'w', encoding='utf-8') as f:
        for ws in wb.worksheets:
            f.write(f"=== SHEET: {ws.title} ({ws.dimensions}) ===\n")
            for row in ws.iter_rows():
                vals = [str(c.value) if c.value is not None else '' for c in row]
                if any(v.strip() for v in vals):
                    f.write(" | ".join(vals) + "\n")

if __name__ == '__main__':
    dump(sys.argv[1], sys.argv[2])
    print("done")
