HEADER_ACADEMIC_XP = "Associated Professor - University of Lleida (2021 - actual)"


SUBHEADER_SCP = "Informatics Degree: Concurrent and Parallel Systems (2021)"
TEXT_SCP = """This course aims to provide a comprehensive understanding of concurrent programming. 
    It covers the significance of concurrency in real-world applications, the distinct characteristics of concurrent 
    systems, and the unique challenges posed by concurrent programming compared to sequential programming. 
    The course delves into synchronization, mutual exclusion, and security properties, while exploring communication 
    and synchronization mechanisms for both shared memory and distributed systems. Students will gain practical 
    experience in developing concurrent applications using techniques like semaphores and monitors, 
    and applying software engineering methodologies to this domain."""
TECNOLOGIES_SCP = ["c.png", "java.png"]

SUBHEADER_PROGCOMIII = "Electronics Degree: Programming and Communications III"
TEXT_PROGCOMIII = """This course focuses on programming basic communication applications using Python as well as the basics
    of databases. Students will learn about internet, protocols and different libraries to develop an application 
    capable of sharing data over the network using sockets and building their own api. Moreover, students will learn
    about the usage of SQL Databases to store and provide data as requested."""
TECNOLOGIES_PROGCOMIII = ["python.png", "postgresql.png", "fastapi.png"]

SUBHEADER_HPC = "Informatics Master’s Degree: High Performance Computing"
TEXT_HPC = """This course focuses on High-Performance Computing (HPC). Students will analyze HPC system performance, 
    understand parallel programming models, and learn about HPC architectures. 
    Practical skills in implementing and debugging parallel applications using OpenMP, MPI, and CUDA will be developed. 
    Hybrid algorithms combining OpenMP-MPI and OpenMP-CUDA will be designed and evaluated for complex problem-solving. 
    Effective communication of technical concepts in written and spoken English is emphasized.
    The overall goal is to train professionals capable of designing, implementing, and optimizing HPC applications."""
TECNOLOGIES_HPC = ["c.png", "nvidia.png", "OpenMP.png", "mpi.gif"]


SUBHEADER_FZTH = "Summer Course: Python From Zero to Hero"
TEXT_FZTH = ["""The aim of the course is to develop and acquire the necessary knowledge to learn and understand the 
    Python programming language. It will provide the tools and knowledge necessary to enter the world of programming 
    with this language and to be able to use it in the real world, both amateur and professional.""",
             """The fundamental contents of the course will be familiarization with the Google Colab environment; 
    types of variables and data structures; operators, conditionals and loops; object-oriented language; 
    error management; file I/O, and advanced functions (analytics libraries).""",
             """Course intended for all people interested in the world of computing and programming. No previous 
    experience in this language is necessary, as it will start with the first notions."""]
TECNOLOGIES_FZTH = ["python.png", "colab.png"]

FIELDS = [
    {"subheader": SUBHEADER_SCP, "text": TEXT_SCP, "technologies": TECNOLOGIES_SCP},
    {"subheader": SUBHEADER_PROGCOMIII, "text": TEXT_PROGCOMIII, "technologies": TECNOLOGIES_PROGCOMIII},
    {"subheader": SUBHEADER_HPC, "text": TEXT_HPC, "technologies": TECNOLOGIES_HPC},
    {"subheader": SUBHEADER_FZTH, "text": TEXT_FZTH, "technologies": TECNOLOGIES_FZTH}
]
