import '@fortawesome/fontawesome-free/css/all.min.css';
import {Card} from "@heroui/react";
import Image from "next/image";
import {header} from "@/app/constants/header";

const profile_image: string = "profile-pic.png"

export default function Header() {
  return (
    <div className="w-full flex flex-wrap gap-4 pb-4">
      <Card className="w-full">
        <div className="flex">
            <div className="w-1/4 rounded">
                <Image
                    src={`/images/${profile_image}`}
                    alt={`profile image`}
                    width={268} // Set width
                    height={110} // Set height
                    className="max-w-full h-auto profile-image-radius"
                />
            </div>
            <div className="w-3/4 flex items-center">
                <div className="w-full text-center">
                    <h1 className='font-bold text-5xl'>{header.name}</h1>
                    <br></br>
                    <p>{header.subtext}</p>
                    <br></br>
                    <div>
                        <a href={header.resume.path} download={header.resume.name}>
                            <button className="border py-2 px-4 rounded-md hover:bg-blue-300">{header.resume.text}</button>
                        </a>        
                    </div>
                    <br></br>
                    {header.social.map((item, index) => (
                        <a key={index} href={item.link}><i className={item.icon}></i></a>
                    ))}
                </div>
          </div>
        </div>
      </Card>
    </div>
  );
}