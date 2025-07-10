### **Project Structure**

First, create the following directory structure for your project:

```
mcss-docs/
├── app/
│   ├── components/
│   │   ├── button/
│   │   │   └── page.tsx
│   │   └── page.tsx
│   ├── core-concepts/
│   │   ├── component-isolation/
│   │   │   └── page.tsx
│   │   ├── five-layers/
│   │   │   └── page.tsx
│   │   ├── onc-model/
│   │   │   └── page.tsx
│   │   └── page.tsx
│   ├── annotations/
│   │   └── page.tsx
│   ├── design-tokens/
│   │   └── page.tsx
│   ├── getting-started/
│   │   └── page.tsx
│   ├── philosophy/
│   │   └── page.tsx
│   ├── layout.tsx
│   ├── globals.css
│   └── page.tsx
├── components/
│   └── Sidebar.tsx
├── public/
├── package.json
├── next.config.mjs
└── tsconfig.json
```

---

### **File Contents**

Now, populate each file with the following code.

#### **`package.json`**

This file defines your project's dependencies and scripts.

JSON

```
{
  "name": "mcss-docs",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "react": "^18",
    "react-dom": "^18",
    "next": "14.2.3"
  },
  "devDependencies": {
    "typescript": "^5",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "eslint": "^8",
    "eslint-config-next": "14.2.3"
  }
}
```

#### **`next.config.mjs`**

The configuration file for Next.js.

JavaScript

```
/** @type {import('next').NextConfig} */
const nextConfig = {};

export default nextConfig;
```

#### **`tsconfig.json`**

The configuration file for TypeScript.

JSON

```
{
  "compilerOptions": {
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

#### **`app/globals.css`**

This file simulates the MCSS engine by styling elements based on their `mcss-*` data attributes.

CSS

```
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --foreground-rgb: 0, 0, 0;
  --background-start-rgb: 214, 219, 220;
  --background-end-rgb: 255, 255, 255;
  --mcss-color-blue-100: #DBEAFE;
  --mcss-color-blue-300: #93C5FD;
  --mcss-color-blue-500: #3B82F6;
  --mcss-color-blue-600: #2563EB;
  --mcss-color-blue-800: #1E40AF;
  --mcss-color-red-500: #EF4444;
  --mcss-color-gray-100: #F3F4F6;
  --mcss-color-gray-700: #374151;
  --mcss-color-slate-100: #f1f5f9;
  --mcss-color-slate-300: #cbd5e1;
  --mcss-color-slate-500: #64748b;
  --mcss-color-slate-800: #1e293b;
  --mcss-color-white: #FFFFFF;
  --mcss-color-interactive-primary: var(--mcss-color-blue-500);
  --mcss-color-interactive-secondary-bg: #E5E7EB;
  --mcss-color-interactive-secondary-text: #1F2937;
  --mcss-color-destructive: var(--mcss-color-red-500);
}

body {
  color: rgb(var(--foreground-rgb));
  background: linear-gradient(
      to bottom,
      transparent,
      rgb(var(--background-end-rgb))
    )
    rgb(var(--background-start-rgb));
}

/* Simulated MCSS Engine */

/* Display */
[mcss-d="flex"] { display: flex; }
[mcss-d="grid"] { display: grid; }
[mcss-d="block"] { display: block; }

/* Sizing */
[mcss-w="1/2"] { width: 50%; }
[mcss-h="screen"] { height: 100vh; }
[mcss-max-w="lg"] { max-width: 32rem; }

/* Spacing */
[mcss-p="4"] { padding: 1rem; }
[mcss-pt="2"] { padding-top: 0.5rem; }
[mcss-pl="3"] { padding-left: 0.75rem; }
[mcss-pb="2"] { padding-bottom: 0.5rem; }
[mcss-pr="3"] { padding-right: 0.75rem; }
[mcss-p~="x:4"] { padding-left: 1rem; padding-right: 1rem; }
[mcss-p~="y:2"] { padding-top: 0.5rem; padding-bottom: 0.5rem; }
[mcss-m="4"] { margin: 1rem; }
[mcss-mt="2"] { margin-top: 0.5rem; }
[mcss-ml="2"] { margin-left: 0.5rem; }
[mcss-mb="2"] { margin-bottom: 0.5rem; }

/* Typography */
[mcss-font~="bold"] { font-weight: 700; }
[mcss-text~="lg"] { font-size: 1.125rem; }
[mcss-text~="base"] { font-size: 1rem; }
[mcss-text~="blue-800"] { color: var(--mcss-color-blue-800); }
[mcss-text~="white"] { color: var(--mcss-color-white); }
[mcss-align="center"] { text-align: center; }

/* Backgrounds */
[mcss-bg="blue-100"] { background-color: var(--mcss-color-blue-100); }
[mcss-bg="interactive-primary"] { background-color: var(--mcss-color-interactive-primary); }
[mcss-bg="interactive-secondary"] { background-color: var(--mcss-color-interactive-secondary-bg); color: var(--mcss-color-interactive-secondary-text); }
[mcss-bg="destructive"] { background-color: var(--mcss-color-destructive); }

/* Borders */
[mcss-border~="1"] { border-width: 1px; border-style: solid; }
[mcss-border~="blue-300"] { border-color: var(--mcss-color-blue-300); }
[mcss-rounded="md"] { border-radius: 0.375rem; }
[mcss-rounded="lg"] { border-radius: 0.5rem; }

/* Flexbox */
[mcss-justify="center"] { justify-content: center; }
[mcss-items="center"] { align-items: center; }

/* Component Specific Styles */
[mcss-c="button"]:hover {
  opacity: 0.9;
}
[mcss-c="button"]:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* General Styles for Docs */
main {
  padding: 2rem;
  line-height: 1.6;
}
h1 {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
  border-bottom: 1px solid #ddd;
  padding-bottom: 0.5rem;
}
h2 {
  font-size: 2rem;
  font-weight: bold;
  margin-top: 2.5rem;
  margin-bottom: 1rem;
}
h3 {
  font-size: 1.5rem;
  font-weight: bold;
  margin-top: 2rem;
  margin-bottom: 1rem;
}
p {
  margin-bottom: 1rem;
}
code {
  background-color: #f4f4f4;
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
  font-family: monospace;
}
pre {
  background-color: #2d2d2d;
  color: #f8f8f2;
  padding: 1rem;
  border-radius: 8px;
  overflow-x: auto;
  margin-bottom: 1rem;
}
pre code {
  background-color: transparent;
  padding: 0;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1rem;
}
th, td {
  border: 1px solid #ddd;
  padding: 0.75rem;
  text-align: left;
}
th {
  background-color: #f9f9f9;
  font-weight: bold;
}
a {
  color: #0070f3;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
```

#### **`app/layout.tsx`**

This is the root layout for the entire application. It includes the sidebar navigation.

TypeScript

```
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Sidebar from "@/components/Sidebar";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "MCSS Official Documentation",
  description: "Build Isolated, Scalable UIs with Semantic HTML",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div style={{ display: 'flex' }}>
          <Sidebar />
          <main style={{ flexGrow: 1, padding: '2rem' }}>
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
```

#### **`components/Sidebar.tsx`**

The navigation sidebar component.

TypeScript

```
import Link from 'next/link';

const Sidebar = () => {
  return (
    <aside style={{
      width: '280px',
      flexShrink: 0,
      backgroundColor: '#f7fafc',
      borderRight: '1px solid #e2e8f0',
      height: '100vh',
      padding: '1.5rem',
      position: 'sticky',
      top: 0,
      overflowY: 'auto'
    }}>
      <h2 style={{ fontSize: '1.25rem', fontWeight: 'bold', marginBottom: '1rem' }}>
        <Link href="/">MCSS Docs</Link>
      </h2>
      <nav>
        <ul>
          <li style={{ marginBottom: '0.75rem' }}>
            <Link href="/getting-started" style={{ fontWeight: 'bold' }}>Getting Started</Link>
          </li>
          <li style={{ marginBottom: '0.75rem' }}>
            <Link href="/philosophy" style={{ fontWeight: 'bold' }}>Philosophy</Link>
          </li>
          
          <li style={{ marginBottom: '1.5rem' }}>
            <h3 style={{ fontWeight: 'bold', marginTop: '1rem', marginBottom: '0.5rem' }}>Core Concepts</h3>
            <ul style={{ paddingLeft: '1rem' }}>
              <li style={{ marginBottom: '0.5rem' }}><Link href="/core-concepts/five-layers">The Five Layers</Link></li>
              <li style={{ marginBottom: '0.5rem' }}><Link href="/core-concepts/onc-model">ONC Model</Link></li>
              <li><Link href="/core-concepts/component-isolation">Component Isolation</Link></li>
            </ul>
          </li>

          <li style={{ marginBottom: '0.75rem' }}>
            <Link href="/annotations" style={{ fontWeight: 'bold' }}>Annotation System</Link>
          </li>
          <li style={{ marginBottom: '0.75rem' }}>
            <Link href="/design-tokens" style={{ fontWeight: 'bold' }}>Design Tokens</Link>
          </li>
          <li style={{ marginBottom: '0.75rem' }}>
            <Link href="/components" style={{ fontWeight: 'bold' }}>Component Library</Link>
             <ul style={{ paddingLeft: '1rem', marginTop: '0.5rem' }}>
                <li><Link href="/components/button">Button</Link></li>
             </ul>
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
```

#### **`app/page.tsx`** (Home Page)

TypeScript

```
import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <h1>Build Isolated, Scalable UIs with Semantic HTML</h1>
      <p>MCSS is a component-based CSS architecture that uses HTML attributes to create truly encapsulated styles, turning your markup into a self-documenting API.</p>

      <h2>What is MCSS?</h2>
      <p>MCSS (Modular Component-based Style System) is a CSS framework designed to solve the challenges of building and maintaining large-scale user interfaces. It addresses common pain points like global namespace pollution, specificity conflicts, and style leakage by providing a novel architecture for true component isolation. By moving the styling API from CSS classes to semantic <code>mcss-*</code> HTML attributes, MCSS enables developers to write clean, predictable, and highly reusable UI components directly in their markup.</p>
      
      <pre><code>
{`<div mcss-c="alert" 
     mcss-p="4" 
     mcss-bg="blue-100" 
     mcss-border="1;blue-300" 
     mcss-rounded="md">
  <strong mcss-n="title" mcss-font="bold">Info:</strong>
  <span mcss-n="message" mcss-ml="2">This is an informational alert.</span>
</div>`}
      </code></pre>

      <h2>Core Features</h2>
      <table>
        <thead>
          <tr>
            <th>Feature</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Attribute-Driven API</strong></td>
            <td>Style components directly in your HTML with a declarative and semantic annotation system. This approach separates styling concerns from structural classes and behavioral hooks, leading to cleaner, more readable markup.</td>
          </tr>
          <tr>
            <td><strong>True Component Isolation</strong></td>
            <td>Achieve genuine style encapsulation. MCSS components are self-contained and immune to global style conflicts, ensuring predictable rendering every time, similar to the benefits of Shadow DOM but without its complexities.</td>
          </tr>
          <tr>
            <td><strong>Integrated Design System</strong></td>
            <td>Leverage a built-in system of design tokens for color, spacing, typography, and more. This ensures visual consistency across your entire application and makes theming straightforward and maintainable.</td>
          </tr>
        </tbody>
      </table>
      
      <Link href="/getting-started" style={{
        display: 'inline-block',
        marginTop: '1rem',
        padding: '0.75rem 1.5rem',
        backgroundColor: 'var(--mcss-color-blue-500)',
        color: 'white',
        borderRadius: '0.375rem',
        fontWeight: 'bold'
      }}>
        Get Started
      </Link>
    </div>
  );
}
```

#### **`app/getting-started/page.tsx`**

TypeScript

```
import Link from 'next/link';

export default function GettingStarted() {
  return (
    <div>
      <h1>Getting Started with MCSS</h1>
      <p>This guide provides a step-by-step tutorial to install MCSS, set up a basic project, and build your first fully-styled, isolated component. By the end, you will have a functional and responsive "Callout" card, and a foundational understanding of how to work with MCSS.</p>

      <h3>Step 1: Installation</h3>
      <p>First, create a new directory for your project and initialize it. Then, install the MCSS framework package.</p>
      <pre><code>
{`# Create and navigate into your new project directory
mkdir mcss-project
cd mcss-project

# Install MCSS using npm
npm install @mcss/framework

# Or, if you prefer yarn
yarn add @mcss/framework`}
      </code></pre>

      <h3>Step 2: Project Setup</h3>
      <p>Next, create an <code>index.html</code> file and link to the MCSS stylesheet.</p>
      <pre><code>
{`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My First MCSS Page</title>
  <link rel="stylesheet" href="./node_modules/@mcss/framework/dist/mcss.css">
</head>
<body>
  </body>
</html>`}
      </code></pre>

      <h3>Step 3: Build the "Hello, MCSS" Component</h3>
      <p>Now it's time to build your first component. We will create a simple <code>Callout</code> card. Add the following HTML inside the <code>&lt;body&gt;</code> tag.</p>
      
      <h4>Component Preview:</h4>
      <div mcss-c="callout" mcss-p="4" mcss-bg="blue-100" mcss-border="1;blue-300" mcss-rounded="md" style={{maxWidth: '500px', marginTop: '1rem'}}>
        <h3 mcss-n="title" mcss-font="bold" mcss-text="lg;blue-800">
          Hello, MCSS!
        </h3>
        <p mcss-n="body" mcss-mt="2" style={{margin: 0, marginTop: '0.5rem'}}>
          This is my first component styled with the MCSS annotation system.
        </p>
      </div>

      <h4>Code:</h4>
      <pre><code>
{`<div mcss-c="callout" 
     mcss-p="4" 
     mcss-bg="blue-100" 
     mcss-border="1;blue-300" 
     mcss-rounded="md">
  
  <h3 mcss-n="title" mcss-font="bold" mcss-text="lg;blue-800">
    Hello, MCSS!
  </h3>
  
  <p mcss-n="body" mcss-mt="2">
    This is my first component styled with the MCSS annotation system.
  </p>
  
</div>`}
      </code></pre>

      <h3>Step 4: View the Result</h3>
      <p>You're all done! Open the <code>index.html</code> file in your web browser to see your styled component.</p>

      <h3>Next Steps</h3>
      <p>Congratulations! You've successfully built your first isolated component with MCSS. Here's where you can go next:</p>
      <ul>
        <li>Dive deeper into the <Link href="/core-concepts">Core Concepts</Link>.</li>
        <li>Explore the full <Link href="/annotations">Annotation System</Link>.</li>
        <li>Browse the <Link href="/components">Component Library</Link>.</li>
      </ul>
    </div>
  );
}
```

#### **`app/components/button/page.tsx`**

TypeScript

```
export default function ButtonPage() {
  return (
    <div>
      <h1>Button</h1>
      <p>Buttons allow users to trigger an action or event, such as submitting a form, opening a dialog, or confirming a choice.</p>

      <h2>Interactive Preview</h2>
      <div style={{ border: '1px solid #ddd', padding: '2rem', borderRadius: '8px', marginTop: '1rem', display: 'flex', gap: '1rem', alignItems: 'center', flexWrap: 'wrap' }}>
        <button mcss-c="button" mcss-p="y:2;x:4" mcss-bg="interactive-primary" mcss-text="white" mcss-rounded="md">
          Primary
        </button>
        <button mcss-c="button" mcss-p="y:2;x:4" mcss-bg="interactive-secondary" mcss-rounded="md">
          Secondary
        </button>
        <button mcss-c="button" mcss-p="y:2;x:4" mcss-bg="destructive" mcss-text="white" mcss-rounded="md">
          Destructive
        </button>
        <button mcss-c="button" mcss-p="y:2;x:4" mcss-bg="interactive-primary" mcss-text="white" mcss-rounded="md" disabled>
          Disabled
        </button>
      </div>

      <h2>Usage</h2>
      <h3>Annotated HTML</h3>
      <pre><code>
{`<button mcss-c="button" 
        mcss-p="y:2;x:4" 
        mcss-bg="interactive-primary" 
        mcss-text="white" 
        mcss-rounded="md">
  Click Me
</button>`}
      </code></pre>
      
      <h3>Required CSS</h3>
      <p>None. The button component is styled entirely through the core MCSS framework and its design tokens.</p>

      <h2>Behavior Contract</h2>
      <p>A component is defined by its behavior as much as its appearance. This contract outlines the expected functionality, interaction states, and accessibility requirements for the button component.</p>
      
      <h3>Interactive States</h3>
      <ul>
        <li><strong>Default:</strong> The button's standard, resting appearance.</li>
        <li><strong>Hover:</strong> The appearance when a user's cursor is over the button.</li>
        <li><strong>Focus:</strong> Must display a visible focus ring to meet accessibility standards.</li>
        <li><strong>Active:</strong> The appearance when the button is being clicked or pressed.</li>
        <li><strong>Disabled:</strong> A muted, lower-contrast look with a <code>not-allowed</code> cursor.</li>
      </ul>

      <h3>Accessibility (A11y)</h3>
      <ul>
        <li><strong>Keyboard Navigation:</strong> The button must be focusable and activatable with Enter/Space.</li>
        <li><strong>Labeling:</strong> The button must have clear, descriptive text. If using an icon, an <code>aria-label</code> is required.</li>
        <li><strong>Contrast:</strong> Text color must have a sufficient contrast ratio against the background.</li>
      </ul>
    </div>
  );
}
```

_(Due to length constraints, I have provided the most critical pages. You can create the other pages like `philosophy`, `core-concepts`, etc., by copying the markdown content from my previous response and converting it into JSX in the same way as the pages above.)_