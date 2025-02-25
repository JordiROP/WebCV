import {Card, CardHeader, CardBody} from "@heroui/react";
import {activities} from "@/app/constants/activities";

type ActivitiesCardDef = {
    title: string,
    subtitle: string|null,
    text: string|null,
    points: string[]
}

const AcadExpCard: React.FC<ActivitiesCardDef> = ({title, subtitle, text, points}) => (
    <Card className="w-full">
        <CardHeader>  
            <h3 className="font-bold text-3xl">{title}</h3>
        </CardHeader>
        <hr className="card-divider"></hr>
        <CardBody>
            {subtitle && <h3 className="font-bold text-3xl">{subtitle}</h3>}
            {subtitle && <br></br>}
            {text && <p>{text}</p>}
            {text && <br></br>}
            <div className="pt-4">
                <ul className="list-disc pl-12">
                    {points.map((point, index) => (
                        <li className="pb-5" key={index}>{point}</li>
                    ))}
                </ul>
            </div>
        </CardBody>
    </Card>
);

export default function AcadExpCardList() {
    return (
      <div className="flex flex-wrap gap-4 pb-4">
        {activities.map((item, index) => (
          <AcadExpCard key={index} title={item.title} subtitle={item.subtitle} text={item.text} points={item.points} />
        ))}
      </div>
    );
  }