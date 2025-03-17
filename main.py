from tkinter import *


# --------------------- UI SETUP -------------------------------------------- #
window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")
window.title("Checklist Empilhadores")

canvas = Canvas(width=100, height=120)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(50, 60, image=logo_img)
canvas.grid(column=0, row=0)

lista_label = Label(text="Checklist Empilhadores")
lista_label.grid(column=1, row=0)

mes_label = Label(text="Mês")
mes_label.grid(column=4, row=0)

mes_entry = Entry()
mes_entry.grid(column=5, row=0)

empilhador_label = Label(text="Empilhador")
empilhador_label.grid(column=2, row=0)
listbox = Listbox(height=2,
                  width=10)
listbox.insert(1, "Frontal")
listbox.insert(2, "Lateral")
listbox.grid(column=3, row=0)

equipamento_label = Label(text="Equipamento:")
equipamento_label.grid(column=0, row=2)

marca_label = Label(text="Marca")
marca_label.grid(column=0, row=3)

marca_entry = Entry()
marca_entry.grid(column=1, row=3)

modelo_label = Label(text="Modelo")
modelo_label.grid(column=2, row=3)

modelo_entry = Entry()
modelo_entry.grid(column=3, row=3)

nr_identificacao_label = Label(text="Numero de Identificação")
nr_identificacao_label.grid(column=0, row=4)

nr_identificacao_entry = Entry()
nr_identificacao_entry.grid(column=1, row=4)

nr_serie_label = Label(text="Numero de Serie")
nr_serie_label.grid(column=2, row=4)

nr_serie_entry = Entry()
nr_serie_entry.grid(column=3, row=4)

carga_label = Label(text="Capacidade de Carga")
carga_label.grid(column=0, row=5)

carga_entry = Entry()
carga_entry.grid(column=1, row=5, sticky=W)

verficar_label = (Label(text="Verificar/Data", justify="left", anchor="w").grid(column=0, row=6, sticky=W))
data_smn_1 = (Entry().grid(column=1, row=6))
data_smn_2 = (Entry().grid(column=2, row=6))
data_smn_3 = (Entry().grid(column=3, row=6))
data_smn_4 = (Entry().grid(column=4, row=6))
data_smn_5 = (Entry().grid(column=5, row=6))

breakpoint_label = (Label(text="------------------------------------------------------------------------------")
                    .grid(column=1, row=7, columnspan=5))

ponto_1_label = (Label(text="1. ASPETO GERAL", justify="left", anchor="w").grid(column=0, row=8, sticky=W))
ponto_1_entry_smn_1 = (Entry().grid(column=1, row=8))
ponto_1_entry_smn_2 = (Entry().grid(column=2, row=8))
ponto_1_entry_smn_3 = (Entry().grid(column=3, row=8))
ponto_1_entry_smn_4 = (Entry().grid(column=4, row=8))
ponto_1_entry_smn_5 = (Entry().grid(column=5, row=8))

ponto_2_label = (Label(text="2. PROTEÇÃO DE CABINE", justify="left", anchor="w").grid(column=0, row=9, sticky=W))
ponto_2_entry_smn_1 = (Entry().grid(column=1, row=9))
ponto_2_entry_smn_2 = (Entry().grid(column=2, row=9))
ponto_2_entry_smn_3 = (Entry().grid(column=3, row=9))
ponto_2_entry_smn_4 = (Entry().grid(column=4, row=9))
ponto_2_entry_smn_5 = (Entry().grid(column=5, row=9))

ponto_3_label = (Label(text="3. ASSENTO", justify="left", anchor="w").grid(column=0, row=10, sticky=W))
ponto_3_entry_smn_1 = (Entry().grid(column=1, row=10))
ponto_3_entry_smn_2 = (Entry().grid(column=2, row=10))
ponto_3_entry_smn_3 = (Entry().grid(column=3, row=10))
ponto_3_entry_smn_4 = (Entry().grid(column=4, row=10))
ponto_3_entry_smn_5 = (Entry().grid(column=5, row=10))
ponto_4_label = (Label(text="4. CINTO DE SEGURANÇA", justify="left", anchor="w").grid(column=0, row=11, sticky=W))
ponto_4_entry = (Entry().grid(column=1, row=11))

ponto_5_label = (Label(text="5. VOLANTE E PUNHO", justify="left", anchor="w").grid(column=0, row=12, sticky=W))
ponto_5_entry = (Entry().grid(column=1, row=12))

ponto_6_label = (Label(text="6. MASTRO", justify="left", anchor="w").grid(column=0, row=13, sticky=W))
ponto_6_entry = (Entry().grid(column=1, row=13))

ponto_7_label = (Label(text="7. RODAS", justify="left", anchor="w").grid(column=0, row=14, sticky=W))
ponto_7_entry = (Entry().grid(column=1, row=14))

ponto_8_label = (Label(text="CILINDROS", justify="left", anchor="w").grid(column=0, row=15, sticky=W))
ponto_8_entry = (Entry().grid(column=1, row=15))

ponto_9_label = (Label(text="10. TUBAGENS HIDRAULICAS", justify="left", anchor="w").grid(column=0, row=16, sticky=W))
ponto_9_entry = (Entry().grid(column=1, row=16))

ponto_10_label = (Label(text="11. NIVEIS DE FLUIDOS", justify="left", anchor="w").grid(column=0, row=17, sticky=W))
ponto_10_entry = (Entry().grid(column=1, row=17))

ponto_11_label = (Label(text="12. LUZES FAROIS", justify="left", anchor="w").grid(column=0, row=18, sticky=W))
ponto_11_entry = (Entry().grid(column=1, row=18))

ponto_12_label = (Label(text="13. LUZES STOP", justify="left", anchor="w").grid(column=0, row=19, sticky=W))
ponto_12_entry = (Entry().grid(column=1, row=19))

ponto_13_label = (Label(text="14. LUZES PISCAS", justify="left", anchor="w").grid(column=0, row=20, sticky=W))
ponto_13_entry = (Entry().grid(column=1, row=20))

ponto_14_label = (Label(text="15. LUZES MARCHA ATRAS", justify="left", anchor="w").grid(column=0, row=21, sticky=W))
ponto_14_entry = (Entry().grid(column=1, row=21))

ponto_15_label = (Label(text="16. LUZES PIRILAMPO", justify="left", anchor="w").grid(column=0, row=22, sticky=W))
ponto_15_entry = (Entry().grid(column=1, row=22))

ponto_16_label = (Label(text="17. BOTÃO DE EMERGENCIA", justify="left", anchor="w").grid(column=0, row=23, sticky=W))
ponto_16_entry = (Entry().grid(column=1, row=23))

ponto_17_label = (Label(text="18. DIRECÇÃO", justify="left", anchor="w").grid(column=0, row=24, sticky=W))
ponto_17_entry = (Entry().grid(column=1, row=24))

ponto_18_label = (Label(text="19. BUZINA", justify="left", anchor="w").grid(column=0, row=25, sticky=W))
ponto_18_entry = (Entry().grid(column=1, row=25))

ponto_19_label = (Label(text="20. TRAVÃO ESTACIONAMENTO").grid(column=0, row=26, sticky=W))
ponto_19_entry = (Entry().grid(column=1, row=26))

ponto_20_label = (Label(text="21. TRAVÃO SERVIÇO", justify="left", anchor="w").grid(column=0, row=27, sticky=W))
ponto_20_entry = (Entry().grid(column=1, row=27))

ponto_21_label = (Label(text="22. AVISADOR SONORO", justify="left", anchor="w").grid(column=0, row=28, sticky=W))
ponto_21_entry = (Entry().grid(column=1, row=28))

ponto_22_label = (Label(text="23.ELEVAÇÃO/INCLINAÇÃO GARFOS", justify="left", anchor="w").grid(column=0, row=29,
                                                                                               sticky=W))
ponto_22_entry = (Entry().grid(column=1, row=29))
horas_label = (Label(text="Horas", justify="left", anchor="w").grid(column=0, row=30))
horas_entry = (Entry().grid(column=1, row=30))

window.mainloop()
