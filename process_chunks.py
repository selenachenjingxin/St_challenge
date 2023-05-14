  # 处理段落
        response2 = sequential_chain.run(para.text)
        st.write(response2)

        # 将处理后的段落添加到新文档中
        new_document.add_paragraph(response2)

    # 添加一个按钮来下载新文档
    download_button = st.button("下载新文档")

    # 如果用户点击了下载按钮，则将新文档保存到本地并提供下载链接
    if download_button:
        output_filename = "processed_document.docx"
        new_document.save(output_filename)
        with open(output_filename, "rb") as f:
            bytes_data = f.read()
            st.download_button(
                label="下载新文档",
                data=bytes_data,
                file_name=output_filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )