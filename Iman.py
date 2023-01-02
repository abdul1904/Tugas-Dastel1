import streamlit as st
from streamlit_option_menu import option_menu
import math
from PIL import Image

with st.sidebar :
    selected = option_menu ("Perhitungan Impedansi Karakteristik dan Konstanta Propagasi dan Rasio Daya",
    ["Perhitungan Impedansi Karakteristik",
    "Perhitungan Konstanta Propagasi",
    "Perhitungan Rasio Daya",
    "Perhitungan Rasio Tegangan",
    "Perhitungan Rasio Arus",
    "Perhitungan Rasio Penguatan",
    "Perhitungan Rasio Redaman",],
    default_index=0)

if(selected == "Perhitungan Impedansi Karakteristik") :
    st.title("Ini adalah Saluran Pengganti Transmisi")
    st.image("saluran1.jpg")
    st.title("Rumus Impendansi Karakteristik")
    st.image("Impedansi1.jpg")
    st.title("Perhitungan Impedansi Karakteristik")

    r = st.number_input ("masukan nilai Resistor", 0)
    l= st.number_input ("masukan nilai Induktor", 0)
    c= st.number_input ("masukan nilai Kapasitor", 0)
    g= st.number_input ("masukan nilai Konduktansi", 0)
    f= st.number_input ("masukan nilai frekuensi", 0)
    hitung = st.button ("hitung Impedansi Karakteristik")

    if hitung : 
        Z_Propagasi=(((r+complex(0,2*math.pi*f*l))/(g+complex(0,2*math.pi*f*c)))**0.5)
        st.write("nilai Impedansi Karakteristik adalah = ", Z_Propagasi)
        st.success(f"nilai Impedansi Karakteristik adalah = {Z_Propagasi} ohm")
    
if(selected == "Perhitungan Konstanta Propagasi") :
    st.title("Ini adalah Saluran Pengganti Transmisi")
    st.image("saluran1.jpg")
    st.title("Rumus Konstanta Propagasi")
    st.image("Konstanta1.jpg")
    st.title("Perhitungan Konstanta Propagasi")

    r = st.number_input ("masukan nilai Resistor", 0)
    l= st.number_input ("masukan nilai Induktor", 0)
    c= st.number_input ("masukan nilai Kapasitor", 0)
    g= st.number_input ("masukan nilai Konduktansi", 0)
    f= st.number_input ("masukan nilai frekuensi", 0)
    hitung = st.button ("hitung Konstanta Progagasi")

    if hitung : 
        K_Propagasi=(((r+complex(0,2*math.pi*f*l))*(g+complex(0,2*math.pi*f*c)))**0.5)
        st.write("nilai konstanta propagasi adalah = ", K_Propagasi)
        st.success(f"nilai konstanta propagasi adalah = {K_Propagasi}")
        
if(selected == "Perhitungan Rasio Daya") :
    st.title("Rumus Rasio Daya")
    st.image("dayaa.jpeg")
    st.title("Perhitungan Rasio Daya")
    p1=st.number_input("Masukkan nilai p1 : ",0)
    p2=st.number_input("Masukkan nilai p2: ",0)
    hitung = st.button ("hitung Rasio Daya")
    if hitung : 
        y=(math.log10(p2/p1))*10
        st.write("nilai rasio daya adalah =",y,"dB")
        st.success(f"nilai rasio daya adalah = {y} dB")

if(selected == "Perhitungan Rasio Tegangan") :
    st.title("Rumus Rasio Tegangan")
    st.image("tega.jpeg")
    st.title("Perhitungan Rasio Tegangan")
    V1=st.number_input("Masukkan nilai V1 : ",0)
    V2=st.number_input("Masukkan nilai V2: ",0)
    hitung = st.button ("hitung Rasio Daya")
    if hitung : 
        x=(math.log10(V2/V1))*20
        st.write("nilai rasio tegangan adalah =",x,"dB")
        st.success(f"nilai tegangan adalah = {x} dB")

if(selected == "Perhitungan Rasio Arus") :
    st.title("Rumus Rasio Arus")
    st.image("arus.jpeg")
    st.title("Perhitungan Rasio Arus")
    i1=st.number_input("Masukkan nilai i1 : ",0)
    i2=st.number_input("Masukkan nilai i2: ",0)
    hitung = st.button ("hitung Rasio Daya")
    if hitung : 
        x=(math.log10(i2/i1))*20
        st.write("nilai rasio Arus adalah =",x,"dB")
        st.success(f"nilai Arus  adalah = {x} dB")

if(selected == "Perhitungan Rasio Penguatan") :
    st.title("Perhitungan Rasio Penguatan")
    st.title("Rumus Rasio Penguatan")
    st.image("a.jpeg")
    k=st.number_input("Masukkan nilai penguatan : ",0)
    hitung = st.button ("hitung Rasio penguatan")
    if hitung : 
        x=(math.log10(k/1))*10
        st.write("nilai rasio penguatan adalah =",x,"dB")
        st.success(f"nilai rasio penguatan adalah = {x} dB")

if(selected == "Perhitungan Rasio Redaman") :
    st.title("Perhitungan Rasio Redaman")
    st.title("Rumus Rasio Redaman")
    st.image("b.jpeg")
    k=st.number_input("Masukkan nilai Redaman : ",0)
    hitung = st.button ("hitung Rasio Redaman")
    if hitung : 
        x=(math.log10(1/k))*10
        st.write("nilai rasio Redaman atau loss adalah =",x,"dB")
        st.success(f"nilai rasio Redaman atau loss adalah = {x} dB")
