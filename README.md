🩺 Dự đoán Ung thư Phổi Bằng KNN
🌟 Tổng Quan
Dự án này sử dụng mô hình K-Nearest Neighbors (KNN) để dự đoán nguy cơ ung thư phổi dựa trên dữ liệu bệnh nhân. Nó bao gồm:  

Jupyter Notebook: Phân tích dữ liệu và huấn luyện mô hình.  
Ứng Dụng Streamlit: Giao diện thân thiện để nhập thông tin và nhận dự đoán.


🎯 Mục Tiêu
Phân tích các thuộc tính bệnh nhân như tuổi, giới tính, thói quen hút thuốc, và các triệu chứng để:  

Dự đoán nguy cơ ung thư phổi.  
Hỗ trợ phát hiện sớm và nâng cao nhận thức về bệnh.


📊 Tập Dữ Liệu

Nguồn: Data/survey lung cancer.csv  
Các Thuộc Tính:


Thuộc Tính
Mô Tả



GENDER
M (Nam), F (Nữ)


AGE
Tuổi của bệnh nhân


SMOKING
1 (Không), 2 (Có)


YELLOW_FINGERS
1 (Không), 2 (Có)


ANXIETY
1 (Không), 2 (Có)


PEER_PRESSURE
1 (Không), 2 (Có)


CHRONIC DISEASE
1 (Không), 2 (Có)


FATIGUE
1 (Không), 2 (Có)


ALLERGY
1 (Không), 2 (Có)


WHEEZING
1 (Không), 2 (Có)


ALCOHOL CONSUMING
1 (Không), 2 (Có)


COUGHING
1 (Không), 2 (Có)


SHORTNESS OF BREATH
1 (Không), 2 (Có)


SWALLOWING DIFFICULTY
1 (Không), 2 (Có)


CHEST PAIN
1 (Không), 2 (Có)


LUNG_CANCER
NO (Âm tính), YES (Dương tính)





🛠 Yêu Cầu

Python: 3.6 trở lên  
Cài đặt các thư viện:pip install streamlit numpy joblib pandas matplotlib seaborn scikit-learn




🔧 Cài Đặt

Sao chép kho lưu trữ:git clone <đường-dẫn-kho-lưu-trữ>


Chuyển đến thư mục dự án:cd <thư-mục-dự-án>


Cài đặt các gói cần thiết:pip install -r requirements.txt


Kiểm tra tệp mô hình:
Đảm bảo Model/knn_model.pkl và Model/scaler.pkl nằm trong thư mục Model.




📖 Hướng Dẫn Sử Dụng
1. Notebook (lung-cancer-prediction.ipynb)

Mở bằng Jupyter Notebook.  
Chạy từng ô để:  
Khám phá dữ liệu.  
Huấn luyện mô hình KNN.  
Đánh giá hiệu suất (độ chính xác: 92.86%).



2. Ứng Dụng Streamlit (app.py)

Chạy ứng dụng:streamlit run app.py


Nhập thông tin:
Giới tính: Chọn Nam/Nữ.  
Tuổi: Nhập giá trị từ 10 đến 100.  
Triệu chứng: Chọn Có/Không hoặc dán chuỗi (ví dụ: "1 2 1 1 2 1 2 2 1 1 2 2 1").


Dự đoán:
Nhấn nút "🧠 Dự đoán" để xem kết quả.




🤖 Mô Hình

Thuật Toán: K-Nearest Neighbors (KNN)  
Độ Chính Xác: 92.86% trên tập kiểm tra  
Tệp Đã Lưu:  
Model/knn_model.pkl: Mô hình KNN đã huấn luyện  
Model/scaler.pkl: Bộ chuẩn hóa dữ liệu




👨‍🎓 Tác Giả

Họ và Tên: Lê Doãn Anh  
Mã Sinh Viên: 2121050186  
Lớp: DCCTCT66_07E  
Giảng Viên Hướng Dẫn: ThS. Nguyễn Thị Phương Bắc


⚠️ Lưu Ý

Đây là công cụ dự đoán, không thay thế chẩn đoán y tế. Hãy tham khảo ý kiến bác sĩ để đánh giá chính xác.  
Đảm bảo tệp dữ liệu và mô hình nằm đúng thư mục trước khi chạy.


