from io import BytesIO
import pandas as pd
import streamlit as st
import os

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def initialize_session_state():
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = ""
    if "check_analyses" not in st.session_state:
        st.session_state["check_analyses"] = False
    if "cutoff_depth" not in st.session_state:
        st.session_state["cutoff_depth"] = 0
    if "cutoff_qual" not in st.session_state:
        st.session_state["cutoff_qual"] = 0
    if "df_altAF" not in st.session_state:
        st.session_state["df_altAF"] = pd.DataFrame()
    if "df_SNV" not in st.session_state:
        st.session_state["df_SNV"] = pd.DataFrame()
    if "personId" not in st.session_state:
        st.session_state["personId"] = ""
    if "df_sample_bin_stretches" not in st.session_state:
        st.session_state["df_sample_bin_stretches"] = pd.DataFrame()
    if "chr_sel_index" not in st.session_state:
        st.session_state["chr_sel_index"] = 0
    if "tmp_vcf" not in st.session_state:
        st.session_state["tmp_vcf"] = ""
    if "vcfs_downloaded" not in st.session_state:
        st.session_state["vcfs_downloaded"] = False
    if "get_vcfs" not in st.session_state:
        st.session_state["get_vcfs"] = False
    if "plot_vcf" not in st.session_state:
        st.session_state["plot_vcf"] = False
    if "bt_demo" not in st.session_state:
        st.session_state["bt_demo"] = False    
    if "vcf_dict" not in st.session_state:
        st.session_state["vcf_dict"] = {
            "index" : "",
            "mother" : "",
            "father" : "",
        }
    if "vcf_upload" not in st.session_state:
        st.session_state["vcf_upload"] = {
            "index" : "",
            "mother" : "",
            "father" : "",
        }
    
    if "id_dict" not in st.session_state:
        st.session_state["id_dict"] = {
            "index" : "",
            "mother" : "",
            "father" : "",
        }

def delete_vcfs(vcf):
    try:
        if isinstance(vcf,dict):
            for key in vcf:
                if vcf[key]:
                    if os.path.exists(vcf[key]):
                        os.remove(vcf[key])
                    if os.path.exists(vcf[key]+".tbi"):
                        os.remove(vcf[key]+".tbi")
        if isinstance(vcf,str):
            os.remove(vcf)
            os.remove(vcf+".tbi")
    except:
        pass