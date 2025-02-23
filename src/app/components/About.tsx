import {Card, CardHeader, CardBody} from "@heroui/react";


export default function Header() {
  return (
    <Card className="w-full">
      <CardHeader>  
          <h3 className="font-bold text-3xl">Get To Know Me a Bit</h3>
      </CardHeader>
      <hr className="card-divider"></hr>
      <CardBody>
        <p>Hello and welcome to my website! I&apos;m a Software and Data engineer graduated with a Master&apos;s degree in Computer Engineering with a major in Big Data at UdL, 
          currently working in Bluetab, an IBM Company as a developer, providing assistance in the productivization of GenAI applications. 
          In addition, I currently impart the subjects of Programming and Communications III to Electronics Degree students, teaching fundamentals about networking, 
          databases and APIs with Python; High Performance Computing, teaching fundamentals about distributed computing with OpenMP, MPI and CUDA.</p>
        <br></br>
        <p>Hello and welcome to my website! I&apos;m a Software and Data engineer graduated with a Master&apos;s degree in Computer Engineering with a major in Big Data at UdL, 
          currently working in Bluetab, an IBM Company as a developer, providing assistance in the productivization of GenAI applications. In addition, I currently impart 
          the subjects of Programming and Communications III to Electronics Degree students, teaching fundamentals about networking, databases and APIs with Python; 
          High Performance Computing, teaching fundamentals about distributed computing with OpenMP, MPI and CUDA.</p>
        <br></br>
        <p>Although I spend most of the time working, I like to use my free time to enjoy myself playing video-games, going to the Gym, and dance Salsa.</p>
      </CardBody>
    </Card>
  );
}