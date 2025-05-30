import streamlit as st
import numpy as np
import joblib

# Load mô hình và scaler
model = joblib.load("Model/knn_model.pkl")
scaler = joblib.load("Model/scaler.pkl")

st.title("🩺 Dự đoán Ung thư Phổi với KNN")

# Giao diện người dùng
st.sidebar.header("Thông tin bệnh nhân")

# Danh sách các biến Có/Không
yesno_fields = [
    "SMOKING", "YELLOW_FINGERS", "ANXIETY", "PEER_PRESSURE", "CHRONIC DISEASE",
    "FATIGUE", "ALLERGY", "WHEEZING", "ALCOHOL CONSUMING", "COUGHING",
    "SHORTNESS OF BREATH", "SWALLOWING DIFFICULTY", "CHEST PAIN"
]

# Nhập chuỗi dán để tự động cập nhật các lựa chọn
bulk_input = st.sidebar.text_input(
    "Dán chuỗi số (1 là Không, 2 là Có):",
    placeholder="1 2 1 1 2 1 2 2 1 1 2 2 1"
)

# Xử lý chuỗi đầu vào
default_values = ["Không"] * len(yesno_fields)
if bulk_input:
    try:
        values = list(map(int, bulk_input.strip().split()))
        default_values = ["Có" if v == 2 else "Không" for v in values]
    except:
        st.sidebar.error("⚠️ Chuỗi không hợp lệ! Đảm bảo chỉ có số 1 hoặc 2.")

def user_input():
    gender = st.sidebar.selectbox("Giới tính", ("Nam", "Nữ"))
    age = st.sidebar.number_input("Tuổi", min_value=10, max_value=100, value=30)

    # Hàm chọn Có/Không từ default
    def get_option(label, idx):
        return st.sidebar.selectbox(label, ("Không", "Có"), index=(1 if default_values[idx] == "Có" else 0))

    # Lấy các lựa chọn
    smoking = get_option("Hút thuốc", 0)
    yellow_fingers = get_option("Ngón tay vàng", 1)
    anxiety = get_option("Lo âu", 2)
    peer_pressure = get_option("Áp lực từ bạn bè", 3)
    chronic_disease = get_option("Bệnh mãn tính", 4)
    fatigue = get_option("Mệt mỏi", 5)
    allergy = get_option("Dị ứng", 6)
    wheezing = get_option("Thở khò khè", 7)
    alcohol = get_option("Uống rượu", 8)
    coughing = get_option("Ho", 9)
    breath = get_option("Khó thở", 10)
    swallow = get_option("Khó nuốt", 11)
    chest_pain = get_option("Đau ngực", 12)

    # Chuyển về dạng số cho model
    gender = 1 if gender == "Nam" else 0
    yesno = lambda x: 1 if x == "Không" else 2  # 1: Không, 2: Có
    features = [
        age, gender, yesno(smoking), yesno(chest_pain), yesno(breath), yesno(coughing), yesno(peer_pressure),
        yesno(chronic_disease), yesno(swallow), yesno(yellow_fingers), yesno(anxiety), yesno(fatigue),
        yesno(allergy), yesno(wheezing), yesno(alcohol)
    ]
    return np.array(features).reshape(1, -1)

# Lấy dữ liệu đầu vào
input_data = user_input()

# Nút dự đoán
if st.button("🧠 Dự đoán"):
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    if prediction[0] == 1:
        st.error("⚠️ Cảnh báo: Bệnh nhân có nguy cơ MẮC UNG THƯ PHỔI.")
        st.image("https://i.imgur.com/U3vTGjX.png", caption="Cùng chia sẻ và hỗ trợ bệnh nhân 🙏", use_container_width=True)
    else:
        st.success("✅ Bệnh nhân KHÔNG có nguy cơ ung thư phổi.")
        st.balloons()
        st.markdown("🎉 **Chúc mừng! Tiếp tục duy trì lối sống lành mạnh nhé.**")
