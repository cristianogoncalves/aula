from fpdf import FPDF
import glob
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-n", "--nome", required=True,
	help="Informe o nome da aula")
args = vars(ap.parse_args())


pdf = FPDF("L", 'mm', "A4")
pdf.set_auto_page_break(0)

imagelist = glob.glob(r".\Imagens\Tratados\*{}_tratado.png".format(args["nome"]))


for image in sorted(imagelist):
    pdf.add_page()
    pdf.image(image,  type="PNG")

pdf.output("{}.pdf".format(args["nome"]), "F")