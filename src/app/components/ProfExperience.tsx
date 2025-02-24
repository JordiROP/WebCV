import {Card, CardHeader, CardBody} from "@heroui/react";
import {profExperience} from "@/app/constants/prof_experience"

type ProfExpCardDef = {
    title: string;
    date: string;
    text: string;
  };

const ProfExpCard: React.FC<ProfExpCardDef> = ({title, date, text}) => (
    <Card className="w-full">
        <CardHeader>  
            <h3 className="font-bold text-3xl">{title}</h3>
        </CardHeader>
        <hr className="card-divider"></hr>
        <CardBody>
            <p>{date}</p>
            <br></br>
            <p>{text}</p>
        </CardBody>
    </Card>
);

export default function ProfExpCardList() {
    return (
      <div className="flex flex-wrap gap-4 pb-4">
        {profExperience.map((item, index) => (
          <ProfExpCard key={index} title={item.title} date={item.date} text={item.text} />
        ))}
      </div>
    );
  }




