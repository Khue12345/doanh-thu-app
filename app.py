import streamlit as st
import pandas as pd

st.title("📊 Tính Tổng Doanh Thu Từ File Excel")

uploaded_file = st.file_uploader("Tải lên file Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Chuẩn hóa tên cột để tránh lỗi chữ hoa/thường
    df.columns = [col.lower().strip() for col in df.columns]

    st.subheader("📋 Dữ liệu của bạn:")
    st.write(df)

    if "doanh thu" in df.columns:
        tong = df["doanh thu"].sum()
        st.success(f"✅ Tổng doanh thu là: **{tong:,.0f}** VND")
    else:
        st.error("❌ Không tìm thấy cột 'Doanh thu' trong file.")
