# Dự Dự Đoán Ung Thư Phổi Bằng KNN

## 🌟 Tổng Quan
Dự án này sử dụng mô hình K-Nearest Neighbors (KNN) để dự đoán nguy cơ ung thư phổi dựa trên dữ liệu bệnh nhân. Nó bao gồm:

- **Jupyter Notebook**: Phân tích dữ liệu và huấn luyện mô hình.
- **Ứng Dụng Streamlit**: Giao diện người dùng thân thiện để nhập thông tin và nhận dự đoán.

## 🎯 Mục Tiêu
Mục tiêu chính của dự án là phân tích các thuộc tính bệnh nhân như tuổi, giới tính, thói quen hút thuốc và các triệu chứng để:

- Dự đoán nguy cơ ung thư phổi.
- Hỗ trợ phát hiện sớm và nâng cao nhận thức về bệnh.

## 📊 Tập Dữ Liệu

**Nguồn Dữ Liệu**: `Data/survey lung cancer.csv`  
Dưới đây là các thuộc tính trong tập dữ liệu:

| Thuộc Tính              | Mô Tả                                                              |
|-------------------------|--------------------------------------------------------------------|
| **GENDER**              | M (Nam), F (Nữ)                                                   |
| **AGE**                 | Tuổi của bệnh nhân                                                |
| **SMOKING**             | 1 (Không), 2 (Có)                                                 |
| **YELLOW_FINGERS**      | 1 (Không), 2 (Có)                                                 |
| **ANXIETY**             | 1 (Không), 2 (Có)                                                 |
| **PEER_PRESSURE**       | 1 (Không), 2 (Có)                                                 |
| **CHRONIC DISEASE**     | 1 (Không), 2 (Có)                                                 |
| **FATIGUE**             | 1 (Không), 2 (Có)                                                 |
| **ALLERGY**             | 1 (Không), 2 (Có)                                                 |
| **WHEEZING**            | 1 (Không), 2 (Có)                                                 |
| **ALCOHOL CONSUMING**   | 1 (Không), 2 (Có)                                                 |
| **COUGHING**            | 1 (Không), 2 (Có)                                                 |
| **SHORTNESS OF BREATH** | 1 (Không), 2 (Có)                                                 |
| **SWALLOWING DIFFICULTY**| 1 (Không), 2 (Có)                                                |
| **CHEST PAIN**          | 1 (Không), 2 (Có)                                                 |
| **LUNG_CANCER**         | NO (Âm tính), YES (Dương tính)                                    |

## 🛠 Yêu Cầu

- **Python**: 3.6 trở lên
- Các thư viện cần cài đặt:

```bash
pip install streamlit numpy joblib pandas matplotlib seaborn scikit-learn
Dự Đoán Ung Thư Phổi
Dự án sử dụng mô hình KNN để dự đoán ung thư phổi dựa trên dữ liệu triệu chứng.
Cài Đặt
Yêu Cầu

Python 3.x
Jupyter Notebook
Streamlit
Git

Hướng Dẫn Cài Đặt

Sao chép kho lưu trữgit clone <đường-dẫn-kho-lưu-trữ>


Chuyển đến thư mục dự áncd <thư-mục-dự-án>


Cài đặt các gói cần thiếtpip install -r requirements.txt


Kiểm tra tệp mô hìnhĐảm bảo các tệp sau có trong thư mục Model:
Model/knn_model.pkl: Mô hình KNN đã huấn luyện.
Model/scaler.pkl: Bộ chuẩn hóa dữ liệu.



Hướng Dẫn Sử Dụng
1. Notebook (lung-cancer-prediction.ipynb)

Mở bằng Jupyter Notebook.
Chạy từng ô để:
Khám phá dữ liệu.
Huấn luyện mô hình KNN.
Đánh giá hiệu suất (độ chính xác: 92.86%).



2. Ứng Dụng Streamlit (app.py)

Chạy ứng dụng:streamlit run app.py


Nhập thông tin:
Giới tính: Nam/Nữ.
Tuổi: 10-100.
Triệu chứng: Chọn Có/Không hoặc dán chuỗi (ví dụ: 1 2 1 1 2 1 2 2 1 1 2 2 1).


Nhấn 🧠 Dự đoán để xem kết quả.

Mô Hình

Thuật Toán: K-Nearest Neighbors (KNN)
Độ Chính Xác: 92.86% trên tập kiểm tra
Tệp Đã Lưu:
Model/knn_model.pkl
Model/scaler.pkl



Tác Giả

Họ và Tên: Lê Doãn Anh
Mã Sinh Viên: 2121050186
Lớp: DCCTCT66_07E
Giảng Viên Hướng Dẫn: ThS. Nguyễn Thị Phương Bắc

Lưu Ý

Công cụ này chỉ mang tính dự đoán, không thay thế chẩn đoán y tế. Hãy tham khảo ý kiến bác sĩ.
Đảm bảo các tệp dữ liệu và mô hình được đặt đúng thư mục trước khi chạy.


