import os
import streamlit as st
import docx2python
import pypandoc

st.title("Word to Word Converter")

# 上传Word文件
uploaded_file = st.file_uploader("Upload a Word file", type='docx')

# 如果有上传的文件，就将其转换为Markdown文本
if uploaded_file is not None:
    # 读取上传的Word文件内容
    docx = docx2python.docx2python(uploaded_file)
    
    # 将Word文档转换为Markdown文本
    md = pypandoc.convert_text(docx.text, "md", format="docx", outputfile="output.md")

    # 处理Markdown文本（这里只是一个示例，你可以根据自己的需求进行修改）
    sections = md.split("\n# ")[1:]
    processed_sections = []
    for section in sections:
        header, *lines = section.split("\n")
        processed_lines = [f"* {line}" for line in lines]
        processed_section = "\n".join([header] + processed_lines)
        processed_sections.append(processed_section)
    processed_md = "\n\n".join(processed_sections)

    # 将Markdown文本转换为Word文档
    output_file = "output.docx"
    pypandoc.convert_text(processed_md, "docx", format="md", outputfile=output_file)

    # 显示Word文档下载链接
    st.subheader("Download Word Document")
    with open(output_file, "rb") as file:
        file_bytes = file.read()
        st.download_button(label="Download", data=file_bytes, file_name=output_file)

    # 删除临时文件
    os.remove("output.md")
    os.remove(output_file)
