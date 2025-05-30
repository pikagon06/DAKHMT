Dự đoán Ung thư Phổi Bằng KNN
Tổng Quan
Dự án này dự đoán nguy cơ ung thư phổi dựa trên dữ liệu bệnh nhân, sử dụng mô hình K-Nearest Neighbors (KNN). Bao gồm một Jupyter Notebook để phân tích dữ liệu và huấn luyện mô hình, cùng với ứng dụng Streamlit để dự đoán dễ dàng.
Mục Tiêu
Phân tích các thuộc tính của bệnh nhân (tuổi, giới tính, hút thuốc, v.v.) để dự đoán nguy cơ ung thư phổi, hỗ trợ phát hiện sớm và nâng cao nhận thức.
Tập Dữ Liệu

Nguồn: Data/survey lung cancer.csv
Các Thuộc Tính:
GENDER: M (Nam), F (Nữ)
AGE: Tuổi của bệnh nhân
SMOKING: 1 (Không), 2 (Có)
YELLOW_FINGERS: 1 (Không), 2 (Có)
ANXIETY: 1 (Không), 2 (Có)
PEER_PRESSURE: 1 (Không), 2 (Có)
CHRONIC DISEASE: 1 (Không), 2 (Có)
FATIGUE: 1 (Không), 2 (Có)
ALLERGY: 1 (Không), 2 (Có)
WHEEZING: 1 (Không), 2 (Có)
ALCOHOL CONSUMING: 1 (Không), 2 (Có)
COUGHING: 1 (Không), 2 (Có)
SHORTNESS OF BREATH: 1 (Không), 2 (Có)
SWALLOWING DIFFICULTY: 1 (Không), 2 (Có)
CHEST PAIN: 1 (Không), 2 (Có)
LUNG_CANCER: NO (Âm tính), YES (Dương tính)



Yêu Cầu

Python 3.6 trở lên
Cài đặt các thư viện:pip install streamlit numpy joblib pandas matplotlib seaborn scikit-learn



Cài Đặt

Sao chép kho lưu trữ:git clone <đường-dẫn-kho-lưu-trữ>


Chuyển đến thư mục dự án:cd <thư-mục-dự-án>


Cài đặt các gói cần thiết:pip install -r requirements.txt


Đảm bảo tệp Model/knn_model.pkl và Model/scaler.pkl nằm trong thư mục Model.

Hướng Dẫn Sử Dụng

Notebook (lung-cancer-prediction.ipynb):
Mở bằng Jupyter Notebook.
Chạy từng ô để khám phá dữ liệu, huấn luyện mô hình KNN và đánh giá hiệu suất (độ chính xác: 92.86%).


Ứng Dụng Streamlit (app.py):
Chạy ứng dụng:streamlit run app.py


Nhập thông tin bệnh nhân ở thanh bên:
Chọn giới tính (Nam/Nữ)
Nhập tuổi (10-100)
Chọn Có/Không cho các triệu chứng (hoặc dán chuỗi như "1 2 1 1 2 1 2 2 1 1 2 2 1")


Nhấn "🧠 Dự đoán" để xem kết quả.



Mô Hình

Thuật Toán: K-Nearest Neighbors (KNN)
Độ Chính Xác: 92.86% trên tập dữ liệu kiểm tra
Tệp Đã Lưu:
Model/knn_model.pkl: Mô hình KNN đã huấn luyện
Model/scaler.pkl: Bộ chuẩn hóa dữ liệu



Tác Giả

Họ và Tên: Lê Doãn Anh
Mã Sinh Viên: 2121050186
Lớp: DCCTCT66_07E
Giảng Viên Hướng Dẫn: ThS. Nguyễn Thị Phương Bắc

Lưu Ý

Đây là công cụ dự đoán, không thay thế chẩn đoán y tế. Hãy tham khảo ý kiến bác sĩ để đánh giá chính xác.
Đảm bảo tệp dữ liệu và mô hình nằm đúng thư mục trước khi chạy.

