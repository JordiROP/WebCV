HEADER_UNI = "University"
SUBHEADER_MASTER = "Masters Degree, Computer Engineering, major in Big Data"
DATE_MASTER = "2019-2021"
TEXT_MASTER = """The Master in Computer Engineering has brought me a totally practical way to the most innovative 
methodologies and technologies in the different areas of computer science, at the same time that has prepared me to 
integrate into large computer projects as well as direct, coordinate and plan them."""

SUBHEADER_DEGREE = "Computer Engineering Degree, major in computation"
DATE_DEGREE = "2014-2018"
TEXT_DEGREE = """The degree of Computer Engineering, has brought me the knowledge and skills necessary to devise, 
design, develop, maintain and manage computer systems for problems ranging from information management in the business 
context, through problems of control and management of industrial processes and devices, to problems of management of 
computer services and infrastructure, communication and information storage. Furthermore, the minor in computation has
provided a better understanding in the different fields of Artificial Intelligence"""

UNI_DATA = [
    {"subheader": SUBHEADER_MASTER, "date": DATE_MASTER, "text": TEXT_MASTER},
    {"subheader": SUBHEADER_DEGREE, "date": DATE_DEGREE, "text": TEXT_DEGREE},
]


HEADER_CFGS = "Certificate of Higher Education (HNC)"
SUBHEADER_DAM = "Multi Platform Application Development"
DATE_DAM = "2012-2014"
TEXT_DAM = """The general competence of this course is to develop, implement, document and maintain cross-platform 
computer applications, using specific technologies and development environments, guaranteeing access to data in a 
secure manner and meeting the criteria of use and quality required by the established standards."""


HEADER_OTHER = "Courses and Certifications"
COURSES = [
    {"subheader": "Spark and Scala at Databricks: Big Data and data engineering",
     "text": """The objective of this course is to learn how to work with the main Spark abstractions, 
     which are RDDs and DataFrames. Know the operation and structure of Apache Spark; Work with Spark RDDs from basic 
     to advanced levels; Work with DataFrames in Spark using the SQL API from basic to advanced levels; 
     Optimize your Apache Spark applications for handling large volumes of data through DataFrames""",
     "credential": "https://www.udemy.com/certificate/UC-2dd12796-fb6f-4229-80a8-ae14ff6951bc/"},
    {"subheader": "DeepLearning.AI TensorFlow Developer",
     "text": """This course covers key areas for developing proficiency in TensorFlow. For computer vision, 
     it emphasizes handling real-world image data and preventing overfitting through techniques like augmentation and 
     dropout. For natural language processing, building models using RNNs, GRUs, and LSTMs while training on text 
     repositories is highlighted.""",
     "credential": "https://www.coursera.org/account/accomplishments/professional-cert/ZBS5XKZN5WTA"},
    {"subheader": "DeepLearning.AI Deep Learning Specialization",
     "text": """This course covers the core concepts of deep learning, equipping learners to construct 
     and optimize neural networks. A strong emphasis is placed on practical applications, with in-depth exploration of 
     computer vision techniques, including object detection, recognition, and artistic style transfer through 
     Convolutional Neural Networks (CNNs). Additionally, the curriculum covers Natural Language Processing (NLP) tasks 
     such as Named Entity Recognition and Question Answering, employing Recurrent Neural Networks (RNNs), 
     word embeddings, and advanced transformer models facilitated by platforms like Hugging Face.""",
     "credential": "https://www.coursera.org/account/accomplishments/specialization/certificate/VE8M8GV6TLWK"}
]