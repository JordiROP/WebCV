import {Card, CardHeader, CardBody} from "@heroui/react";
import {education} from "@/app/constants/education"

type EduCardDef = {
    title: string,
    body: EduCardBodyDef[]
}
type EduCardBodyDef = {
    subtitle: string;
    date: string | null;
    text: string;
    credential: string | null;
  };

const EduCard: React.FC<EduCardDef> = ({title, body}) => (
    <Card className="w-full">
        <CardHeader>  
            <h3 className="font-bold text-3xl">{title}</h3>
        </CardHeader>
        <hr className="card-divider"></hr>
        {body.map((item, index) => (
          <EduCardBody key={index} subtitle={item.subtitle} date={item.date} text={item.text} credential={item.credential}/>
        ))}
    </Card>
);

const EduCardBody: React.FC<EduCardBodyDef> = ({subtitle, date, text, credential}) => (
    <CardBody>
        <h4 className="font-bold text-2xl">{subtitle}</h4>
        <br></br>
        {date && <p>{date}</p>}
        {date && <br></br>}
        <p>{text}</p>
        {credential && <br></br>}
        {credential && <p><a href={credential} className="text-blue-500 hover:text-blue-800 hover:underline">Certificate</a></p>}
    </CardBody>
);

export default function EduCardList() {
    return (
      <div className="flex flex-wrap gap-4 pt-4 pb-4">
        {education.map((item, index) => (
          <EduCard key={index} title={item.title} body={item.body} />
        ))}
      </div>
    );
  }




