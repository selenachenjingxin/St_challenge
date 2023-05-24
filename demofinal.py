# Import required libraries
import streamlit as st
import docx
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
import io

# Show the input text in a readable format
st.set_page_config(layout='wide')

# Title of the app
st.title('Technical Document Rewriter')


template = '''
Your role:
You have extensive experience as a technical documentation engineer, with a talent for presenting information in a clear and easy-to-understand manner. You are skilled in using tables to effectively demonstrate information, and excel at developing effective information mapping strategies.

Your task:

I will give you an example of content that have been converted into Information Mapping style. You need to apply what you have learned to convert another piece of content. Make sure that you do not leave out any information, which means all information should be found in the transformed content. Just show me the transformed content.

Example1:

Before Transformation:
<body>
    <div style="height:100px;background:#ED008C !important;text-align:left;margin:0px;"><h1 style="color: white;text-align: left;padding-top:15px;padding-left:10px;">Intranet</h1></div>
    <div style="background:#eeeeee;padding:10px 5px;">Home&nbsp;&nbsp;|&nbsp;&nbsp;Sales and Marketing&nbsp;&nbsp;|&nbsp;&nbsp;Engineering&nbsp;&nbsp;|&nbsp;&nbsp;Human Resources;&nbsp;&nbsp;|&nbsp;&nbsp;Operations&nbsp;&nbsp;|&nbsp;&nbsp;Finance and Accounting</div>
    <div id="content">
    <h1 style="color: #ED008C !important;">IT Equipment/Services Policy</h1>
    <p>1.1 A number of vendors have been approved for the purchase of IT services and equipment. Regional Managers may purchase IT services by preparing a draft Statement of Requirements, which should identify the equipment/services required, and preferred vendor from the list of approved vendors. (See item 1.3.) These vendors, and only these vendors, shall be used for all IT purchases. (For exceptions, see item 1.4 below.)</p>
    <p>1.2 The IT Manager will be involved in all IT purchases. The IT Manager’s role is to check and finalize the details of the Statement of Requirements (draft prepared by Regional Manager) and negotiate the terms and conditions with the vendor. The IT Manager will also need to sign all and any contracts.</p>
    <p>1.3 Approved vendors are Best IT Solutions (hardware and system design and development), Integrated Technology (all hardware), and AAA Corporation (for system design and development and IT audit services). Use of these approved vendors should result in a reduction in IT costs across the whole organization and, clearly, for individual regions also.</p>
    <p>1.4 Regional Managers have authority to purchase individual PCs from any vendor, following the usual purchasing process. (See also 1.3 for approved hardware vendors.)</p>
    <p>1.5 Regional Managers requiring networking hardware, software, or design must use Integrated Technology, who are the only approved vendors for these services/equipment. Contact Rose Than, Customer Services Manager at Integrated Technology. (Contacts for other approved vendors are <a onclick='stop_clock();ss();'>Jenny Marshall</a>, National Business Manager at Best IT Solutions; and Carl Niall, Account Manager at AAA Corporation.)</p>
    <p>1.6 The main aim of this purchasing policy is the simplification of contractual arrangements for IT services and equipment, which will be affected by the use of approved vendors. Results should also include an improvement to the quality of services provided to users.</p>
    <p>1.7 The contract, covering the terms and conditions agreed by the IT Manager and the vendor, is drawn up by the Contracts Manager. Approved vendors must supply the agreed equipment/services once all parties have signed the contract.</p></div>
    </body>

After Transformation:

<body id="after"><div id="content" style="margin-top: 15px;"><h1 style="color: #ED008C !important;">Policy for Purchasing IT Equipment and Services</h1><hr noshade="noshade" size="1" /><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><th width="150">Policy</th><td>It is the organization’s policy to purchase IT services and equipment from approved vendors by following a formal purchasing process.<p><strong><em>Exception</em></strong>: Regional Managers have authority to purchase individual PCs from any vendor, following the standard purchasing process. </p></td></tr></table><hr noshade="noshade" size="1" /><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><th width="150">Rationale</th><td>Purchasing IT services and equipment from approved vendors simplifies contractual arrangements, improves the quality of services provided to users, and reduces IT costs for individual regions and across the organization.</td></tr></table><hr noshade="noshade" size="1" /><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><th width="150">Approved vendors</th><td>The table below lists the approved vendors, the IT equipment and services provided to the organization, and the name of the vendor's contact person..<table width="100%" cellpadding="0" cellspacing="0" border="0" class="move"><tr><th width="33%">Vendor</th><th width="34%">Services/Equipment</th><th width="33%">Contact name</th></tr><tr><td>Best IT Solutions</td><td>All hardware, and system design and development.</td><td>Jenny Marshall, National Business Manager</td></tr><tr><td>Integrated Technology</td><td>All hardware, and networking hardware, software, and design.</td><td>Rose Than, Customer Services Manager</td></tr><tr><td>AAA Corporation</td><td>System design and development, and IT audit services.</td><td>Carl Niall, Account Manager</td></tr></table></td></tr></table><hr noshade="noshade" size="1" /><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><th width="150">Purchasing process</th><td>The table below describes the process for purchasing IT equipment or services from an approved vendor.<table width="100%" cellpadding="0" cellspacing="0" border="0" class="move"><tr><th width="10%">Stage</th><th width="40%">Who</th><th width="50%">Does what</th></tr><tr><td>1</td><td><p>Regional Manager</p></td><td><p>Drafts Statement of Requirements, identifying the equipment/services required, and preferred vendor from the list of approved vendors.</td></tr><tr><td>2</td><td><p>IT Manager</p></td><td><a onclick='stop_clock();ss();'><ul><li>Finalizes the Statement of Requirements and</li><li>Negotiates terms and conditions with the vendor.</li></ul></a></td></tr><tr><td>3</td><td><p>Contracts Manager</p></td><td><p>Prepares a contract covering the agreed terms and conditions.</p></td></tr><tr><td>4</td><td><p>Regional Manager IT Manager, and vendors</p></td><td><p>Signs the contract.</p></td></tr><tr><td>5</td><td><p>The vendor</p></td><td><p>Supplies agreed equipment/services.</p></td></tr></table></td></tr></table><hr noshade="noshade" size="1" /></body>

Content to be transformed by you:{text}

'''
llm = OpenAI(temperature=0.8,max_tokens=1500)
prompt = PromptTemplate(template=template, input_variables=["text"])
chain = LLMChain(llm=llm, prompt=prompt)

col1, col2 = st.columns([2,1])  

col1.write("""
Welcome to this technical document rewriter!🥳 
This application helps you rewrite your 
technical documents not originally written in Information Mapping/DITA into the 
required structured documents.
""")
# Text input from the user
input_text = col1.text_area("Paste your text here", height=400)
chains = []
if col2.checkbox("Grammar Check Optimization"):
    template = "As a professional technical document engineer, I would like you to optimize the following text and output the optimized content. The text is as follows: {text}"
    prompt = PromptTemplate(template=template, input_variables=["text"])
    chain = LLMChain(llm=llm, prompt=prompt)
    chains.append(chain)

if col2.checkbox("Punctuation Check"):
    template = "As a professional technical document engineer, I would like you to optimize the following text and output the optimized content. The text is as follows: {text}"
    prompt = PromptTemplate(template=template, input_variables=["text"])
    chain = LLMChain(llm=llm, prompt=prompt)
    chains.append(chain)

if col2.checkbox("Sentence Structure Optimization"):
    template = "As a professional technical document engineer, I would like you to optimize the sentence structure of the following text and output the optimized content. The text is as follows: {text}"
    prompt = PromptTemplate(template=template, input_variables=["text"])
    chain = LLMChain(llm=llm, prompt=prompt)
    chains.append(chain)

if col2.checkbox("Paragraph Structure Optimization"):
    template = "As a professional technical document engineer, I would like you to optimize the paragraph structure of the following text, simplify complex paragraphs where possible using ordered or unordered lists, and output the optimized content. The text is as follows: {text}"
    prompt = PromptTemplate(template=template, input_variables=["text"])
    chain = LLMChain(llm=llm, prompt=prompt)
    chains.append(chain)

sequential_chain = SimpleSequentialChain(chains=chains)

# Create two columns for the input and output
col1, col2 = st.columns(2)



# Adding a horizontal line
st.markdown('---')

if input_text:
    # Show the input text in a readable format in the left column
    col1.markdown("**Original Content**")
    col1.markdown(input_text, unsafe_allow_html=True)
    response = chain.run(input_text)

    # Show the output text in a readable format in the right column
  
    col2.markdown(response, unsafe_allow_html=True)
