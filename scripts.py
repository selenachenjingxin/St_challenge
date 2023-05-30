"""
if st.sidebar.checkbox("拼写检查优化"):
    template = "你是一位专业的技术文档工程师，现在我希望你对以下文本修正错别字和不正确的用词并输出修正后的内容。文本如下：{text}"
    prompt = PromptTemplate(template=template, input_variables=["text"])
    chain = LLMChain(llm=llm, prompt=prompt)
    chains.append(chain)

if st.sidebar.checkbox("语法检查优化"):
    template = "你是一位专业的技术文档工程师，现在我希望你对以下文本进行语法检查，修正不正确的语法，并输出优化后的内容。文本如下：{text}"
    prompt = PromptTemplate(template=template, input_variables=["text"])
    chain = LLMChain(llm=llm, prompt=prompt)
    chains.append(chain)

if st.sidebar.checkbox("标点符号检查"):
    template = "你是一位专业的技术文档工程师，现在我希望你对以下文本进行标点符号检查，修改使用不恰当的标点符号，并输出优化后的内容。文本如下：{text}"
    prompt = PromptTemplate(template=template, input_variables=["text"])
    chain = LLMChain(llm=llm, prompt=prompt)
    chains.append(chain)

if st.sidebar.checkbox("句子结构优化"):
    template = "你是一位专业的技术文档工程师，现在我希望你对以下文本进行句子结构优化，若有长难句，简化长难句并输出优化后的内容。文本如下：{text}"
    prompt = PromptTemplate(template=template, input_variables=["text"])
    chain = LLMChain(llm=llm, prompt=prompt)
    chains.append(chain)

if st.sidebar.checkbox("段落结构优化"):
    template = "你是一位专业的技术文档工程师，现在我希望你对以下文本进行段落结构优化，将复杂的段落，在可能的情况下使用有序列表或者无序列表等，并输出优化后的内容。文本如下：{text}"
    prompt = PromptTemplate(template=template, input_variables=["text"])
    chain = LLMChain(llm=llm, prompt=prompt)
    chains.append(chain)
"""