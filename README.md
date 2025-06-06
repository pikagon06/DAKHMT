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
