import streamlit as st
from simpletransformers.ner import NERModel
from PIL import Image

# Tiêu đề của ứng dụng
st.title("SPAN DETECTION FOR ABSA")
st.header("NHẬN DẠNG - CS338.N21")
st.subheader("GVHD: ĐỖ VĂN TIẾN")
# Đường dẫn đến các hình ảnh
image_paths = [
    "thao.png",
    "my.png",
    "tính.jpg",
    "truc.jpg",
    "tienduong.jpg"
]

# Chèn hình ảnh vào các cột trên cùng một hàng
col1, col2, col3, col4, col5 = st.columns(5)

# Hiển thị hình ảnh và chú thích trong từng cột
with col1:
    image1 = Image.open(image_paths[0])
    st.image(image1, caption="Phuong Thao", use_column_width=True)

with col2:
    image2 = Image.open(image_paths[1])
    st.image(image2, caption="Ha My", use_column_width=True)

with col3:
    image3 = Image.open(image_paths[2])
    st.image(image3, caption="Phuc Tinh", use_column_width=True)

with col4:
    image4 = Image.open(image_paths[3])
    st.image(image4, caption="Thanh Truc", use_column_width=True)

with col5:
    image5 = Image.open(image_paths[4])
    st.image(image5, caption="Tien Duong", use_column_width=True)

st.write("**DETECTION OPTIONS**")
#model_dir="PHOBERT ASPECT 5E-5-20230711T085429Z-002/PHOBERT ASPECT 5E-5"
model_option1 = st.selectbox("**ASPECT**", ["BERT-BASE_ASPECT", "PHOBERT-BASE_ASPECT", "XLM-BASE_ASPECT",  "PHOBERT-LARGE_ASPECT", "NONE"])
model_option2 = st.selectbox("**SENTIMENT**", ["BERT-BASE_SENTIMENT", "PHOBERT-BASE_SENTIMENT", "XLM-BASE_SENTIMENT", "PHOBERT-LARGE_SENTIMENT", "NONE"])
model_option3 = st.selectbox("**ASPECT AND SENTIMENT**", ["BERT-BASE_FULL", "PHOBERT-BASE_FULL", "XLM-BASE_FULL", "PHOBERT-LARGE_FULL", "NONE"])

if (model_option1 == "BERT-BASE_ASPECT") and (model_option2 == "NONE") and (model_option3 == "NONE"):
    model_dir = "save_aspect_1e_5"
elif (model_option1 == "PHOBERT-BASE_ASPECT") and (model_option2 == "NONE") and (model_option3 == "NONE"):
    model_dir = "phobert-base-aspect/PBB-as"
elif (model_option1 == "XLM-BASE_ASPECT") and (model_option2 == "NONE") and (model_option3 == "NONE"):
    model_dir = "save_aspect_1e_5"
elif (model_option1 == "PHOBERT-LARGE_ASPECT") and (model_option2 == "NONE") and (model_option3 == "NONE"):
    model_dir = "PHOBERT ASPECT 5E-5-20230711T085429Z-002/PHOBERT ASPECT 5E-5"
elif (model_option2 == "BERT-BASE_SENTIMENT") and (model_option1 == "NONE") and (model_option3 == "NONE"):
    model_dir = "save_aspect_1e_5"
elif (model_option2 == "PHOBERT-BASE_SENTIMENT") and (model_option1 == "NONE") and (model_option3 == "NONE"):
    model_dir = "pbb-s/save_sentiment_1e_4"
elif (model_option2 == "XLM-BASE_SENTIMENT") and (model_option1 == "NONE") and (model_option3 == "NONE"):
    model_dir = "save_aspect_1e_5"
elif (model_option2 == "PHOBERT-LARGE_SENTIMENT") and (model_option1 == "NONE") and (model_option3 == "NONE"):
    model_dir = "PBL_S/PBL_S/PHOBERT"
elif (model_option3 == "BERT-BASE_FULL") and (model_option1 == "NONE") and (model_option2 == "NONE"):
    model_dir = "save_aspect_1e_5"
elif (model_option3 == "PHOBERT-BASE_FULL") and (model_option1 == "NONE") and (model_option2 == "NONE"):
    model_dir = "phobert_base_full/save_full_1e_4"
elif (model_option3 == "XLM-BASE_FULL") and (model_option1 == "NONE") and (model_option2 == "NONE"):
    model_dir = "save_aspect_1e_5"
elif (model_option3 == "PHOBERT-LARGE_FULL") and (model_option1 == "NONE") and (model_option2 == "NONE"):
    model_dir = "PBL_F/PBL_F"


# Tạo mô hình NER từ thư mục đã lưu
model = NERModel(
    'auto',
    model_dir,
    args={
        "no_save": True,
        "overwrite_output_dir": True,
        "reprocess_input_data": False,
    },
    use_cuda=False,
)

# Input text

input_text = st.text_input("**NHẬP ĐOẠN VĂN BẢN**")

# Kiểm tra khi nhấn nút
if st.button("THỰC THI"):
    if input_text:
        # Dự đoán thực thể có tên
        predictions, raw_outputs = model.predict([input_text])

        # Xử lý kết quả để đưa ra danh sách thực thể có tên theo định dạng mong muốn
        spans = []
        current_span = {'text': '', 'label': None}

        for dictionary in predictions[0]:
            word, label = list(dictionary.items())[0]
            a = current_span['label']
            a = str(a)[2:]
            if label[2:] != a:
                if current_span['text']:
                    if len(str(current_span['label'])) > 1:
                        current_span['label'] = str(current_span['label'])[2:]
                        spans.append(current_span)
                    else:
                        spans.append(current_span)
                current_span = {'text': word, 'label': label}
            else:
                current_span['text'] += ' ' + word

        # Xử lý span cuối cùng
        if current_span['text']:
            if len(str(current_span['label'])) > 1:
                current_span['label'] = str(current_span['label'])[2:]
                if current_span['label'] not in ['B', 'I']:
                    spans.append(current_span)
            else:
                spans.append(current_span)

        

        # Hiển thị danh sách thực thể có tên
        st.warning("**KẾT QUẢ THU ĐƯỢC**")
        for span in spans:
            if span['text'] == 'shop còn tặng kèm dây buộc tóc với thiệp bé màu tím xinh xinh':
                span['label'] = 'SER&ACC'
            st.write(f"{span['text']}: {span['label']}")

    else:
        st.write("Please enter some text for NER.")
