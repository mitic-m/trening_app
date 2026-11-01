from fpdf import FPDF


def napravi_pdf(plan, klijent) -> bytes:
    pdf = FPDF()
    pdf.add_page()

    # Naša slova (č, ć, š, ž, đ) traže pravi font, a ne podrazumevani
    pdf.add_font("Arial", "", r"C:\Windows\Fonts\arial.ttf")
    pdf.add_font("Arial", "B", r"C:\Windows\Fonts\arialbd.ttf")

    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 12, plan.naziv, new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Klijent: {klijent.ime} {klijent.prezime}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    for dan in plan.dani:
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, dan.naziv, new_x="LMARGIN", new_y="NEXT")

        pdf.set_font("Arial", "", 12)
        for stavka in dan.vezbe:
            tekst = f"{stavka.vezba.naziv}: {stavka.serije} x {stavka.ponavljanja}"
            pdf.cell(0, 8, tekst, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(3)

    return bytes(pdf.output())