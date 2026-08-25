import sys, docx

def iter_block_items(parent):
    from docx.document import Document as _Doc
    from docx.oxml.ns import qn
    from docx.table import Table, _Cell
    from docx.text.paragraph import Paragraph
    if isinstance(parent, _Doc):
        parent_elm = parent.element.body
    else:
        parent_elm = parent._tc
    for child in parent_elm.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

def dump(path, out):
    d = docx.Document(path)
    with open(out, 'w', encoding='utf-8') as f:
        for block in iter_block_items(d):
            if block.__class__.__name__ == 'Paragraph':
                style = block.style.name if block.style else ''
                text = block.text
                if text.strip():
                    f.write(f"[{style}] {text}\n")
            else:
                f.write("[TABLE]\n")
                for row in block.rows:
                    cells = [c.text.strip().replace('\n',' | ') for c in row.cells]
                    f.write(" || ".join(cells) + "\n")
                f.write("[/TABLE]\n")

if __name__ == '__main__':
    dump(sys.argv[1], sys.argv[2])
    print("done")
