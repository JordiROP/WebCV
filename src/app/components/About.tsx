import {Card, CardHeader, CardBody} from "@heroui/react";
import {about} from "@/app/constants/about"

export default function AboutMe() {
  return (
    <Card className="w-full">
      <CardHeader>  
          <h3 className="font-bold text-3xl">{about.title}</h3>
      </CardHeader>
      <hr className="card-divider"></hr>
      <div className="flex flex-wrap gap-4 pb-4">
        <CardBody>
          <p>{about.upText}</p>
          <br></br>
          <p>{about.midText}</p>
          <br></br>
          <p>{about.botText}</p>
        </CardBody>
        </div>
    </Card>
  );
}