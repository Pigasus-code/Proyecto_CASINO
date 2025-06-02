import pandas as pd
from fpdf import FPDF
import datetime
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class GestorReporte:
    
    def generar_reporte_personalizado(self,filtros_maquina:list,filtros_casino:list,contadores:list,fecha_inicio,fecha_fin,formato:str,nombre:str)->str:
        contadores_rango_fecha=[c for c in contadores if c.fecha >=fecha_inicio and c.fecha <= fecha_fin]
        df = pd.DataFrame([c.to_dict() for c in contadores_rango_fecha])
        filtros=filtros_maquina+filtros_casino+["fecha","in","out","jackpot","billetero"]
        df = df[filtros]
        if formato == "excel":
            ruta = os.path.join(BASE_DIR,"Data","Reportes",f"{nombre}.xlsx")
            df.to_excel(ruta, index=False)
            return ruta
        elif formato == "pdf":
            with open(os.path.join(BASE_DIR,"Data","datos_empresa.txt"), "r") as f:
                nombre_empresa = f.readline().strip()
                telefono = f.readline().strip()
                nit = f.readline().strip()
                direccion_emp = f.readline().strip()
                
            pdf = FPDF(orientation="P", unit="mm", format="A4")
            pdf.add_page()

            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "REPORTE PERSONALIZADO", ln=True, align="C")

            hoy = datetime.date.today().strftime("%Y-%m-%d")
            pdf.set_font("Arial", "", 12)
            pdf.cell(0, 8, f"Fecha de emisi\u00f3n: {hoy}", ln=True, align="C")
            pdf.ln(5)

            pdf.set_font("Helvetica", "B", 12)
            pdf.cell(0, 6, nombre_empresa, ln=True)
            pdf.set_font("Helvetica", "", 10)
            pdf.cell(0, 5, f"Tel: {telefono}   NIT: {nit}", ln=True)
            pdf.cell(0, 5, f"Direcci\u00f3n: {direccion_emp}", ln=True)
            pdf.ln(8)

            agrupador_casino = filtros_casino[0] if len(filtros_casino) > 0 else None

            if agrupador_casino:
                for codigo, subdf_casino in df.groupby(agrupador_casino):
                    nombre_casino = subdf_casino.iloc[0][filtros_casino[1]] if len(filtros_casino) > 1 else ""
                    direccion_casino = subdf_casino.iloc[0][filtros_casino[2]] if len(filtros_casino) > 2 else ""

                    pdf.set_font("Arial", "B", 12)
                    pdf.cell(0, 8, f"Casino {codigo} - {nombre_casino}", ln=True)
                    pdf.set_font("Arial", "", 10)
                    if direccion_casino:
                        pdf.cell(0, 6, f"Direcci\u00f3n: {direccion_casino}", ln=True)
                    pdf.ln(3)

                    agrupador_maquina = filtros_maquina[0] if len(filtros_maquina) > 0 else None
                    for asset, subdf_maquina in subdf_casino.groupby(agrupador_maquina) if agrupador_maquina else [("", subdf_casino)]:
                        marca = subdf_maquina.iloc[0][filtros_maquina[1]] if len(filtros_maquina) > 1 else ""
                        modelo = subdf_maquina.iloc[0][filtros_maquina[2]] if len(filtros_maquina) > 2 else ""

                        pdf.set_font("Arial", "B", 11)
                        pdf.cell(0, 7, f"  Maquina {asset} - {marca} {modelo}", ln=True)
                        pdf.set_font("Arial", "", 10)
                        pdf.ln(1)

                        pdf.set_font("Courier", "I", 9)
                        pdf.cell(25, 6, "Fecha", 1)
                        pdf.cell(20, 6, "In", 1, align="R")
                        pdf.cell(20, 6, "Out", 1, align="R")
                        pdf.cell(25, 6, "Jackpot", 1, align="R")
                        pdf.cell(25, 6, "Billetero", 1, align="R")
                        pdf.ln()

                        for _, row in subdf_maquina.iterrows():
                            pdf.cell(25, 6, str(row.get("fecha", "")), 1)
                            pdf.cell(20, 6, f'{row.get("in", 0):.2f}', 1, align="R")
                            pdf.cell(20, 6, f'{row.get("out", 0):.2f}', 1, align="R")
                            pdf.cell(25, 6, f'{row.get("jackpot", 0):.2f}', 1, align="R")
                            pdf.cell(25, 6, f'{row.get("billetero", 0):.2f}', 1, align="R")
                            pdf.ln()
                        pdf.ln(4)

                    pdf.ln(6)
            else:
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 10, "No hay datos agrupables por casino.", ln=True)

            # --- Guardar el archivo ---
            
            ruta = os.path.join(BASE_DIR,"Data","Reportes",f"{nombre}.pdf")
            pdf.output(ruta)
            return ruta

    def generar_reporte_individual_maquina(self,assets_maquinas:list,maquinas:list,formato:str,nombre:str)->str:
        df = pd.DataFrame([c.to_dict() for c in maquinas])
        df = df.loc[df["asset"].isin(assets_maquinas),["asset","marca","modelo","serial","denominacion","estado","casino"]]
        if formato == "excel":
            ruta = os.path.join(BASE_DIR,"Data","Reportes",f"{nombre}.xlsx")
            df.to_excel(ruta, index=False)
            return ruta
        elif formato == "pdf":
            with open(os.path.join(BASE_DIR,"Data","datos_empresa.txt"), "r") as f:
                nombre_empresa = f.readline().strip()
                telefono = f.readline().strip()
                nit = f.readline().strip()
                direccion_emp = f.readline().strip()
                
            pdf = FPDF(orientation="P", unit="mm", format="A4")
            pdf.add_page()

            # — Encabezado principal —
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "REPORTE INVENTARIO DE MAQUINAS", ln=True, align="C")

            fecha_hoy = datetime.date.today().strftime("%Y-%m-%d")
            pdf.set_font("Arial", "", 12)
            pdf.cell(0, 8, f"Fecha de emisión: {fecha_hoy}", ln=True, align="C")
            pdf.ln(6)

            # — Datos empresa —
            pdf.set_font("Helvetica", "B", 12)
            pdf.cell(0, 6, nombre_empresa, ln=True)
            pdf.set_font("Helvetica", "", 10)
            pdf.cell(0, 5, f"Tel: {telefono}   NIT: {nit}", ln=True)
            pdf.cell(0, 5, f"Dirección: {direccion_emp}", ln=True)
            pdf.ln(8)

            # — Tabla de máquinas —
            # Cabeceras
            pdf.set_font("Courier", "B", 10)
            headers = ["Asset","Marca","Modelo","Serial","Denominacion","Estado","Casino"]
            widths  = [20, 20, 20, 20, 30, 20, 20]
            for h, w in zip(headers, widths):
                pdf.cell(w, 7, h, border=1, align="C")
            pdf.ln()

            # Filas
            pdf.set_font("Courier", "", 9)
            for _, row in df.iterrows():
                pdf.cell(widths[0], 6, str(row["asset"]), border=1)
                pdf.cell(widths[1], 6, str(row["marca"]), border=1)
                pdf.cell(widths[2], 6, str(row["modelo"]), border=1)
                pdf.cell(widths[3], 6, str(row["serial"]), border=1)
                pdf.cell(widths[4], 6, str(row["denominacion"]), border=1, align="R")
                pdf.cell(widths[5], 6, f'{row["estado"]}', border=1, align="R")
                pdf.cell(widths[6], 6, f'{row["casino"]}', border=1, align="R")
                pdf.ln()

            # Guardar
            ruta = os.path.join(BASE_DIR,"Data","Reportes",f"{nombre}.pdf")
            pdf.output(ruta)
            return ruta
            
    
    def generar_reporte_individual_casino(self,codigos_casinos,maquinas:list,casinos:list,formato:str,nombre:str)->str:
        dict_casinos=[c.to_dict() for c in casinos]
        for maquina in maquinas:
            for dic in dict_casinos:
                if maquina.casino.codigo == dic["codigo"]:
                    if "maquinas" not in dic.keys():
                        dic["maquinas"]=f"{maquina.asset}\n"
                    else:
                        dic["maquinas"]+=f"{maquina.asset}\n"
                    
        df = pd.DataFrame([dicc for dicc in dict_casinos])
        df = df.loc[df["codigo"].isin(codigos_casinos),["codigo","nombre","direccion","estado","maquinas"]]
        if formato == "excel":
            ruta = os.path.join(BASE_DIR,"Data","Reportes",f"{nombre}.xlsx")
            df.to_excel(ruta, index=False)
            return ruta
        elif formato == "pdf":
            with open(os.path.join(BASE_DIR,"Data","datos_empresa.txt"), "r") as f:
                nombre_empresa = f.readline().strip()
                telefono = f.readline().strip()
                nit = f.readline().strip()
                direccion_emp = f.readline().strip()
            
            pdf = FPDF(orientation="P", unit="mm", format="A4")
            pdf.add_page()

            # — Encabezado principal —
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "REPORTE INVENTARIO DE CASINOS", ln=True, align="C")

            hoy = datetime.date.today().strftime("%Y-%m-%d")
            pdf.set_font("Arial", "", 12)
            pdf.cell(0, 8, f"Fecha de emisión: {hoy}", ln=True, align="C")
            pdf.ln(6)

            # — Datos de la empresa —
            pdf.set_font("Helvetica", "B", 12)
            pdf.cell(0, 6, nombre_empresa, ln=True)
            pdf.set_font("Helvetica", "", 10)
            pdf.cell(0, 5, f"Tel: {telefono}   NIT: {nit}", ln=True)
            pdf.cell(0, 5, f"Dirección: {direccion_emp}", ln=True)
            pdf.ln(8)

            # — Recorremos cada casino —
            for _, row in df.iterrows():
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 8, f"Casino {row['codigo']} - {row['nombre']}", ln=True)
                pdf.set_font("Arial", "", 10)
                pdf.cell(0, 6, f"Dirección: {row['direccion']}", ln=True)
                pdf.cell(0, 6, f"Estado: {row['estado']}", ln=True)
                pdf.ln(3)

                # Lista de máquinas (previamente concatenadas con '\n')
                pdf.set_font("Courier", "", 10)
                maquinas = str(row["maquinas"]).split("\n")
                for asset in maquinas:
                    asset = asset.strip()
                    if not asset:
                        continue
                    pdf.cell(0, 6, f"  - Máquina asset: {asset}", ln=True)
                pdf.ln(6)

            ruta = os.path.join(BASE_DIR,"Data","Reportes",f"{nombre}.pdf")
            pdf.output(ruta)
            return ruta
    
    def generar_reporte_consolidado(self,cuadre_por_casino:list,cuadre_por_maquina:list,fecha_inicio,fecha_fin,formato:str,nombre:str)->str:
        
        # 1) Crear DataFrames desde los to_dict() de cada lista
        df_casino = pd.DataFrame([c.to_dict() for c in cuadre_por_casino])
        df_maquina = pd.DataFrame([m.to_dict() for m in cuadre_por_maquina])

        # Filtrar solo columnas necesarias
        columnas_casino = ["codigo","fecha", "in", "out", "jackpot", "billetero", "utilidad"]
        df_casino = df_casino[[c for c in columnas_casino if c in df_casino.columns]]

        columnas_maquina = ["asset", "casino_codigo","fecha", "in", "out", "jackpot", "billetero", "utilidad"]
        df_maquina = df_maquina[[c for c in columnas_maquina if c in df_maquina.columns]]
        
        if formato == "excel":
            ruta = os.path.join(BASE_DIR,"Data","Reportes",f"{nombre}.xlsx")
            # Crear un Excel con dos hojas: Cuadre_Casino y Cuadre_Maquina
            with pd.ExcelWriter(ruta, engine="openpyxl") as writer:
                df_casino.to_excel(writer, sheet_name="Cuadre_Casino", index=False)
                df_maquina.to_excel(writer, sheet_name="Cuadre_Maquina", index=False)
            return ruta
        elif formato == "pdf":
            with open(os.path.join(BASE_DIR,"Data","datos_empresa.txt"), "r") as f:
                nombre_empresa = f.readline().strip()
                telefono = f.readline().strip()
                nit = f.readline().strip()
                direccion_emp = f.readline().strip()
            
            pdf = FPDF(orientation="P", unit="mm", format="A4")
            pdf.add_page()

            # -- Encabezado principal --
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "REPORTE CONSOLIDADO", ln=True, align="C")

            # Fecha de emisión
            hoy = datetime.date.today().strftime("%Y-%m-%d")
            pdf.set_font("Arial", "", 12)
            pdf.cell(0, 8, f"Fecha de emisión: {hoy}", ln=True, align="C")
            pdf.ln(6)

            # -- Datos de la empresa --
            pdf.set_font("Helvetica", "B", 12)
            pdf.cell(0, 6, nombre_empresa, ln=True)
            pdf.set_font("Helvetica", "", 10)
            pdf.cell(0, 5, f"Tel: {telefono}   NIT: {nit}", ln=True)
            pdf.cell(0, 5, f"Dirección: {direccion_emp}", ln=True)
            pdf.ln(8)

            # -- Sección: Cuadre por Casino --
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 8, "Cuadre por Casino", ln=True)
            pdf.ln(4)

            # Encabezados de tabla: incluir Fecha
            pdf.set_font("Courier", "B", 10)
            encabezado_cas = ["Código","Fecha","In","Out","Jackpot","Billetero","Utilidad"]
            anchos_cas =     [20,     25,    25,    25,       30,         30,        30]
            for texto, ancho in zip(encabezado_cas, anchos_cas):
                pdf.cell(ancho, 7, texto, border=1, align="C")
            pdf.ln()
            pdf.set_font("Courier", "", 9)
            for _, row in df_casino.iterrows():
                inicio,fin=str(row.get("fecha", "")).split("/")
                x_actual = pdf.get_x()
                y_actual = pdf.get_y()
                pdf.cell(anchos_cas[0], 6, str(row["codigo"]), border=1)
                pdf.set_xy(x_actual + anchos_cas[0], y_actual)
                pdf.multi_cell(anchos_cas[1],3,f"{inicio}\n{fin}", border=1)
                pdf.set_xy(x_actual + anchos_cas[0] + anchos_cas[1], y_actual)
                pdf.cell(anchos_cas[2], 6, f'{row.get("in", 0):.2f}', border=1, align="R")
                pdf.cell(anchos_cas[3], 6, f'{row.get("out", 0):.2f}', border=1, align="R")
                pdf.cell(anchos_cas[4], 6, f'{row.get("jackpot", 0):.2f}', border=1, align="R")
                pdf.cell(anchos_cas[5], 6, f'{row.get("billetero", 0):.2f}', border=1, align="R")
                pdf.cell(anchos_cas[6], 6, f'{row.get("utilidad", 0):.2f}', border=1, align="R")
                pdf.ln()
            pdf.ln(8)

            # -- Sección: Cuadre por Máquina --
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 8, "Cuadre por Máquina", ln=True)
            pdf.ln(4)

            # Encabezados de tabla: incluir Fecha
            pdf.set_font("Courier", "B", 10)
            encabezado_maq = ["Asset","Casino","Fecha","In","Out","Jackpot","Billetero","Utilidad"]
            anchos_maq =     [20,     25,      25,    20,    20,       25,        25,        30]
            for texto, ancho in zip(encabezado_maq, anchos_maq):
                pdf.cell(ancho, 7, texto, border=1, align="C")
            pdf.ln()

            pdf.set_font("Courier", "", 9)
            for _, row in df_maquina.iterrows():
                inicio,fin=str(row.get("fecha", "")).split("/")
                x = pdf.get_x()
                y = pdf.get_y()
                h = 6  
                h_total = 2 * 3 
                pdf.set_xy(x, y)
                pdf.cell(anchos_maq[0], 6, str(row["asset"]), border=1)
                pdf.set_xy(x + anchos_maq[0], y)
                pdf.cell(anchos_maq[1], 6, str(row.get("casino_codigo", "")), border=1)
                pdf.set_xy(x + anchos_maq[0] + anchos_maq[1], y)
                pdf.multi_cell(anchos_maq[1],3,f"{inicio}\n{fin}", border=1)
                pdf.set_xy(x_actual + anchos_maq[0] + anchos_maq[1], y_actual)
                x_dato = x + sum(anchos_maq[:3])
                pdf.set_xy(x_dato, y)
                pdf.cell(anchos_maq[3], 6, f'{row.get("in", 0):.2f}', border=1, align="R")
                pdf.cell(anchos_maq[4], 6, f'{row.get("out", 0):.2f}', border=1, align="R")
                pdf.cell(anchos_maq[5], 6, f'{row.get("jackpot", 0):.2f}', border=1, align="R")
                pdf.cell(anchos_maq[6], 6, f'{row.get("billetero", 0):.2f}', border=1, align="R")
                pdf.cell(anchos_maq[7], 6, f'{row.get("utilidad", 0):.2f}', border=1, align="R")
                pdf.ln()
                
            ruta = os.path.join(BASE_DIR,"Data","Reportes",f"{nombre}.pdf")
            pdf.output(ruta)
            return ruta
        
    
    def generar_reporte_especial(self,gestor,inico,fin,codigo_casino:int,assets_maquinas:list,contadores:list,porcentaje:float,formato:str,nombre:str)->str:
        utilidad=[]
        
        for i in assets_maquinas:
            a= gestor.calculo_utilidad_maquina(inico,fin,i,contadores)
            utilidad.append(a)

        utilidad_total= sum(u for u in utilidad if u is not None)
        participacion = (utilidad_total*porcentaje)/100

        df = pd.DataFrame([{
            "Codigo": codigo_casino,
            "Assets": ", ".join(str(asset) for asset in assets_maquinas),
            "Porcentaje": porcentaje,
            "Utilidad": utilidad_total,
            "Participacion":participacion

        }])

        if formato =="excel":
            ruta= os.path.join(BASE_DIR,"Data","Reportes",f"{nombre}.xlsx")
            df.to_excel(ruta,index=False)
            return ruta
        
        elif formato =="pdf":
            with open(os.path.join(BASE_DIR,"Data","datos_empresa.txt"), "r") as f:
                nombre_empresa = f.readline().strip()
                telefono = f.readline().strip()
                nit = f.readline().strip()
                direccion_emp = f.readline().strip()
                
            pdf = FPDF(orientation="P", unit="mm", format="A4")
            pdf.add_page()
            
            
            # -- Encabezado principal --
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "REPORTE Especial", ln=True, align="C")

            # Fecha de emisión
            hoy = datetime.date.today().strftime("%Y-%m-%d")
            pdf.set_font("Arial", "", 12)
            pdf.cell(0, 8, f"Fecha de emisión: {hoy}", ln=True, align="C")
            pdf.ln(6)

            # -- Datos de la empresa --
            pdf.set_font("Helvetica", "B", 12)
            pdf.cell(0, 6, nombre_empresa, ln=True)
            pdf.set_font("Helvetica", "", 10)
            pdf.cell(0, 5, f"Tel: {telefono}   NIT: {nit}", ln=True)
            pdf.cell(0, 5, f"Dirección: {direccion_emp}", ln=True)
            pdf.ln(8)
            

            pdf.set_font("Arial", style='B', size=14)
            pdf.cell(200, 10, txt=f"Reporte del Casino: {codigo_casino}", ln=True, align='C')
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Fecha inicial: {inico} | Fecha final: {fin}", ln=True, align='C')
            pdf.ln(10)

            # Definimos los anchos de columna (ajusta según el texto esperado)
            col_widths = [30, 60, 30, 30, 40]  # Debe sumar menos que el ancho de página (aprox 190mm para A4 margen incluido)

            # Encabezados de la tabla
            pdf.set_font("Arial", style='B', size=12)
            for i, col in enumerate(df.columns):
                pdf.cell(col_widths[i], 10, col, border=1, align='C')
            pdf.ln()

            # Datos de la tabla (primera fila del DataFrame)
            pdf.set_font("Arial", size=12)
            for i, col in enumerate(df.columns):
                valor = str(df.iloc[0][col])
                pdf.cell(col_widths[i], 10, valor, border=1, align='C')
            pdf.ln()

            ruta = os.path.join(BASE_DIR,"Data","Reportes", f"{nombre}.pdf")
            pdf.output(ruta)
            return ruta