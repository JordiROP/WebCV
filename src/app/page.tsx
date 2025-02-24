import Tabs from "@/app/components/Tabs"
import { Readex_Pro } from 'next/font/google';
import clsx from 'clsx';
const readexPro = Readex_Pro({ subsets: ['latin'] });
export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className={clsx("flex flex-col gap-8 row-start-2 items-center sm:items-start", readexPro.className)}>
        <Tabs />
      </main>
      <footer className="row-start-3 gap-6 flex-wrap items-center justify-center">
        <p className="text-center">Built with <a href="https://nextjs.org/" className="text-blue-500 hover:text-blue-800 hover:underline">Next.js</a> by Vercel 💻</p>
        <p>Made with ❤️ by Jordi R. Onrubia Palacios</p>
      </footer>
    </div>
  );
}
