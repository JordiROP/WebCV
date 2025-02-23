import { Tabs, TabsList, TabsTrigger, TabsContent } from '@radix-ui/react-tabs';
import Header from "@/app/components/About";
import ProfExpCardList from '@/app/components/ProfExperience';
import EduCardList from '@/app/components/Education';
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
        <Header />  
    </TabsContent>
    <TabsContent value="profExperience">
        <ProfExpCardList />  
    </TabsContent>
    <TabsContent value="acadExperience">
        <p>This is the Settings tab content.</p>
    </TabsContent>
    <TabsContent value="education">
        <EduCardList />
    </TabsContent>
    <TabsContent value="additional">
        <p>This is the Settings tab content.</p>
    </TabsContent>
    </Tabs>
  );
}
