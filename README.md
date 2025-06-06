# 🩺 Dự Đoán Ung Thư Phổi Bằng KNN

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Accuracy](https://img.shields.io/badge/Độ%20Chính%20Xác-92.86%25-brightgreen.svg)

## 🌟 Tổng Quan

Dự án sử dụng thuật toán **K-Nearest Neighbors (KNN)** để dự đoán nguy cơ ung thư phổi dựa trên dữ liệu bệnh nhân. Bao gồm:

- **Jupyter Notebook**: Phân tích dữ liệu, huấn luyện và đánh giá mô hình.
- **Ứng dụng Streamlit**: Giao diện thân thiện để nhập thông tin và nhận dự đoán.

## 🎯 Mục Tiêu

- Dự đoán nguy cơ ung thư phổi dựa trên các thuộc tính như tuổi, giới tính, thói quen hút thuốc và triệu chứng.
- Hỗ trợ phát hiện sớm và nâng cao nhận thức về ung thư phổi.

## 📊 Tập Dữ Liệu

**Nguồn**: `Data/survey_lung_cancer.csv`

**Thuộc Tính**:

| Thuộc Tính                | Mô Tả                          |
|---------------------------|--------------------------------|
| GENDER                    | M (Nam), F (Nữ)               |
| AGE                       | Tuổi của bệnh nhân            |
| SMOKING                   | 1 (Không), 2 (Có)             |
| YELLOW_FINGERS            | 1 (Không), 2 (Có)             |
| ANXIETY                   | 1 (Không), 2 (Có)             |
| PEER_PRESSURE             | 1 (Không), 2 (Có)             |
| CHRONIC DISEASE           | 1 (Không), 2 (Có)             |
| FATIGUE                   | 1 (Không), 2 (Có)             |
| ALLERGY                   | 1 (Không), 2 (Có)             |
| WHEEZING                  | 1 (Không), 2 (Có)             |
| ALCOHOL CONSUMING         | 1 (Không), 2 (Có)             |
| COUGHING                  | 1 (Không), 2 (Có)             |
| SHORTNESS OF BREATH       | 1 (Không), 2 (Có)             |
| SWALLOWING DIFFICULTY     | 1 (Không), 2 (Có)             |
| CHEST PAIN                | 1 (Không), 2 (Có)             |
| LUNG_CANCER               | NO (Âm tính), YES (Dương tính) |

## 🛠 Yêu Cầu

- **Python**: 3.6 trở lên
- **Thư viện**:
  ```bash
  pip install streamlit numpy joblib pandas matplotlib seaborn scikit-learn
  ```

## 🔧 Cài Đặt

1. **Sao chép kho lưu trữ**
   ```bash
   git clone <đường-dẫn-kho-lưu-trữ>
   ```

2. **Chuyển đến thư mục dự án**
   ```bash
   cd <thư-mục-dự-án>
   ```

3. **Cài đặt các gói cần thiết**
   ```bash
   pip install -r requirements.txt
   ```

4. **Kiểm tra tệp mô hình**
   Đảm bảo các tệp sau nằm trong thư mục `Model`:
   - `Model/knn_model.pkl`: Mô hình KNN đã huấn luyện.
   - `Model/scaler.pkl`: Bộ chuẩn hóa dữ liệu.

## 📖 Hướng Dẫn Sử Dụng

### 1. Jupyter Notebook (`lung-cancer-prediction.ipynb`)
- Mở bằng Jupyter Notebook.
- Chạy từng ô để:
  - Khám phá dữ liệu.
  - Huấn luyện mô hình KNN.
  - Đánh giá hiệu suất (độ chính xác: **92.86%**).

### 2. Ứng Dụng Streamlit (`app.py`)
- Chạy ứng dụng:
  ```bash
  streamlit run app.py
  ```
- Nhập thông tin:
  - **Giới tính**: Chọn Nam/Nữ.
  - **Tuổi**: Nhập giá trị từ 10 đến 100.
  - **Triệu chứng**: Chọn Có/Không 
- Nhấn nút **🧠 Dự đoán** để xem kết quả.

## 🤖 Mô Hình

- **Thuật Toán**: K-Nearest Neighbors (KNN)
- **Độ Chính Xác**: 92.86% trên tập kiểm tra
- **Tệp Đã Lưu**:
  - `Model/knn_model.pkl`: Mô hình KNN đã huấn luyện.
  - `Model/scaler.pkl`: Bộ chuẩn hóa dữ liệu.

## 👨‍🎓 Tác Giả

- **Họ và Tên**: Lê Doãn Anh
- **Mã Sinh Viên**: 2121050186
- **Lớp**: DCCTCT66_07E
- **Giảng Viên Hướng Dẫn**: ThS. Nguyễn Thị Phương Bắc

## ⚠️ Lưu Ý

- Đây là công cụ dự đoán, **không thay thế chẩn đoán y tế**. Vui lòng tham khảo ý kiến bác sĩ để đánh giá chính xác.
- Đảm bảo các tệp dữ liệu và mô hình được đặt đúng thư mục trước khi chạy.
