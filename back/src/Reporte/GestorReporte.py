import pandas as pd
from fpdf import FPDF
import datetime


class GestorReporte:
    
    def generar_reporte_personalizado(self,filtros_maquina:list,filtros_casino:list,contadores:list,fecha_inicio,fecha_fin,formato:str,nombre:str)->str:
        contadores_rango_fecha=[c for c in contadores if c.fecha >=fecha_inicio and c.fecha <= fecha_fin]
        df = pd.DataFrame([c.to_dict() for c in contadores_rango_fecha])
        filtros=filtros_maquina+filtros_casino+["fecha","in","out","jackpot","billetero"]
        df = df[filtros]
        if formato == "excel":
            ruta = f"CASINO/Data/Reportes/{nombre}.xlsx"
            df.to_excel(ruta, index=False)
            return ruta
        elif formato == "pdf":
            with open("CASINO/Data/datos_empresa.txt", "r") as f:
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
            ruta = f"CASINO/Data/Reportes/{nombre}.pdf"
            pdf.output(ruta)
            return ruta

    def generar_reporte_individual_maquina(self,assets_maquinas:list,maquinas:list,formato:str,nombre:str)->str:
        df = pd.DataFrame([c.to_dict() for c in maquinas])
        df = df.loc[df["asset"].isin(assets_maquinas),["asset","marca","modelo","serial","denominacion","estado","casino"]]
        if formato == "excel":
            ruta = f"CASINO/Data/Reportes/{nombre}.xlsx"
            df.to_excel(ruta, index=False)
            return ruta
        elif formato == "pdf":
            with open("CASINO/Data/datos_empresa.txt", "r") as f:
                nombre_empresa = f.readline().strip()
                telefono = f.readline().strip()
                nit = f.readline().strip()
                direccion_emp = f.readline().strip()
                
            pdf = FPDF(orientation="P", unit="mm", format="A4")
            pdf.add_page()

            # — Encabezado principal —
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "REPORTE DE MAQUINAS", ln=True, align="C")

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
            ruta = f"CASINO/Data/Reportes/{nombre}.pdf"
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
            ruta = f"CASINO/Data/Reportes/{nombre}.xlsx"
            df.to_excel(ruta, index=False)
            return ruta
        elif formato == "pdf":
            with open("CASINO/Data/datos_empresa.txt", "r") as f:
                nombre_empresa = f.readline().strip()
                telefono = f.readline().strip()
                nit = f.readline().strip()
                direccion_emp = f.readline().strip()
            
            pdf = FPDF(orientation="P", unit="mm", format="A4")
            pdf.add_page()

            # — Encabezado principal —
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "REPORTE GLOBAL DE CASINOS", ln=True, align="C")

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

            ruta = f"CASINO/Data/Reportes/{nombre}.pdf"
            pdf.output(ruta)
            return ruta
    
    def generar_reporte_consolidado(self,contadores:list,fecha_inicio,fecha_fin,formato:str,nombre:str)->str:
        """
        generar un reporte en el formato especificado de los contadores en un rango de fecha
        """
        pass
    
    def generar_reporte_especial(self,codigo_casino:int,assets_maquinas:list,contadores:list,porcentaje:float,formato:str,nombre:str)->str:
        """
        generar un reporte en el formato especificado de un casino y una seleccion
        de maquinas del mismo, tambien debe mostrar cual es la participacion
        de este grupo de maquinas en la utilidad total del casino haciendo uso de un 
        porcentaje (mirar especificacion del archivo del proyecto)
        """
        pass