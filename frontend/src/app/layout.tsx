import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import Link from "next/link";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Foresight — Forward-Looking News Analysis",
  description:
    "Scenario-based analysis of global events in politics, tech, and economy.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-gray-50 text-gray-900">
        <header className="sticky top-0 z-10 border-b border-gray-200 bg-white/80 backdrop-blur">
          <div className="mx-auto flex max-w-4xl items-center justify-between px-4 py-3">
            <Link href="/" className="text-lg font-bold tracking-tight">
              Foresight
            </Link>
            <nav className="flex gap-4 text-sm text-gray-500">
              <Link href="/" className="hover:text-gray-900 transition-colors">
                Feed
              </Link>
            </nav>
          </div>
        </header>
        <main className="mx-auto w-full max-w-4xl flex-1 px-4 py-8">
          {children}
        </main>
        <footer className="border-t border-gray-200 py-4 text-center text-xs text-gray-400">
          Foresight — scenario-based news analysis
        </footer>
      </body>
    </html>
  );
}
