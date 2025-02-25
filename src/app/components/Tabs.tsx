import { Tabs, TabsList, TabsTrigger, TabsContent } from '@radix-ui/react-tabs';
import AboutMe from "@/app/components/About";
import ProfExpCardList from '@/app/components/ProfExperience';
import EduCardList from '@/app/components/Education';
import AcadExpCardList from '@/app/components/AcadExperience';
import Activities from '@/app/components/Activities';
import '@/app/globals.css';
export default function MyTabs() {
  return (
    <Tabs defaultValue="aboutMe" className="max-w-[69.25rem]">
      <TabsList className="max-w-[69.25rem]">
        <TabsTrigger value="aboutMe" className='pr-5'> About Me</TabsTrigger>
        <TabsTrigger value="profExperience" className='pr-5'>Professional Experience</TabsTrigger>
        <TabsTrigger value="acadExperience" className='pr-5'>Academic Experience</TabsTrigger>
        <TabsTrigger value="education" className='pr-5'>Education</TabsTrigger>
        <TabsTrigger value="additional">Additional Activities</TabsTrigger>
      </TabsList>
      <hr className="tab-divider mt-4 mb-5"></hr>   
    <TabsContent value="aboutMe">
        <AboutMe />  
    </TabsContent>
    <TabsContent value="profExperience">
        <ProfExpCardList />  
    </TabsContent>
    <TabsContent value="acadExperience">
        <AcadExpCardList />  
    </TabsContent>
    <TabsContent value="education">
        <EduCardList />
    </TabsContent>
    <TabsContent value="additional">
      <Activities />
    </TabsContent>
    </Tabs>
  );
}
