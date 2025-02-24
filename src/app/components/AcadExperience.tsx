import {Card, CardHeader, CardBody} from "@heroui/react";
import {acadExperience} from "@/app/constants/acad_experience";
import Image from "next/image";

type AcadExpCardDef = {
    title: string,
    cards: AcadExpCardBodyDef[]
}

type AcadExpCardBodyDef = {
    title: string
    body: string
    techs: string[]
}

const AcadExpCard: React.FC<AcadExpCardDef> = ({title, cards}) => (
    <Card className="w-full">
        <CardHeader>  
            <h3 className="font-bold text-4xl">{title}</h3>
        </CardHeader>
        <hr className="card-divider"></hr>
        <div className="pt-4">
            {cards.map((item, index) => (
            <AcadExpCardBody key={index} title={item.title} body={item.body} techs={item.techs}/>
            ))}
        </div>
    </Card>
);

const AcadExpCardBody: React.FC<AcadExpCardBodyDef> = ({title, body, techs}) => (
    <Card className="w-[97%] mx-auto mt-4 mb-6">
        <CardHeader>  
            <h4 className="font-bold text-3xl">{title}</h4>
        </CardHeader>
        <CardBody>
            <p>{body}</p>
            <div className="flex items-center">
                {techs.map((img, index) => (
                <div key={index}>
                    <Image
                        src={`/images/${img}`}
                        alt={`${img} logo`}
                        width={110} // Set width
                        height={110} // Set height
                        className="pl-5 pb-5 pt-7"
                    />
                </div>
                ))}
            </div>
        </CardBody>
    </Card>
);

export default function AcadExpCardList() {
    return (
      <div className="flex flex-wrap gap-4 pb-4">
        {acadExperience.map((item, index) => (
          <AcadExpCard key={index} title={item.title} cards={item.cards} />
        ))}
      </div>
    );
  }