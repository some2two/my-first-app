import streamlit as st

st.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")

price = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0, value=0.0)
discount = st.number_input("กรอกส่วนลด (%):", min_value=0.0, value=0.0)

st.divider()

sale_price = price * discount / 100
vat = (price - sale_price) * 0.07
net_price = (price - sale_price) + vat

show_price = f"• ราคาสินค้า: {price:.2f} บาท"
show_discount = f"• เปอร์เซ็นต์ส่วนลด: {discount:.0f}%"
show_sale_price = f"• ส่วนลด ({discount:.0f}%): -{sale_price:.2f} บาท"
show_vat = f"• ภาษีมูลค่าเพิ่ม (VAT 7%): +{vat:.2f} บาท"
show_net_price = f"• ราคาสุทธิที่ต้องจ่าย: {net_price:.2f} บาท"

st.write(show_sale_price)
st.write(f"• ราคาหลังหักส่วนลด: {price - sale_price:.2f} บาท")
st.write(show_vat)
st.subheader(show_net_price)

st.divider()

st.write("นาย รชต อินต๊ะจา เลขที่ 2 ม.4/5")
