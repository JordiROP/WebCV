"use client"
import { Tabs, TabsList, TabsTrigger, TabsContent } from '@radix-ui/react-tabs';
import AboutMe from "@/app/components/About";
import ProfExpCardList from '@/app/components/ProfExperience';
import EduCardList from '@/app/components/Education';
import AcadExpCardList from '@/app/components/AcadExperience';
import Activities from '@/app/components/Activities';
import '@/app/globals.css';
import { useState } from 'react';



export default function MyTabs() {
  const [selectedTab, setSelectedTab] = useState('aboutMe');
  return (
    <Tabs defaultValue="aboutMe" className="max-w-[69.25rem]" onValueChange={setSelectedTab}>
      <TabsList className="flex max-w-[69.25rem]">
        <TabsTrigger value="aboutMe" className={`mr-5 ${selectedTab === 'aboutMe' ? 'border-b-2 border-blue-500 text-blue-600':'text-gray-600 hover:text-blue-500'}`} > About Me</TabsTrigger>
        <TabsTrigger value="profExperience" className={`mr-5 ${selectedTab === 'profExperience' ? 'border-b-2 border-blue-500 text-blue-600':'text-gray-600 hover:text-blue-500'}`}>Professional Experience</TabsTrigger>
        <TabsTrigger value="acadExperience" className={`mr-5 ${selectedTab === 'acadExperience' ? 'border-b-2 border-blue-500 text-blue-600':'text-gray-600 hover:text-blue-500'}`}>Academic Experience</TabsTrigger>
        <TabsTrigger value="education" className={`mr-5 ${selectedTab === 'education' ? 'border-b-2 border-blue-500 text-blue-600':'text-gray-600 hover:text-blue-500'}`}>Education</TabsTrigger>
        <TabsTrigger value="additional" className={`${selectedTab === 'additional' ? 'border-b-2 border-blue-500 text-blue-600':'text-gray-600 hover:text-blue-500'}`}>Additional Activities</TabsTrigger>
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
